"""ที่พัก data ตอนโปรแกรม run อยู่ กับการอ่าน/เขียนไฟล์ (ชุดแกนกลาง)

รายละเอียดอยู่ใน docs/tasks/core.md
เปิดไฟล์ CSV ทุกครั้งต้องใส่ newline="" กับ encoding=config.CSV_ENCODING
"""

import csv
import os
from datetime import datetime

from chuaynoi import config
from chuaynoi.core.models import Engagement, HelpRequest, Transaction, User


class AppData:
    """data ทั้งหมดตอน run โปรแกรม ส่งต่อให้ทุก function ในชื่อ app

    attribute: users, requests, engagements, transactions (list ของ object),
               current_user_id (str, "" แปลว่ายังไม่ login), skipped_rows (int)
    """

    def __init__(self):
        self.users = []
        self.requests = []
        self.engagements = []
        self.transactions = []
        self.current_user_id = ""
        self.skipped_rows = 0

    def find_user(self, student_id):
        """return User ที่ student_id ตรงกัน ไม่เจอ return None"""
        for user in self.users:
            if user.student_id == student_id:
                return user
        return None

    def find_request(self, request_id):
        """return HelpRequest ที่ตรงกัน หรือ None"""
        for request in self.requests:
            if request.request_id == request_id:
                return request
        return None

    def find_engagement(self, engagement_id):
        """return Engagement ที่ตรงกัน หรือ None"""
        for engagement in self.engagements:
            if engagement.engagement_id == engagement_id:
                return engagement
        return None

    def next_id(self, prefix, existing_ids, digits):
        """สร้าง id ตัวถัดไป เช่น next_id("R", ["R0001", "R0002"], 4) จะได้ "R0003" ออกมา"""
        biggest = 0
        for old_id in existing_ids:
            number = int(old_id[len(prefix) :])
            if number > biggest:
                biggest = number
        return prefix + str(biggest + 1).zfill(digits)


def load_csv(path, fields, from_row):
    """อ่าน CSV ออกมาเป็น list ของ object แล้ว return (items, skipped)

    ถ้ายังไม่มีไฟล์ ให้สร้างไฟล์ใหม่ที่มีแค่ header ส่วนแถวไหนแปลงไม่ได้ก็ข้ามไป แล้วนับไว้ใน skipped
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
    """เขียนทับ CSV ด้วยทุก object ใน items, return True ถ้าเขียนได้ False ถ้าเขียนไม่ได้"""
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
    """ต่อบรรทัด "[เวลา] รหัสนักศึกษา การกระทำ" ไว้ท้าย activity_log.txt"""
    time_text = datetime.now().strftime(config.TIME_FORMAT)
    line = f"[{time_text}] {student_id} {action}\n"
    try:
        with open(config.ACTIVITY_LOG_FILE, "a", encoding=config.TEXT_ENCODING) as file:
            file.write(line)
    except OSError:
        print(f"ไม่สามารถเขียน log ได้: {line.strip()}")


def load_all():
    """โหลด data ทั้ง 4 ไฟล์ด้วย load_csv แล้ว return AppData ที่พร้อมใช้งาน"""
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
    """save users, requests, engagements ด้วย save_csv แล้ว return True ถ้าเขียนได้ครบทุกไฟล์

    ไม่ต้อง save transactions เพราะ wallet.service.add_transaction เขียนต่อท้ายไฟล์ให้ทันทีอยู่แล้ว
    """
    users_ok = save_csv(config.USERS_FILE, config.USER_FIELDS, app.users)
    requests_ok = save_csv(config.REQUESTS_FILE, config.REQUEST_FIELDS, app.requests)
    engagements_ok = save_csv(
        config.ENGAGEMENTS_FILE, config.ENGAGEMENT_FIELDS, app.engagements
    )
    return users_ok and requests_ok and engagements_ok
