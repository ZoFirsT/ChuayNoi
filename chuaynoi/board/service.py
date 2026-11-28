"""rule ของประกาศกับการช่วยงาน (ชุด A)

ทุก function เช็กกฎให้ครบก่อน ผิดข้อไหน return (False, เหตุผล) และ app ต้องเหมือนเดิม
ผ่านหมดค่อยแก้ data แล้ว return (True, ข้อความ) ไฟล์นี้ไม่มี input() กับ print()
แต้มขยับผ่าน add_transaction() เท่านั้น
ดู: docs/tasks/a-board.md หัวข้อ create_request ถึง close_request
"""

from datetime import datetime

from chuaynoi import config
from chuaynoi.core.models import Engagement, HelpRequest
from chuaynoi.wallet.service import add_transaction, get_balance


def create_request(app, owner_id, title, detail, category, reward, slots, minutes):
    """โพสต์ประกาศใหม่ แล้วกันแต้มของผู้ขอไว้ reward × slots

    รับ: owner_id รหัสผู้ขอ, title กับ detail ข้อความประกาศ, category หมวด,
        reward แต้มต่อคน, slots จำนวนผู้ช่วย, minutes เวลาโดยประมาณ (นาที)
    คืน: (True, ข้อความสำเร็จ) หรือ (False, เหตุผล)
    กฎ: CR1–CR8 ตามลำดับ
    แก้ data: เพิ่ม HelpRequest status OPEN ท้าย app.requests
        และรายการ HOLD ของผู้ขอ (ใช้ได้ -cost, กันไว้ +cost)
    ดู: docs/tasks/a-board.md หัวข้อ create_request
    """
    text = title + " " + detail
    for word in config.BANNED_WORDS:
        if word in text:
            return (False, "ประกาศนี้ขอให้ทำงานแทน ผิดกติกา 'ช่วยได้ ไม่ทำแทน'")
    if category not in config.CATEGORIES:
        return (False, f"ไม่มีหมวด {category}")
    if not (config.REWARD_MIN <= reward <= config.REWARD_MAX):
        return (False, f"แต้มต่อคนต้องอยู่ระหว่าง {config.REWARD_MIN} ถึง {config.REWARD_MAX}")
    if not (config.SLOTS_MIN <= slots <= config.SLOTS_MAX):
        return (False, f"จำนวนผู้ช่วยต้องอยู่ระหว่าง {config.SLOTS_MIN} ถึง {config.SLOTS_MAX}")
    if not (config.MINUTES_MIN <= minutes <= config.MINUTES_MAX):
        return (
            False,
            f"เวลาต้องอยู่ระหว่าง {config.MINUTES_MIN} ถึง {config.MINUTES_MAX} นาที",
        )
    if not (config.TITLE_MIN <= len(title) <= config.TITLE_MAX):
        return (False, f"หัวข้อต้องยาว {config.TITLE_MIN} ถึง {config.TITLE_MAX} ตัวอักษร")
    if not (config.DETAIL_MIN <= len(detail) <= config.DETAIL_MAX):
        return (False, f"รายละเอียดต้องไม่เกิน {config.DETAIL_MAX} ตัวอักษร")
    cost = reward * slots
    available, held = get_balance(app, owner_id)
    if available < cost:
        return (False, f"แต้มไม่พอ ต้องใช้ {cost} มี {available}")

    request_id = app.next_id("R", [r.request_id for r in app.requests], 4)
    now = datetime.now().strftime(config.TIME_FORMAT)
    request = HelpRequest(request_id, owner_id, title, detail, category, reward, slots, minutes, config.REQ_OPEN, now)
    app.requests.append(request)
    add_transaction(app, owner_id, config.TXN_HOLD, -cost, cost, request_id, f"กันแต้ม {reward} x {slots} คน")
    return (True, f"โพสต์ประกาศ {request_id} แล้ว กันแต้มไว้ {cost} แต้ม")


def apply_to_request(app, helper_id, request_id):
    """สมัครช่วยประกาศ ถ้ายังมีที่ว่างก็รับงานทันที

    รับ: helper_id รหัสผู้ช่วย, request_id รหัสประกาศ
    คืน: (True, ข้อความสำเร็จ) หรือ (False, เหตุผล)
    กฎ: AP1–AP5 ตามลำดับ
    แก้ data: เพิ่ม Engagement status ACCEPTED ท้าย app.engagements แต้มไม่ขยับ
    ดู: docs/tasks/a-board.md หัวข้อ apply_to_request
    """
    request = app.find_request(request_id)
    if request is None:
        return (False, "ไม่พบประกาศ")
    if request.status != config.REQ_OPEN:
        return (False, "ประกาศนี้ปิดรับแล้ว")
    if request.owner_id == helper_id:
        return (False, "ช่วยงานของตัวเองไม่ได้")
    for eng in app.engagements:
        if eng.request_id == request_id and eng.helper_id == helper_id and eng.status != config.ENG_WITHDRAWN:
            return (False, "คุณรับงานนี้ไปแล้ว")
    if request.count_used_slots(app.engagements) >= request.slots:
        return (False, "ที่เต็มแล้ว")
    engagement_id = app.next_id("E", [e.engagement_id for e in app.engagements], 4)
    now = datetime.now().strftime(config.TIME_FORMAT)
    engagement = Engagement(engagement_id, request_id, helper_id, config.ENG_ACCEPTED, "", 0, now)
    app.engagements.append(engagement)
    return (True, f"รับงาน {request_id} แล้ว รหัสงานของคุณคือ {engagement_id}")


