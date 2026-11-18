"""สมุดบัญชีแต้ม ไฟล์นี้ห้ามมี input/print (ชุดแกนกลาง)

เราไม่เก็บยอดคงเหลือไว้ตรง ๆ แต่เก็บเป็นรายการต่อท้ายไปเรื่อย ๆ แล้วคำนวณยอดใหม่ทุกครั้ง
สิ่งที่ต้องจริงตลอด: ผลรวม (ใช้ได้ + กันไว้) ของทุกคน == config.START_POINTS x จำนวนผู้ใช้
ชุด A กับชุด B เรียก function ในไฟล์นี้ ถ้าจะเปลี่ยนชื่อหรือ parameter ต้องบอกทีมก่อน
รายละเอียดอยู่ใน docs/tasks/core.md
"""

import csv
import os
from datetime import datetime

from chuaynoi import config
from chuaynoi.core.models import Transaction


def add_transaction(app, student_id, kind, d_available, d_held, request_id="", note=""):
    """สร้างรายการแต้มใหม่ ใส่เข้า app.transactions แล้วเขียนต่อท้าย transactions.csv เลย

    return Transaction ที่สร้าง ถ้า kind ไม่อยู่ใน config.TRANSACTION_KINDS ให้ raise ValueError
    """
    raise NotImplementedError("TODO(แกนกลาง): add_transaction")


def get_balance(app, student_id):
    """return tuple (available, held) ซึ่งก็คือผลรวม d_available กับ d_held ทุกรายการของคนนี้"""
    raise NotImplementedError("TODO(แกนกลาง): get_balance")


def list_history(app, student_id, limit=10):
    """return list ของ Transaction ของคนนี้ เรียงล่าสุดขึ้นก่อน ไม่เกิน limit รายการ (ฟังก์ชันช่วย)"""
    raise NotImplementedError("TODO(แกนกลาง): list_history")
