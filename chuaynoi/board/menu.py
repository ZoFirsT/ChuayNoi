"""หน้าจอของบอร์ดประกาศ (ชุด A)

ทุกหน้าจอเริ่มด้วย display.print_header(ชื่อหน้า) ถามด้วย ui.inputs แล้วเรียก service
ผลขึ้นต้นด้วย "[OK] " ถ้าสำเร็จ หรือ "[!] " ถ้าไม่สำเร็จ หน้าจอไม่เช็กกฎและไม่ขยับแต้มเอง
เลือกจากรายการด้วยเลขลำดับ (0 = กลับ) ตารางตัด title เหลือ 25 ตัวแรก
ก่อนโพสต์ สมัครช่วย ยืนยันงาน ปิดรับ ต้องถาม y/n
สำเร็จแล้ว storage.save_all(app) แล้ว storage.append_log(...) จบหน้าด้วยการรอ Enter ยกเว้นเลือก 0
ดู: docs/05-contracts.md ข้อ 4
"""

from chuaynoi import config
from chuaynoi.board import search, service
from chuaynoi.core import storage
from chuaynoi.ui import display, inputs
from chuaynoi.wallet.service import get_balance


def screen_board(app):
    """เมนู 1 ดูบอร์ดประกาศ แล้วสมัครช่วยประกาศที่เลือก

    ถาม: คำค้น (เว้นว่างได้), หมวด (หรือทุกหมวด), แต้มขั้นต่ำ, เรียงตาม,
        ลำดับประกาศที่จะสมัคร, ยืนยัน y/n
    คืน: None
    แก้ data: สมัครสำเร็จ save_all(app) แล้ว log "APPLY {request_id} {engagement_id}"
        ถ้าไม่มีประกาศตรงเงื่อนไข แสดง [i] แล้วกลับ
    ดู: docs/05-contracts.md ข้อ 4
    """
    raise NotImplementedError("TODO(ชุด A): screen_board")


def screen_post(app):
    """เมนู 2 โพสต์ประกาศขอความช่วยเหลือ

    ถาม: หัวข้อ, รายละเอียด (เว้นว่างได้), หมวด, แต้มต่อคน, จำนวนผู้ช่วย, เวลาโดยประมาณ (นาที),
        ยืนยัน y/n หลังแสดงสรุปแต้มที่จะถูกกัน
    คืน: None
    แก้ data: โพสต์สำเร็จ save_all(app) แล้ว log "CREATE_REQUEST {request_id}"
        สรุปแต้มเป็นแค่ตัวเลขที่โชว์ ไม่เช็กกฎ ให้ create_request ตัดสิน
    ดู: docs/05-contracts.md ข้อ 4
    """
    raise NotImplementedError("TODO(ชุด A): screen_post")


def screen_my_requests(app):
    """เมนู 3 ดูประกาศของฉัน แล้วยืนยันงานหรือปิดรับ

    ถาม: ลำดับประกาศของฉัน, เมนูยืนยันงานหรือปิดรับ,
        (ยืนยันงาน) ลำดับงานของผู้ช่วย, ยืนยัน y/n
    คืน: None
    แก้ data: สำเร็จ save_all(app) แล้ว log "APPROVE {engagement_id}" หรือ "CLOSE {request_id}"
        0 ที่ระดับไหนก็กลับเมนูหลักทันที ไม่เช็กกฎเอง ให้ approve_work กับ close_request ตัดสิน
    ดู: docs/05-contracts.md ข้อ 4
    """
    raise NotImplementedError("TODO(ชุด A): screen_my_requests")


def screen_my_jobs(app):
    """เมนู 4 ดูงานที่ฉันรับช่วย แล้วส่งงาน

    ถาม: ลำดับงานที่ฉันรับ, ผลงาน (ข้อความหรือลิงก์)
    คืน: None
    แก้ data: ส่งสำเร็จ save_all(app) แล้ว log "SUBMIT {engagement_id}"
    ดู: docs/05-contracts.md ข้อ 4
    """
    raise NotImplementedError("TODO(ชุด A): screen_my_jobs")
