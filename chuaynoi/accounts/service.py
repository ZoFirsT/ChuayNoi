from datetime import datetime

from chuaynoi import config
from chuaynoi.core.models import User
from chuaynoi.wallet.service import add_transaction


def register_user(app, student_id, name, faculty, skills):
    if not student_id.isdigit() or not student_id.isascii() or len(student_id) != config.STUDENT_ID_LENGTH:
        return (
            False,
            f"รหัสนักศึกษาต้องเป็นตัวเลข {config.STUDENT_ID_LENGTH} หลัก",
        )

    if app.find_user(student_id) is not None:
        return (False, "มีผู้ใช้รหัสนี้แล้ว")

    if len(name) < config.NAME_MIN or len(name) > config.NAME_MAX:
        return (
            False,
            f"ชื่อต้องยาว {config.NAME_MIN} ถึง {config.NAME_MAX} ตัวอักษร",
        )

    if faculty not in config.FACULTIES:
        return (False, f"ไม่มีคณะ {faculty}")

    created_at = datetime.now().strftime(config.TIME_FORMAT)
    app.users.append(User(student_id, name, faculty, skills, created_at))
    add_transaction(
        app, student_id, config.TXN_SIGNUP, config.START_POINTS, 0, "", "แต้มเริ่มต้น"
    )
    return (True, f"สมัครสำเร็จ ได้รับ {config.START_POINTS} แต้ม")


def login_user(app, student_id):
    user = app.find_user(student_id)
    if user is None:
        return (False, "ไม่พบรหัสนักศึกษานี้ กรุณาสมัครก่อน")

    app.current_user_id = student_id
    return (True, f"สวัสดี {user.name}")
