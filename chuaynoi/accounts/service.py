"""rule ของการสมัครผู้ใช้ ไฟล์นี้ห้ามมี input/print (ชุด B)

รายละเอียดอยู่ใน docs/tasks/b-accounts-reports.md
"""

from datetime import datetime

from chuaynoi import config
from chuaynoi.core.models import User
from chuaynoi.wallet.service import add_transaction


def register_user(app, student_id, name, faculty, skills):
    """สมัครผู้ใช้ใหม่แล้วให้แต้มเริ่มต้น return (success, message)

    ไม่ให้สมัครถ้ารหัสนักศึกษาไม่ใช่ตัวเลข 10 หลัก, มีคนใช้รหัสนี้แล้ว หรือคณะไม่อยู่ใน config.FACULTIES
    """
    raise NotImplementedError("TODO(ชุด B): register_user")


def login_user(app, student_id):
    """ถ้าเจอผู้ใช้ก็ตั้ง app.current_user_id ให้ แล้ว return (success, message) (ฟังก์ชันช่วย)"""
    raise NotImplementedError("TODO(ชุด B): login_user")
