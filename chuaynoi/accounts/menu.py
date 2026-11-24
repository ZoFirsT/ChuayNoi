from chuaynoi import config
from chuaynoi.accounts import service
from chuaynoi.core import storage
from chuaynoi.ui import display, inputs


def screen_register(app):
    while True:
        student_id = inputs.input_text(
            "รหัสนักศึกษา (0 = กลับ): ", 1, config.STUDENT_ID_LENGTH
        )
        if student_id == "0":
            return False

        name = inputs.input_text(
            f"ชื่อ-นามสกุล ({config.NAME_MIN}-{config.NAME_MAX} ตัวอักษร): ",
            config.NAME_MIN,
            config.NAME_MAX,
        )
        faculty = inputs.input_choice("เลือกคณะ", config.FACULTIES)
        skills_text = inputs.input_text(
            "ทักษะ คั่นด้วย , (เว้นว่างได้): ", 0, config.DETAIL_MAX
        )
        skills = split_skills(skills_text)

        success, message = service.register_user(app, student_id, name, faculty, skills)
        if success:
            if not storage.save_all(app):
                print("[!] บันทึกไฟล์ไม่สำเร็จ ถ้าเปิดไฟล์ใน Excel ค้างไว้ให้ปิดก่อน")
            service.login_user(app, student_id)
            storage.append_log(app.current_user_id, "REGISTER")
            print("[OK] " + message)
            return True

        print("[!] " + message)
        if not inputs.input_yes_no("ลองใหม่?"):
            return False


def screen_login(app):
    student_id = inputs.input_text(
        "รหัสนักศึกษา (0 = กลับ): ", 1, config.STUDENT_ID_LENGTH
    )
    if student_id == "0":
        return False

    success, message = service.login_user(app, student_id)
    if not success:
        print("[!] " + message)
        return False

    print("[OK] " + message)
    storage.append_log(student_id, "LOGIN")
    return True


def split_skills(text):
    skills = []
    for part in text.split(","):
        part = part.strip()
        if part != "":
            skills.append(part)
    return skills
