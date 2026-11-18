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
        raise NotImplementedError("TODO(แกนกลาง): AppData.__init__")

    def find_user(self, student_id):
        """return User ที่ student_id ตรงกัน ไม่เจอ return None"""
        raise NotImplementedError("TODO(แกนกลาง): AppData.find_user")

    def find_request(self, request_id):
        """return HelpRequest ที่ตรงกัน หรือ None"""
        raise NotImplementedError("TODO(แกนกลาง): AppData.find_request")

    def find_engagement(self, engagement_id):
        """return Engagement ที่ตรงกัน หรือ None"""
        raise NotImplementedError("TODO(แกนกลาง): AppData.find_engagement")

    def next_id(self, prefix, existing_ids, digits):
        """สร้าง id ตัวถัดไป เช่น next_id("R", ["R0001", "R0002"], 4) จะได้ "R0003" ออกมา"""
        raise NotImplementedError("TODO(แกนกลาง): AppData.next_id")


def load_csv(path, fields, from_row):
    """อ่าน CSV ออกมาเป็น list ของ object แล้ว return (items, skipped)

    ถ้ายังไม่มีไฟล์ ให้สร้างไฟล์ใหม่ที่มีแค่ header ส่วนแถวไหนแปลงไม่ได้ก็ข้ามไป แล้วนับไว้ใน skipped
    """
    raise NotImplementedError("TODO(แกนกลาง): load_csv")


def save_csv(path, fields, items):
    """เขียนทับ CSV ด้วยทุก object ใน items, return True ถ้าเขียนได้ False ถ้าเขียนไม่ได้"""
    raise NotImplementedError("TODO(แกนกลาง): save_csv")


def append_log(student_id, action):
    """ต่อบรรทัด "[เวลา] รหัสนักศึกษา การกระทำ" ไว้ท้าย activity_log.txt"""
    raise NotImplementedError("TODO(แกนกลาง): append_log")


def load_all():
    """โหลด data ทั้ง 4 ไฟล์ด้วย load_csv แล้ว return AppData ที่พร้อมใช้งาน"""
    raise NotImplementedError("TODO(แกนกลาง): load_all")


def save_all(app):
    """save users, requests, engagements ด้วย save_csv แล้ว return True ถ้าเขียนได้ครบทุกไฟล์

    ไม่ต้อง save transactions เพราะ wallet.service.add_transaction เขียนต่อท้ายไฟล์ให้ทันทีอยู่แล้ว
    """
    raise NotImplementedError("TODO(แกนกลาง): save_all")
