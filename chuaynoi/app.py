"""เมนูหลัก ของโปรแกรม โหลด data ให้ login แล้วพาไปหน้าจอของแต่ละ feature (แกนกลาง)

ไฟล์นี้เป็นที่เดียวที่จับ KeyboardInterrupt (Ctrl+C) ที่อื่นต้องปล่อยให้ผ่านมาถึงที่นี่
ดู: docs/05-contracts.md ข้อ 4 และข้อ 7
"""

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
    """เปิดโปรแกรม โหลด data แล้ววนหน้าแรกกับ เมนูหลัก จนกว่าผู้ใช้จะเลือกออก

    คืน: ไม่คืนค่า
    แก้ data: ตอนจบ (เลือกออก หรือกด Ctrl+C) เรียก storage.save_all(app)
        สำเร็จ print "[OK] บันทึกข้อมูลแล้ว" ไม่สำเร็จ print "[!] บันทึกข้อมูลไม่สำเร็จ ถ้าเปิดไฟล์ใน Excel ค้างไว้ให้ปิดก่อน"
        ถ้า load ข้ามแถวไป print "[i] ข้าม {n} แถวที่อ่านไม่ผ่าน" ก่อนเข้าหน้าแรก
        เมื่อ main_menu คืน "logout" เคลียร์ app.current_user_id เป็น "" แล้วกลับหน้าแรก
    error: Ctrl+C ที่ไหนก็ได้ในหน้าแรกหรือ เมนูหลัก ถูกจับที่นี่ (print บรรทัดว่าง แล้ว save เหมือนออกปกติ ไม่มี Traceback)
        ไม่ครอบคลุม Ctrl+C ตอน load_all() กับ EOFError
    ดู: docs/05-contracts.md ข้อ 7
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


def start_screen(app):
    """แสดงหน้าแรก ให้เลือกเข้าสู่ระบบ [1] สมัคร [2] หรือออก [0] วนจนกว่าจะ login หรือเลือกออก

    คืน: True เมื่อ login สำเร็จ (รวมสมัครแล้ว login), False เมื่อ user เลือกออก
    แก้ data: ไม่แก้เอง screen_login กับ screen_register เป็นคนตั้ง app.current_user_id
    ดู: docs/05-contracts.md ข้อ 4
    """
    while True:
        display.print_header(
            "ChuayNoi | หน้าแรก", "ช่วยหน่อย: บอร์ดขอความช่วยเหลือ จ่ายกันด้วยแต้มน้ำใจ"
        )
        display.print_menu(START_MENU, "ออกจากโปรแกรม")
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
    """แสดง เมนูหลัก พร้อมชื่อกับยอดแต้มล่าสุด แล้วเรียกหน้าจอตามเลขที่เลือก

    คืน: "exit" เมื่อเลือกบันทึกและออก, "logout" เมื่อเลือกสลับผู้ใช้
    แก้ data: ไม่แก้เอง หลังกลับจากทุกหน้าจอ พิมพ์ชื่อกับยอดใหม่ที่อ่านจาก app ตอนนั้น
    ดู: docs/05-contracts.md ข้อ 4
    """
    while True:
        user = app.find_user(app.current_user_id)
        available, held = wallet_service.get_balance(app, user.student_id)
        display.print_header(
            f"ChuayNoi | เมนูหลัก    ผู้ใช้: {user.name} ({user.student_id})",
            f"ใช้ได้ {available} | กันไว้ {held}",
        )
        display.print_menu(MAIN_MENU, "บันทึกและออก")
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
