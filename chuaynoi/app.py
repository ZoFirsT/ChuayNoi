"""main menu ของโปรแกรม: โหลด data, ให้ login แล้วพาไปหน้าจอของแต่ละ feature (ชุดแกนกลาง)

รายละเอียดอยู่ใน docs/tasks/core.md
"""

from chuaynoi.accounts import menu as accounts_menu
from chuaynoi.board import menu as board_menu
from chuaynoi.core import storage
from chuaynoi.reports import menu as reports_menu
from chuaynoi.wallet import menu as wallet_menu

START_MENU = (
    "เข้าสู่ระบบด้วยรหัสนักศึกษา",
    "สมัครผู้ใช้ใหม่",
)

MAIN_MENU = (
    "ดูบอร์ดประกาศ / ค้นหา",
    "โพสต์ขอความช่วยเหลือ",
    "งานที่ฉันโพสต์ (ยืนยันงาน / ปิดรับ)",
    "งานที่ฉันรับช่วย (ส่งงาน)",
    "กระเป๋าแต้มและประวัติ",
    "สรุปสถิติ / ส่งออกรายงาน .txt",
    "สลับผู้ใช้",
)


def run():
    """จุดเริ่มของโปรแกรม โหลด data แล้วเข้าหน้าแรก ต่อด้วย main menu วนไปจนกว่า user จะเลือกออก

    ถ้ากด Ctrl+C ตอนไหนก็ตาม ต้อง save data แล้วออกแบบเนียน ๆ ห้ามมี Traceback โผล่
    """
    raise NotImplementedError("TODO(แกนกลาง): run")


def start_screen(app):
    """หน้าแรก: [1] เข้าสู่ระบบ [2] สมัคร [0] ออก

    return True ถ้า login ผ่าน, False ถ้า user เลือกออก
    """
    raise NotImplementedError("TODO(แกนกลาง): start_screen")


def main_menu(app):
    """main menu: เลือกเลขไหนก็เรียกหน้าจอของ feature นั้น

    return "logout" ถ้าเลือกสลับผู้ใช้ หรือ "exit" ถ้าเลือกออก
    """
    raise NotImplementedError("TODO(แกนกลาง): main_menu")
