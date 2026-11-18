"""rule ของประกาศกับ flow การช่วยงาน ไฟล์นี้ห้ามมี input/print (ชุด A)

ทุก function เป็น pattern เดียวกัน: เช็ก rule ให้ครบก่อน ผ่านแล้วค่อยแก้ data แล้ว return (success, message)
ถ้าผิด rule ข้อไหนก็ตาม data ต้องเหมือนเดิมเป๊ะ
step ของแต่ละ function อยู่ใน docs/tasks/a-board.md
"""

from datetime import datetime

from chuaynoi import config
from chuaynoi.core.models import Engagement, HelpRequest
from chuaynoi.wallet.service import add_transaction, get_balance


def create_request(app, owner_id, title, detail, category, reward, slots, minutes):
    """โพสต์ประกาศใหม่แล้วกันแต้มไว้ reward x slots, return (success, message)

    ไม่ให้โพสต์ถ้ามีคำต้องห้าม, แต้มต่อคนหรือจำนวนคนเกินช่วง หรือแต้มใช้ได้ไม่พอ
    """
    raise NotImplementedError("TODO(ชุด A): create_request")


def apply_to_request(app, helper_id, request_id):
    """สมัครช่วยงาน ถ้ายังมีที่ว่างก็รับเลย return (success, message)

    ไม่ให้สมัครถ้าหาประกาศไม่เจอหรือประกาศไม่เปิดรับ, จะช่วยงานตัวเอง, เคยรับงานนี้แล้ว หรือที่เต็ม
    """
    raise NotImplementedError("TODO(ชุด A): apply_to_request")


def submit_work(app, helper_id, engagement_id, result):
    """ผู้ช่วยส่งงาน (เป็นข้อความหรือ link ก็ได้) แล้วเปลี่ยน status เป็น SUBMITTED, return (success, message)"""
    raise NotImplementedError("TODO(ชุด A): submit_work")


def approve_work(app, owner_id, engagement_id):
    """เจ้าของประกาศยืนยันงานที่ส่งมา แล้วโอนแต้มให้ผู้ช่วย return (success, message)"""
    raise NotImplementedError("TODO(ชุด A): approve_work")


def close_request(app, owner_id, request_id):
    """ปิดรับผู้ช่วย คืนแต้มของที่ที่ไม่มีใครรับ แล้วตั้ง status ใหม่ return (success, message)"""
    raise NotImplementedError("TODO(ชุด A): close_request")
