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
    raise NotImplementedError("TODO(ชุด A): create_request")


def apply_to_request(app, helper_id, request_id):
    """สมัครช่วยประกาศ ถ้ายังมีที่ว่างก็รับงานทันที

    รับ: helper_id รหัสผู้ช่วย, request_id รหัสประกาศ
    คืน: (True, ข้อความสำเร็จ) หรือ (False, เหตุผล)
    กฎ: AP1–AP5 ตามลำดับ
    แก้ data: เพิ่ม Engagement status ACCEPTED ท้าย app.engagements แต้มไม่ขยับ
    ดู: docs/tasks/a-board.md หัวข้อ apply_to_request
    """
    raise NotImplementedError("TODO(ชุด A): apply_to_request")


def submit_work(app, helper_id, engagement_id, result):
    """ผู้ช่วยส่งผลงานของงานที่รับไว้

    รับ: helper_id รหัสผู้ช่วย, engagement_id รหัสงาน, result ผลงาน (ข้อความหรือลิงก์)
    คืน: (True, ข้อความสำเร็จ) หรือ (False, เหตุผล)
    กฎ: SW1–SW3 ตามลำดับ
    แก้ data: engagement เปลี่ยนเป็น SUBMITTED เก็บ result กับ updated_at แต้มไม่ขยับ
    ดู: docs/tasks/a-board.md หัวข้อ submit_work
    """
    raise NotImplementedError("TODO(ชุด A): submit_work")


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
    raise NotImplementedError("TODO(ชุด A): approve_work")


def close_request(app, owner_id, request_id):
    """ผู้ขอปิดรับผู้ช่วย แล้วคืนแต้มของslot ที่ไม่มีใครรับ

    รับ: owner_id รหัสผู้ขอ, request_id รหัสประกาศ
    คืน: (True, ข้อความสำเร็จ) หรือ (False, เหตุผล)
    กฎ: CL1–CL2 ตามลำดับ
    แก้ data: ถ้ามีslot ที่ไม่ได้ใช้ เพิ่มรายการ REFUND ของผู้ขอ (ใช้ได้ +refund, กันไว้ -refund)
        status ประกาศเป็น CANCELLED (ไม่มีใครรับเลย), COMPLETED (ไม่เหลืองานค้าง) หรือ CLOSED (ยังมีงานค้าง)
    ดู: docs/tasks/a-board.md หัวข้อ close_request
    """
    raise NotImplementedError("TODO(ชุด A): close_request")
