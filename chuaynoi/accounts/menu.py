from chuaynoi import config
from chuaynoi.accounts import service
from chuaynoi.core import storage
from chuaynoi.ui import display, inputs

def screen_register(app):
    display.print_header("สมัครผู้ใช้ใหม่", "พิมพ์ข้อมูลตามที่ถาม สมัครแล้วได้แต้มเริ่มต้นทันที")

    while True:
        student_id = inputs.input_text(
            f"รหัสนักศึกษา ({config.STUDENT_ID_LENGTH} หลัก): ", 1, 30
        )
        name = inputs.input_text(
            f"ชื่อ ({config.NAME_MIN}-{config.NAME_MAX} ตัวอักษร): ",
            config.NAME_MIN,
            config.NAME_MAX,
        )
        faculty = inputs.input_choice("เลือกคณะ:", config.FACULTIES)
        skills_text = inputs.input_text(
            "ทักษะ คั่นด้วย , (เว้นว่างได้): ", 0, config.DETAIL_MAX
        )
        skills = split_skills(skills_text)

        success, message = service.register_user(app, student_id, name, faculty, skills)
        if success:
            print("[OK] " + message)
            service.login_user(app, student_id)
            storage.save_all(app)
            storage.append_log(student_id, "REGISTER")
            return True

        print("[!] " + message)
        if not inputs.input_yes_no("ลองสมัครใหม่อีกครั้ง?"):
            return False

def screen_login(app):
    display.print_header("เข้าสู่ระบบ")

    while True:
        student_id = inputs.input_text("รหัสนักศึกษา: ", 1, 30)
        success, message = service.login_user(app, student_id)
        if success:
            print("[OK] " + message)
            storage.append_log(student_id, "LOGIN")
            return True

        print("[!] " + message)
        if not inputs.input_yes_no("ลองใหม่อีกครั้ง?"):
            return False

def split_skills(text):
    skills = []
    for part in text.split(","):
        part = part.strip().replace(config.SKILL_SEPARATOR, " ")
        if part != "":
            skills.append(part)
    return skills
