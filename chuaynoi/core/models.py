"""data class หลักของโปรแกรม 1 object = 1 แถวใน CSV (แกนกลาง)

ทุก class มี to_row() แปลง object เป็น list ตามลำดับ *_FIELDS ใน config
กับ from_row(row) แปลง dict 1 แถวจาก csv.DictReader กลับเป็น object
ชื่อ attribute ของทุก class เป็นข้อตกลงร่วมของทุกชุด ห้ามเปลี่ยน
ดู: docs/02-design.md หัวข้อ User, HelpRequest, Engagement และ Transaction
"""

from chuaynoi import config


class User:
    """นักศึกษา 1 คน (users.csv) เป็นได้ทั้งผู้ขอและผู้ช่วย ยอดแต้มไม่ได้เก็บไว้ที่นี่

    ดู: docs/02-design.md หัวข้อ User
    """

    def __init__(self, student_id, name, faculty, skills, created_at):
        """เก็บทุก parameter เป็น attribute ชื่อเดียวกัน (skills เป็น list ของ str)"""
        self.student_id = student_id
        self.name = name
        self.faculty = faculty
        self.skills = skills
        self.created_at = created_at

    def to_row(self):
        """แปลงเป็น list 1 แถวไว้เขียน CSV (skills ต่อกันด้วย config.SKILL_SEPARATOR)"""
        return [
            self.student_id,
            self.name,
            self.faculty,
            config.SKILL_SEPARATOR.join(self.skills),
            self.created_at,
        ]

    @staticmethod
    def from_row(row):
        """แปลง dict 1 แถวเป็น User (skills ว่างได้ list ว่าง) raise ValueError ถ้า faculty ไม่อยู่ใน config.FACULTIES"""
        if row["faculty"] not in config.FACULTIES:
            raise ValueError(f"Invalid faculty: {row['faculty']}")

        if row["skills"] == "":
            skills = []
        else:
            skills = row["skills"].split(config.SKILL_SEPARATOR)

        return User(
            row["student_id"], row["name"], row["faculty"], skills, row["created_at"]
        )


class HelpRequest:
    """ประกาศขอให้ช่วย 1 อัน (requests.csv)

    ดู: docs/02-design.md หัวข้อ HelpRequest
    """

    def __init__(
        self,
        request_id,
        owner_id,
        title,
        detail,
        category,
        reward,
        slots,
        minutes,
        status,
        created_at,
    ):
        """เก็บทุก parameter เป็น attribute ชื่อเดียวกัน (reward, slots, minutes เป็น int)"""
        self.request_id = request_id
        self.owner_id = owner_id
        self.title = title
        self.detail = detail
        self.category = category
        self.reward = reward
        self.slots = slots
        self.minutes = minutes
        self.status = status
        self.created_at = created_at

    def total_cost(self):
        """หาแต้มที่ต้องกันไว้ตอนโพสต์

        คืน: reward × slots (int)
        แก้ data: ไม่แก้อะไร
        """
        return self.reward * self.slots

    def count_used_slots(self, engagements):
        """นับจำนวน slot ในประกาศนี้ที่ถูกจองไปแล้ว

        รับ: engagements list ของ Engagement ทั้งหมด (ปกติคือ app.engagements)
        คืน: จำนวน engagement ของประกาศนี้ที่ status อยู่ใน config.ACTIVE_ENGAGEMENT_STATUSES
            หรือเป็น ENG_APPROVED (ผู้ช่วยที่ถอนตัว WITHDRAWN ไม่นับ)
        แก้ data: ไม่แก้อะไร
        ดู: docs/02-design.md หัวข้อ HelpRequest
        """
        count = 0
        for e in engagements:
            if e.request_id == self.request_id and (
                e.status in config.ACTIVE_ENGAGEMENT_STATUSES
                or e.status == config.ENG_APPROVED
            ):
                count += 1
        return count

    def to_row(self):
        """แปลงเป็น list 1 แถวไว้เขียน CSV (เรียงตาม config.REQUEST_FIELDS)"""
        return [
            self.request_id,
            self.owner_id,
            self.title,
            self.detail,
            self.category,
            self.reward,
            self.slots,
            self.minutes,
            self.status,
            self.created_at,
        ]

    @staticmethod
    def from_row(row):
        """แปลง dict 1 แถวเป็น HelpRequest raise ValueError ถ้า reward, slots, minutes ไม่ใช่ตัวเลข หรือ status กับ category ไม่อยู่ใน config"""
        reward = int(row["reward"])
        slots = int(row["slots"])
        minutes = int(row["minutes"])

        if row["status"] not in config.REQUEST_STATUSES:
            raise ValueError(f"Invalid req status: {row['status']}")

        if row["category"] not in config.CATEGORIES:
            raise ValueError(f"Invalid category: {row['category']}")

        return HelpRequest(
            row["request_id"],
            row["owner_id"],
            row["title"],
            row["detail"],
            row["category"],
            reward,
            slots,
            minutes,
            row["status"],
            row["created_at"],
        )


