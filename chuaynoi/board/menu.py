"""หน้าจอของบอร์ดประกาศ (ชุด A)

ทุกหน้าจอทำเหมือนกัน: ถามด้วย ui.inputs แล้วเรียก service จากนั้นโชว์ [OK] หรือ [!]
ถ้าสำเร็จให้ storage.save_all(app) กับ storage.append_log(...) ด้วย
อะไรที่ย้อนกลับไม่ได้ (ยืนยันงาน ปิดรับ) ต้องถาม y/n ก่อนทุกครั้ง
"""

from chuaynoi import config
from chuaynoi.board import search, service
from chuaynoi.core import storage
from chuaynoi.ui import display, inputs
from chuaynoi.wallet.service import get_balance


def screen_board(app):
    """เมนู 1: ถามคำค้น หมวด แต้มขั้นต่ำ กับการเรียง โชว์เป็นตาราง แล้วให้เลือกประกาศที่จะสมัครช่วย"""
    raise NotImplementedError("TODO(ชุด A): screen_board")


def screen_post(app):
    """เมนู 2: ถามรายละเอียดประกาศ โชว์ว่าจะโดนกันแต้มเท่าไหร่ ถาม y/n แล้วค่อยโพสต์"""
    raise NotImplementedError("TODO(ชุด A): screen_post")


def screen_my_requests(app):
    """เมนู 3: โชว์ประกาศของเรากับผู้ช่วยแต่ละคน ให้เลือกว่าจะยืนยันงานหรือปิดรับ"""
    raise NotImplementedError("TODO(ชุด A): screen_my_requests")


def screen_my_jobs(app):
    """เมนู 4: โชว์งานที่เรารับไว้ แล้วให้เลือกส่งงาน"""
    raise NotImplementedError("TODO(ชุด A): screen_my_jobs")
