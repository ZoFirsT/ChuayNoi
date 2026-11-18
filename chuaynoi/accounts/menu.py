"""หน้าจอสมัครกับ login (ชุด B)

ทุกหน้าจอทำเหมือนกัน: ถามด้วย ui.inputs แล้วเรียก service จากนั้นโชว์ [OK] หรือ [!]
ถ้าสำเร็จให้ storage.save_all(app) กับ storage.append_log(...) ด้วย
"""

from chuaynoi import config
from chuaynoi.accounts import service
from chuaynoi.core import storage
from chuaynoi.ui import display, inputs


def screen_register(app):
    """ถามรหัสนักศึกษา ชื่อ คณะ ทักษะ แล้วสมัครให้ return True ถ้าสมัครเสร็จและ login แล้ว"""
    raise NotImplementedError("TODO(ชุด B): screen_register")


def screen_login(app):
    """ถามรหัสนักศึกษาแล้ว login ให้ return True ถ้าผ่าน"""
    raise NotImplementedError("TODO(ชุด B): screen_login")
