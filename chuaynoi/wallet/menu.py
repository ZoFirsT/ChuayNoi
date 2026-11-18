"""หน้ากระเป๋าแต้ม (ชุดแกนกลาง)"""

from chuaynoi.ui import display
from chuaynoi.wallet import service


def screen_wallet(app):
    """โชว์ยอดใช้ได้ ยอดที่กันไว้ กับประวัติ 10 รายการล่าสุดเป็นตาราง"""
    student_id = app.current_user_id
    user = app.find_user(student_id)
    available, held = service.get_balance(app, student_id)

    display.print_header(
        f"กระเป๋าแต้มของ {user.name} ({user.student_id})", f"ใช้ได้ {available} | กันไว้ {held}"
    )

    rows = []
    for txn in service.list_history(app, student_id):
        rows.append([txn.created_at, txn.kind, txn.d_available, txn.d_held, txn.note])
    display.print_table(["เวลา", "ประเภท", "ใช้ได้", "กันไว้", "หมายเหตุ"], rows)

    input("กด Enter เพื่อกลับเมนูหลัก")
