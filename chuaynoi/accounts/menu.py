"""หน้าจอสมัครและ login (ชุด B)

ทุกหน้าจอถามด้วย ui.inputs แล้วเรียก service ผลขึ้นต้นด้วย "[OK] " ถ้าสำเร็จ หรือ "[!] " ถ้าไม่สำเร็จ
สมัครสำเร็จต้อง storage.save_all(app) แล้ว storage.append_log(...) ส่วน login เขียน log อย่างเดียว
สองหน้านี้ไม่พิมพ์ header ไม่รอ Enter และกลับด้วย 0 ที่ช่องรหัสนักศึกษา
หน้าจอไม่เช็กกฎเอง ให้ service ตัดสิน
ดู: docs/05-contracts.md ข้อ 4
"""

from chuaynoi import config
from chuaynoi.accounts import service
from chuaynoi.core import storage
from chuaynoi.ui import display, inputs


def screen_register(app):
    """หน้าสมัครผู้ใช้ใหม่ (หน้าแรก [2])

    ถาม: รหัสนักศึกษา (0 = กลับ), ชื่อ-นามสกุล, คณะ (เลือกจาก config.FACULTIES), ทักษะ (คั่นด้วย , เว้นว่างได้)
    คืน: True เมื่อสมัครสำเร็จและ login แล้ว, False เมื่อผู้ใช้เลือกกลับ
    แก้ data: สมัครสำเร็จ save_all(app) แล้ว log "REGISTER" (ไม่มี LOGIN)
        ถ้า register_user ไม่ผ่าน แสดงเหตุผลแล้วถามว่าจะลองใหม่ไหม
    ดู: docs/05-contracts.md ข้อ 4
    """
    raise NotImplementedError("TODO(ชุด B): screen_register")


def screen_login(app):
    """หน้า login ด้วยรหัสนักศึกษา (หน้าแรก [1])

    ถาม: รหัสนักศึกษา (0 = กลับ) ลองครั้งเดียว ไม่ผ่านก็แสดงเหตุผลแล้วคืน False
    คืน: True เมื่อ login สำเร็จ, False เมื่อไม่ผ่านหรือเลือกกลับ
    แก้ data: ไม่ save เขียน log "LOGIN" เมื่อสำเร็จ
    ดู: docs/05-contracts.md ข้อ 4
    """
    raise NotImplementedError("TODO(ชุด B): screen_login")
