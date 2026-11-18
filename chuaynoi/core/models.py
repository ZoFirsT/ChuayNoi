"""data class หลักของโปรแกรม (1 object = 1 แถวใน CSV) ชุดแกนกลางเป็นคนเขียน

attribute ของทุก class ดูได้ใน docs/02-design.md หัวข้อ "คลาสและ attribute"
ทุกชุดใช้ชื่อตามนั้นเป๊ะ ๆ ถ้าจะเปลี่ยนชื่อต้องบอกทีมก่อน

ทุก class มี 2 ตัวนี้
    to_row()           แปลง object เป็น list ไว้เขียนลง CSV (เรียงตาม *_FIELDS ใน config)
    from_row(row)      แปลง dict 1 แถวจาก csv.DictReader กลับเป็น object
                       ถ้า data ผิด format ให้ ValueError หลุดออกไปเลย (storage จะข้ามแถวนั้นเอง)
"""

from chuaynoi import config


class User:
    """นักศึกษา 1 คน (users.csv) เป็นได้ทั้งคนขอและคนช่วย ยอดแต้มไม่ได้เก็บไว้ตรงนี้"""

    def __init__(self, student_id, name, faculty, skills, created_at):
        """เก็บทุก parameter เป็น attribute ชื่อเดียวกัน (skills เป็น list ของ str)"""
        raise NotImplementedError("TODO(แกนกลาง): User.__init__")

    def to_row(self):
        raise NotImplementedError("TODO(แกนกลาง): User.to_row")

    @staticmethod
    def from_row(row):
        raise NotImplementedError("TODO(แกนกลาง): User.from_row")


class HelpRequest:
    """ประกาศขอให้ช่วย 1 อัน (requests.csv)"""

    def __init__(self, request_id, owner_id, title, detail, category,
                 reward, slots, minutes, status, created_at):
        """เก็บทุก parameter เป็น attribute ชื่อเดียวกัน (reward, slots, minutes เป็น int)"""
        raise NotImplementedError("TODO(แกนกลาง): HelpRequest.__init__")

    def total_cost(self):
        """แต้มที่ต้องกันไว้ตอนโพสต์ = reward x slots"""
        raise NotImplementedError("TODO(แกนกลาง): HelpRequest.total_cost")

    def count_used_slots(self, engagements):
        """นับว่าที่ถูกใช้ไปกี่ที่แล้ว (นับผู้ช่วยของประกาศนี้ที่ยังทำอยู่หรือยืนยันแล้ว คนที่ถอนตัวไม่นับ)"""
        raise NotImplementedError("TODO(แกนกลาง): HelpRequest.count_used_slots")

    def to_row(self):
        raise NotImplementedError("TODO(แกนกลาง): HelpRequest.to_row")

    @staticmethod
    def from_row(row):
        raise NotImplementedError("TODO(แกนกลาง): HelpRequest.from_row")


class Engagement:
    """ผู้ช่วย 1 คนในประกาศ 1 อัน (engagements.csv)"""

    def __init__(self, engagement_id, request_id, helper_id, status,
                 result, revisions, updated_at):
        """เก็บทุก parameter เป็น attribute ชื่อเดียวกัน (revisions เป็น int)"""
        raise NotImplementedError("TODO(แกนกลาง): Engagement.__init__")

    def change_status(self, new_status):
        """เปลี่ยน status ตาม config.ALLOWED_TRANSITIONS ถ้าไปต่อไม่ได้ให้ raise ValueError พร้อมบอกเหตุผล"""
        raise NotImplementedError("TODO(แกนกลาง): Engagement.change_status")

    def to_row(self):
        raise NotImplementedError("TODO(แกนกลาง): Engagement.to_row")

    @staticmethod
    def from_row(row):
        raise NotImplementedError("TODO(แกนกลาง): Engagement.from_row")


class Transaction:
    """รายการแต้มที่ขยับ 1 รายการ (transactions.csv) มีแต่เพิ่มต่อท้าย ห้ามแก้ของเดิม"""

    def __init__(self, txn_id, created_at, student_id, kind,
                 d_available, d_held, request_id, note):
        """เก็บทุก parameter เป็น attribute ชื่อเดียวกัน (d_available, d_held เป็น int)"""
        raise NotImplementedError("TODO(แกนกลาง): Transaction.__init__")

    def to_row(self):
        raise NotImplementedError("TODO(แกนกลาง): Transaction.to_row")

    @staticmethod
    def from_row(row):
        raise NotImplementedError("TODO(แกนกลาง): Transaction.from_row")