def submit_work(app, helper_id, engagement_id, result):
    """ผู้ช่วยส่งผลงานของงานที่รับไว้

    รับ: helper_id รหัสผู้ช่วย, engagement_id รหัสงาน, result ผลงาน (ข้อความหรือลิงก์)
    คืน: (True, ข้อความสำเร็จ) หรือ (False, เหตุผล)
    กฎ: SW1–SW3 ตามลำดับ
    แก้ data: engagement เปลี่ยนเป็น SUBMITTED เก็บ result กับ updated_at แต้มไม่ขยับ
    ดู: docs/tasks/a-board.md หัวข้อ submit_work
    """
    engagement = app.find_engagement(engagement_id)
    if engagement is None or engagement.helper_id != helper_id:
        return (False, "ไม่พบงานนี้ในงานที่คุณรับไว้")
    if not (config.RESULT_MIN <= len(result.strip()) <= config.RESULT_MAX):
        return (False, f"ผลงานต้องยาว {config.RESULT_MIN} ถึง {config.RESULT_MAX} ตัวอักษร")
    if engagement.status not in (config.ENG_ACCEPTED, config.ENG_REVISION):
        return (False, f"ส่งงานนี้ไม่ได้ เพราะ status ตอนนี้คือ {engagement.status}")

    engagement.change_status(config.ENG_SUBMITTED)
    engagement.result = result.strip()
    engagement.updated_at = datetime.now().strftime(config.TIME_FORMAT)
    return (True, f"ส่งงาน {engagement_id} แล้ว รอผู้ขอยืนยัน")


def approve_work(app, owner_id, engagement_id):
    """ผู้ขอยืนยันงานที่ส่งมา แล้วโอนแต้มให้ผู้ช่วย

    รับ: owner_id รหัสผู้ขอ, engagement_id รหัสงาน
    คืน: (True, ข้อความสำเร็จ) หรือ (False, เหตุผล)
    กฎ: AV1–AV2 ตามลำดับ
    แก้ data: engagement เปลี่ยนเป็น APPROVED, เพิ่มรายการ PAY ของผู้ขอ (กันไว้ -reward)
        กับ EARN ของผู้ช่วย (ใช้ได้ +reward) ถ้าไม่เหลืองานค้างและประกาศปิดรับแล้วหรือที่เต็มแล้ว
        ประกาศเปลี่ยนเป็น COMPLETED
    ดู: docs/tasks/a-board.md หัวข้อ approve_work
    """
    engagement = app.find_engagement(engagement_id)
    if engagement is None:
        return (False, "ไม่พบงานนี้ในประกาศของคุณ")
    request = app.find_request(engagement.request_id)
    if request is None or request.owner_id != owner_id:
        return (False, "ไม่พบงานนี้ในประกาศของคุณ")
    if engagement.status != config.ENG_SUBMITTED:
        return (False, "ยืนยันได้เฉพาะงานที่ส่งแล้ว")

    engagement.change_status(config.ENG_APPROVED)
    engagement.updated_at = datetime.now().strftime(config.TIME_FORMAT)

    add_transaction(app, owner_id, config.TXN_PAY, 0, -request.reward, request.request_id, f"จ่ายให้ {engagement_id}")
    add_transaction(app, engagement.helper_id, config.TXN_EARN, request.reward, 0, request.request_id, f"ได้รับจาก {request.request_id}")

    has_active = False
    for eng in app.engagements:
        if eng.request_id == request.request_id and eng.status in config.ACTIVE_ENGAGEMENT_STATUSES:
            has_active = True
            break
    if not has_active and (request.status == config.REQ_CLOSED or request.count_used_slots(app.engagements) >= request.slots):
        request.status = config.REQ_COMPLETED

    helper = app.find_user(engagement.helper_id)
    helper_name = helper.name if helper else engagement.helper_id
    return (True, f"ยืนยันงานแล้ว โอน {request.reward} แต้มให้ {helper_name}")


def close_request(app, owner_id, request_id):
    """ผู้ขอปิดรับผู้ช่วย แล้วคืนแต้มของ slot ที่ไม่มีใครรับ

    รับ: owner_id รหัสผู้ขอ, request_id รหัสประกาศ
    คืน: (True, ข้อความสำเร็จ) หรือ (False, เหตุผล)
    กฎ: CL1–CL2 ตามลำดับ
    แก้ data: ถ้ามี slot ที่ไม่ได้ใช้ เพิ่มรายการ REFUND ของผู้ขอ (ใช้ได้ +refund, กันไว้ -refund)
        status ประกาศเป็น CANCELLED (ไม่มีใครรับเลย), COMPLETED (ไม่เหลืองานค้าง) หรือ CLOSED (ยังมีงานค้าง)
    ดู: docs/tasks/a-board.md หัวข้อ close_request
    """
    request = app.find_request(request_id)
    if request is None or request.owner_id != owner_id:
        return (False, "ไม่พบประกาศนี้ในประกาศของคุณ")
    if request.status != config.REQ_OPEN:
        return (False, "ปิดรับได้เฉพาะประกาศที่เปิดอยู่")
    used = request.count_used_slots(app.engagements)
    unused = request.slots - used
    refund = unused * request.reward
    if unused > 0:
        add_transaction(app, owner_id, config.TXN_REFUND, refund, -refund, request_id, f"คืนที่ว่าง {unused} ที่")

    has_active = False
    for eng in app.engagements:
        if eng.request_id == request_id and eng.status in config.ACTIVE_ENGAGEMENT_STATUSES:
            has_active = True
            break

    if used == 0:
        request.status = config.REQ_CANCELLED
    elif not has_active:
        request.status = config.REQ_COMPLETED
    else:
        request.status = config.REQ_CLOSED

    return (True, f"ปิดรับ {request_id} แล้ว คืน {refund} แต้ม")
