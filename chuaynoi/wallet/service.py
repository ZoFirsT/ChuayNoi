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
    if kind not in config.TRANSACTION_KINDS:
        raise ValueError(f"kind ต้องอยู่ใน {config.TRANSACTION_KINDS} แต่เจอ {kind}")

    txn_id = app.next_id("T", [t.txn_id for t in app.transactions], 6)

    created_at = datetime.now().strftime(config.TIME_FORMAT)
    txn = Transaction(
        txn_id, created_at, student_id, kind, d_available, d_held, request_id, note
    )
    app.transactions.append(txn)

    path = config.TRANSACTIONS_FILE
    is_new_file = not os.path.exists(path) or os.path.getsize(path) == 0
    with open(path, "a", newline="", encoding=config.CSV_ENCODING) as file:
        writer = csv.writer(file)
        if is_new_file:
            writer.writerow(config.TRANSACTION_FIELDS)
        writer.writerow(txn.to_row())

    return txn


def get_balance(app, student_id):
    """return tuple (available, held) ซึ่งก็คือผลรวม d_available กับ d_held ทุกรายการของคนนี้"""
    available = 0
    held = 0
    for txn in app.transactions:
        if txn.student_id == student_id:
            available += txn.d_available
            held += txn.d_held
    return available, held


def list_history(app, student_id, limit=10):
    """return list ของ Transaction ของคนนี้ เรียงล่าสุดขึ้นก่อน ไม่เกิน limit รายการ (ฟังก์ชันช่วย)"""
    history = []
    for txn in app.transactions:
        if txn.student_id == student_id:
            history.append(txn)
    history.reverse()  # เรียงล่าสุดขึ้นก่อน
    return history[:limit]
