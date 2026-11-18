"""main menu ของโปรแกรม: โหลด data, ให้ login แล้วพาไปหน้าจอของแต่ละ feature (ชุดแกนกลาง)

รายละเอียดอยู่ใน docs/tasks/core.md
"""

from chuaynoi import config
from chuaynoi.accounts import menu as accounts_menu
from chuaynoi.board import menu as board_menu
from chuaynoi.core import storage
from chuaynoi.reports import menu as reports_menu
from chuaynoi.ui import display, inputs
from chuaynoi.wallet import menu as wallet_menu
from chuaynoi.wallet import service as wallet_service

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
    app = storage.load_all()
    if app.skipped_rows > 0:
        print(f"[i] ข้าม {app.skipped_rows} แถวที่อ่านไม่ผ่าน")

    try:
        while True:
            if not start_screen(app):
                break
            result = main_menu(app)
            if result == "exit":
                break
            app.current_user_id = ""
    except KeyboardInterrupt:
        print()

    if storage.save_all(app):
        print("[OK] บันทึกข้อมูลแล้ว")
    else:
        print("[!] บันทึกข้อมูลไม่สำเร็จ ถ้าเปิดไฟล์ใน Excel ค้างไว้ให้ปิดก่อน")


def print_menu(options, zero_label):
    """พิมพ์ตัวเลือกเป็นข้อ ๆ [1] ถึง [n] ปิดท้ายด้วย [0] กับเส้นคั่น"""
    
    for i in range(len(options)):
        print(f" [{i + 1}] {options[i]}")
    print(f" [0] {zero_label}")
    print("-" * config.SCREEN_WIDTH)


def start_screen(app):
    """หน้าแรก: [1] เข้าสู่ระบบ [2] สมัคร [0] ออก

    return True ถ้า login ผ่าน, False ถ้า user เลือกออก
    """
    while True:
        display.print_header(
            "ChuayNoi | หน้าแรก", "ช่วยหน่อย: บอร์ดขอความช่วยเหลือ จ่ายกันด้วยแต้มน้ำใจ"
        )
        print_menu(START_MENU, "ออกจากโปรแกรม")
        choice = inputs.input_int(
            f"เลือกเมนู (0-{len(START_MENU)}): ", 0, len(START_MENU)
        )

        if choice == 0:
            return False
        if choice == 1:
            logged_in = accounts_menu.screen_login(app)
        else:
            logged_in = accounts_menu.screen_register(app)

        if logged_in:
            return True


def main_menu(app):
    """main menu: เลือกเลขไหนก็เรียกหน้าจอของ feature นั้น
    return "logout" ถ้าเลือกสลับผู้ใช้ หรือ "exit" ถ้าเลือกออก
    """
    while True:
        user = app.find_user(app.current_user_id)
        available, held = wallet_service.get_balance(app, user.student_id)
        display.print_header(
            f"ChuayNoi | เมนูหลัก    ผู้ใช้: {user.name} ({user.student_id})",
            f"ใช้ได้ {available} | กันไว้ {held}",
        )
        print_menu(MAIN_MENU, "บันทึกและออก")
        choice = inputs.input_int(f"เลือกเมนู (0-{len(MAIN_MENU)}): ", 0, len(MAIN_MENU))

        if choice == 0:
            return "exit"
        if choice == 1:
            board_menu.screen_board(app)
        elif choice == 2:
            board_menu.screen_post(app)
        elif choice == 3:
            board_menu.screen_my_requests(app)
        elif choice == 4:
            board_menu.screen_my_jobs(app)
        elif choice == 5:
            wallet_menu.screen_wallet(app)
        elif choice == 6:
            reports_menu.screen_reports(app)
        else:
            return "logout"
