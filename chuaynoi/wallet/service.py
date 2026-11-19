"""สมุดบัญชีแต้ม เพิ่มรายการแต้ม ดูยอด ดูประวัติ (แกนกลาง)

ไม่เก็บยอดคงเหลือไว้ที่ไหน ยอดคือผลรวมของรายการใน transactions.csv
แต้มรวมของทุกคน (ใช้ได้ + กันไว้) ต้องเท่ากับ config.START_POINTS × จำนวนผู้ใช้เสมอ
ไฟล์นี้ไม่มี input() กับ print()
ดู: docs/05-contracts.md ข้อ 2 และข้อ 6
"""

import csv
import os
from datetime import datetime

from chuaynoi import config
from chuaynoi.core.models import Transaction


def add_transaction(app, student_id, kind, d_available, d_held, request_id="", note=""):
    """เพิ่มรายการแต้ม 1 รายการ เขียนต่อท้าย transactions.csv ทันที แล้วค่อยเพิ่มเข้า app.transactions

    รับ: kind ต้องอยู่ใน config.TRANSACTION_KINDS, d_available กับ d_held
        คือแต้มที่เปลี่ยน (+ เพิ่ม, - ลด), request_id ใส่ "" ถ้าไม่เกี่ยวกับประกาศ
    คืน: Transaction ตัวที่เพิ่งสร้าง (รหัส T + 6 หลัก)
    แก้ data: เขียนต่อท้าย transactions.csv ก่อน สำเร็จแล้วค่อยต่อท้าย app.transactions
        ไม่ต้องรอ save_all()
    error: raise ValueError ถ้า kind ไม่ถูก (ตอนนั้นยังไม่แก้อะไร)
        ถ้าเขียนไฟล์ไม่ได้ OSError จะหลุดออกไป และ app.transactions ไม่เปลี่ยน
    ดู: docs/05-contracts.md ข้อ 2
    """
    if kind not in config.TRANSACTION_KINDS:
        raise ValueError(f"kind ต้องอยู่ใน {config.TRANSACTION_KINDS} แต่เจอ {kind}")

    txn_id = app.next_id("T", [t.txn_id for t in app.transactions], 6)

    created_at = datetime.now().strftime(config.TIME_FORMAT)
    txn = Transaction(
        txn_id, created_at, student_id, kind, d_available, d_held, request_id, note
    )

    path = config.TRANSACTIONS_FILE
    is_new_file = not os.path.exists(path) or os.path.getsize(path) == 0
    with open(path, "a", newline="", encoding=config.CSV_ENCODING) as file:
        writer = csv.writer(file)
        if is_new_file:
            writer.writerow(config.TRANSACTION_FIELDS)
        writer.writerow(txn.to_row())

    app.transactions.append(txn)

    return txn


def get_balance(app, student_id):
    """รวมแต้มของนักศึกษาคนหนึ่งจากรายการใน app.transactions

    รับ: student_id รหัสนักศึกษา
    คืน: tuple (available, held) เป็น int ผลรวม d_available กับ d_held ของคนนี้
    แก้ data: ไม่แก้อะไร
    ดู: docs/05-contracts.md ข้อ 2
    """
    available = 0
    held = 0
    for txn in app.transactions:
        if txn.student_id == student_id:
            available += txn.d_available
            held += txn.d_held
    return available, held


def list_history(app, student_id, limit=10):
    """เอารายการแต้มของนักศึกษาคนนี้ เรียงล่าสุดก่อน ไม่เกิน limit รายการ คืน list ของ Transaction (function ช่วย)"""
    history = []
    for txn in app.transactions:
        if txn.student_id == student_id:
            history.append(txn)
    history.reverse()  # เรียงล่าสุดขึ้นก่อน
    return history[:limit]
