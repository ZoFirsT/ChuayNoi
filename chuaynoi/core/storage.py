"""ที่เก็บ data ตอนโปรแกรม run กับการอ่าน/เขียนไฟล์ (แกนกลาง)

เปิดไฟล์ CSV ทุกครั้งใส่ newline="" กับ encoding=config.CSV_ENCODING
รายการแต้มไม่ได้เขียนที่นี่ ให้เขียนผ่าน wallet.service.add_transaction()
ดู: docs/05-contracts.md ข้อ 2
"""

import csv
import os
from datetime import datetime

from chuaynoi import config
from chuaynoi.core.models import Engagement, HelpRequest, Transaction, User


class AppData:
    """data ทั้งหมดตอน run โปรแกรม ส่งต่อให้ทุก function ในชื่อ app

    attribute: users, requests, engagements, transactions (list ของ object เรียงตามไฟล์ เก่าสุดก่อน),
        current_user_id (str, "" แปลว่ายังไม่มีใคร login),
        skipped_rows (int, จำนวนแถวที่อ่านไม่ผ่านตอน load)
    ดู: docs/05-contracts.md ข้อ 2
    """

    def __init__(self):
        """เริ่มด้วย list ว่าง 4 ตัว current_user_id เป็น "" และ skipped_rows เป็น 0"""
        self.users = []
        self.requests = []
        self.engagements = []
        self.transactions = []
        self.current_user_id = ""
        self.skipped_rows = 0

    def find_user(self, student_id):
        """หา User จากรหัสนักศึกษา

        คืน: ตัว User จริงใน self.users (แก้ที่ตัวนี้ app เปลี่ยนตาม) หรือ None ถ้าไม่เจอ
        """
        for user in self.users:
            if user.student_id == student_id:
                return user
        return None

    def find_request(self, request_id):
        """หา HelpRequest จากรหัสประกาศ

        คืน: ตัว HelpRequest จริงใน self.requests หรือ None ถ้าไม่เจอ
        """
        for request in self.requests:
            if request.request_id == request_id:
                return request
        return None

    def find_engagement(self, engagement_id):
        """หา Engagement จากรหัสงาน

        คืน: ตัว Engagement จริงใน self.engagements หรือ None ถ้าไม่เจอ
        """
        for engagement in self.engagements:
            if engagement.engagement_id == engagement_id:
                return engagement
        return None

    def next_id(self, prefix, existing_ids, digits):
        """สร้างรหัสถัดไปของ prefix นั้น

        รับ: prefix เช่น "R", existing_ids รหัสที่มีอยู่แล้ว, digits จำนวนหลักของตัวเลข
        คืน: prefix + (เลขมากสุดที่มี + 1) เติม 0 ให้ครบ digits ถ้ายังไม่มีรหัสเลยได้เลข 1
            เช่น next_id("R", ["R0001", "R0002"], 4) ได้ "R0003"
        แก้ data: ไม่แก้อะไร
        """
        biggest = 0
        for old_id in existing_ids:
            number = int(old_id[len(prefix) :])
            if number > biggest:
                biggest = number
        return prefix + str(biggest + 1).zfill(digits)


def load_csv(path, fields, from_row):
    """อ่าน CSV 1 ไฟล์เป็น list ของ object

    รับ: path ไฟล์, fields header ที่ใช้ตอนสร้างไฟล์ใหม่, from_row function แปลง dict 1 แถวเป็น object
    คืน: (items, skipped) skipped คือจำนวนแถวที่ from_row raise ValueError หรือ KeyError แล้วถูกข้าม
    แก้ data: ถ้ายังไม่มีไฟล์ สร้างไฟล์ที่มีแต่ header (กับ folder data/ ถ้ายังไม่มี)
    error: จับแค่ ValueError กับ KeyError ของแต่ละแถว
        แถวที่ column ไม่ครบจน from_row raise TypeError ไม่ถูกจับ โปรแกรมจะหยุด
    ดู: docs/05-contracts.md ข้อ 2
    """
    os.makedirs(config.DATA_DIR, exist_ok=True)
    if not os.path.exists(path):
        save_csv(path, fields, [])
        return ([], 0)

    items = []
    skipped = 0
    with open(path, "r", newline="", encoding=config.CSV_ENCODING) as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                items.append(from_row(row))
            except (ValueError, KeyError):
                skipped += 1
    return (items, skipped)