class Engagement:
    """ผู้ช่วย 1 คนในประกาศ 1 อัน (engagements.csv) status เปลี่ยนได้ตาม config.ALLOWED_TRANSITIONS

    ดู: docs/02-design.md หัวข้อ Engagement
    """

    def __init__(
        self,
        engagement_id,
        request_id,
        helper_id,
        status,
        result,
        revisions,
        updated_at,
    ):
        """เก็บทุก parameter เป็น attribute ชื่อเดียวกัน (revisions เป็น int)"""
        self.engagement_id = engagement_id
        self.request_id = request_id
        self.helper_id = helper_id
        self.status = status
        self.result = result
        self.revisions = revisions
        self.updated_at = updated_at

    def change_status(self, new_status):
        """เปลี่ยน status ตามเส้นทางที่ config.ALLOWED_TRANSITIONS อนุญาต

        รับ: new_status status ใหม่
        คืน: ไม่คืนค่า
        แก้ data: self.status เป็น new_status (updated_at ไม่เปลี่ยนเอง ผู้เรียกตั้งเอง)
        error: raise ValueError("เปลี่ยน status จาก {เดิม} ไป {ใหม่} ไม่ได้") ถ้าเปลี่ยนไม่ได้ ตอนนั้นยังไม่แก้อะไร
        ดู: docs/02-design.md หัวข้อ Engagement
        """
        allowed = config.ALLOWED_TRANSITIONS.get(self.status, ())
        if new_status not in allowed:
            raise ValueError(f"เปลี่ยน status จาก {self.status} ไป {new_status} ไม่ได้")
        self.status = new_status

    def to_row(self):
        """แปลงเป็น list 1 แถวไว้เขียน CSV (เรียงตาม config.ENGAGEMENT_FIELDS)"""
        return [
            self.engagement_id,
            self.request_id,
            self.helper_id,
            self.status,
            self.result,
            self.revisions,
            self.updated_at,
        ]

    @staticmethod
    def from_row(row):
        """แปลง dict 1 แถวเป็น Engagement raise ValueError ถ้า revisions ไม่ใช่ตัวเลข หรือ status ไม่อยู่ใน config.ENGAGEMENT_STATUSES"""
        revisions = int(row["revisions"])

        if row["status"] not in config.ENGAGEMENT_STATUSES:
            raise ValueError(f"Invalid engagement status: {row['status']}")

        return Engagement(
            row["engagement_id"],
            row["request_id"],
            row["helper_id"],
            row["status"],
            row["result"],
            revisions,
            row["updated_at"],
        )


class Transaction:
    """รายการแต้มที่ขยับ 1 รายการ (transactions.csv) มีแต่เพิ่มต่อท้าย ห้ามแก้ของเดิม

    ดู: docs/02-design.md หัวข้อ Transaction
    """

    def __init__(
        self,
        txn_id,
        created_at,
        student_id,
        kind,
        d_available,
        d_held,
        request_id,
        note,
    ):
        """เก็บทุก parameter เป็น attribute ชื่อเดียวกัน (d_available, d_held เป็น int)"""
        self.txn_id = txn_id
        self.created_at = created_at
        self.student_id = student_id
        self.kind = kind
        self.d_available = d_available
        self.d_held = d_held
        self.request_id = request_id
        self.note = note

    def to_row(self):
        """แปลงเป็น list 1 แถวไว้เขียน CSV (เรียงตาม config.TRANSACTION_FIELDS)"""
        return [
            self.txn_id,
            self.created_at,
            self.student_id,
            self.kind,
            self.d_available,
            self.d_held,
            self.request_id,
            self.note,
        ]

    @staticmethod
    def from_row(row):
        """แปลง dict 1 แถวเป็น Transaction raise ValueError ถ้า d_available หรือ d_held ไม่ใช่ตัวเลข หรือ kind ไม่อยู่ใน config.TRANSACTION_KINDS"""
        d_available = int(row["d_available"])
        d_held = int(row["d_held"])

        if row["kind"] not in config.TRANSACTION_KINDS:
            raise ValueError(f"Invalid transaction kind: {row['kind']}")

        return Transaction(
            row["txn_id"],
            row["created_at"],
            row["student_id"],
            row["kind"],
            d_available,
            d_held,
            row["request_id"],
            row["note"],
        )
