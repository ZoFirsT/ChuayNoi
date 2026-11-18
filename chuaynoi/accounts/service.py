"""rule ของการสมัครและ login (ชุด B)

ทุก function เช็กกฎให้ครบก่อน ผิดข้อไหน return (False, เหตุผล) และ app ต้องเหมือนเดิม
ผ่านหมดค่อยแก้ data แล้ว return (True, ข้อความ) ไฟล์นี้ไม่มี input() กับ print()
ข้อความที่ return ไม่ใส่ "[OK] " หรือ "[!] " หน้าจอเป็นคนเติม แต้มขยับผ่าน add_transaction() เท่านั้น
ดู: docs/tasks/b-accounts-reports.md หัวข้อ register_user และ login_user
"""

from datetime import datetime

from chuaynoi import config
from chuaynoi.core.models import User
from chuaynoi.wallet.service import add_transaction


def register_user(app, student_id, name, faculty, skills):
    """สมัครผู้ใช้ใหม่ แล้วให้แต้มเริ่มต้น

    รับ: student_id รหัสนักศึกษา, name ชื่อ-นามสกุล, faculty คณะ, skills list ของ str (เก็บตามที่ส่งมา หน้าจอแยกและตัด space ให้ก่อนเรียก)
    คืน: (True, ข้อความสำเร็จ) หรือ (False, เหตุผล)
    กฎ: RG1–RG4 ตามลำดับ (รหัสนักศึกษา, รหัสซ้ำ, ความยาวชื่อ, คณะใน config.FACULTIES)
    แก้ data: เพิ่ม User ท้าย app.users กับรายการ SIGNUP ของผู้ใช้ใหม่ (ใช้ได้ +config.START_POINTS)
        ไม่ login ให้ (ไม่ตั้ง app.current_user_id)
    ดู: docs/tasks/b-accounts-reports.md หัวข้อ register_user
    """
    raise NotImplementedError("TODO(ชุด B): register_user")


def login_user(app, student_id):
    """ตั้งผู้ใช้ที่ login อยู่ตามรหัสนักศึกษา (function ช่วย)

    รับ: student_id รหัสนักศึกษา
    คืน: (True, ข้อความทักทาย) ถ้าเจอผู้ใช้ หรือ (False, เหตุผล) ถ้าไม่เจอ
    แก้ data: ถ้าเจอ ตั้ง app.current_user_id เป็น student_id ถ้าไม่เจอไม่แก้อะไร
    ดู: docs/tasks/b-accounts-reports.md หัวข้อ login_user
    """
    raise NotImplementedError("TODO(ชุด B): login_user")