def save_csv(path, fields, items):
    """เขียนทับ CSV ด้วย object ทุกตัวใน items

    รับ: path ไฟล์, fields header, items list ของ object ที่มี to_row()
    คืน: True ถ้าเขียนได้ False ถ้าเขียนไม่ได้
    แก้ data: เขียนทับทั้งไฟล์
    error: จับ OSError ไว้แล้วคืน False ไม่ raise ออกไป
    """
    try:
        with open(path, "w", newline="", encoding=config.CSV_ENCODING) as file:
            writer = csv.writer(file)
            writer.writerow(fields)
            for item in items:
                writer.writerow(item.to_row())
    except OSError:
        return False
    return True


def append_log(student_id, action):
    """ต่อท้าย activity_log.txt 1 บรรทัด รูปแบบ [YYYY-MM-DD HH:MM] {student_id} {action}

    รับ: student_id รหัสผู้ทำ, action ข้อความการกระทำ เช่น "LOGIN" (ชื่อ action อยู่ใน docs/05-contracts.md ข้อ 5)
    คืน: ไม่คืนค่า
    แก้ data: ต่อท้าย activity_log.txt
    error: จับ OSError แล้ว print() บรรทัดเตือน (ไม่มี prefix [!]) โปรแกรมไม่หยุด
    ดู: docs/05-contracts.md ข้อ 5
    """
    time_text = datetime.now().strftime(config.TIME_FORMAT)
    line = f"[{time_text}] {student_id} {action}\n"
    try:
        with open(config.ACTIVITY_LOG_FILE, "a", encoding=config.TEXT_ENCODING) as file:
            file.write(line)
    except OSError:
        print(f"ไม่สามารถเขียน log ได้: {line.strip()}")


def load_all():
    """โหลด users, requests, engagements, transactions ด้วย load_csv

    คืน: AppData ที่พร้อมใช้ (skipped_rows รวมแถวที่ข้ามของทั้ง 4 ไฟล์)
    แก้ data: สร้าง folder data/ กับไฟล์ที่ยังไม่มี (แค่ header)
    error: ไม่จับอะไร Ctrl+C ตอนโหลด หรือแถวที่ column ไม่ครบ ทำให้โปรแกรมหยุด
    ดู: docs/05-contracts.md ข้อ 2
    """
    app = AppData()
    app.users, skipped = load_csv(config.USERS_FILE, config.USER_FIELDS, User.from_row)
    app.skipped_rows += skipped
    app.requests, skipped = load_csv(
        config.REQUESTS_FILE, config.REQUEST_FIELDS, HelpRequest.from_row
    )
    app.skipped_rows += skipped
    app.engagements, skipped = load_csv(
        config.ENGAGEMENTS_FILE, config.ENGAGEMENT_FIELDS, Engagement.from_row
    )
    app.skipped_rows += skipped
    app.transactions, skipped = load_csv(
        config.TRANSACTIONS_FILE, config.TRANSACTION_FIELDS, Transaction.from_row
    )
    app.skipped_rows += skipped
    return app


def save_all(app):
    """เขียน users, requests, engagements ลงไฟล์ด้วย save_csv

    คืน: True ถ้าเขียนได้ครบทุกไฟล์ False ถ้ามีไฟล์ที่เขียนไม่ได้ (ไม่ raise OSError)
    แก้ data: เขียนทับ users.csv, requests.csv, engagements.csv
        ไม่แตะ transactions.csv เพราะ add_transaction() เขียนต่อท้ายให้ทุกครั้งอยู่แล้ว
    ดู: docs/05-contracts.md ข้อ 2
    """
    users_ok = save_csv(config.USERS_FILE, config.USER_FIELDS, app.users)
    requests_ok = save_csv(config.REQUESTS_FILE, config.REQUEST_FIELDS, app.requests)
    engagements_ok = save_csv(
        config.ENGAGEMENTS_FILE, config.ENGAGEMENT_FIELDS, app.engagements
    )
    return users_ok and requests_ok and engagements_ok
