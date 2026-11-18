"""หน้ากระเป๋าแต้ม (แกนกลาง)

โชว์ยอดกับประวัติของผู้ใช้ที่ login อยู่ แล้วรอ Enter ก่อนกลับเมนูหลัก
ดู: docs/05-contracts.md ข้อ 4
"""

from chuaynoi.ui import display
from chuaynoi.wallet import service


def screen_wallet(app):
    """โชว์ยอดใช้ได้ ยอดกันไว้ และประวัติแต้มล่าสุด 10 รายการเป็นตาราง

    คืน: None
    แก้ data: ไม่แก้อะไร ไม่ save ไม่เขียน log
    ดู: docs/05-contracts.md ข้อ 4
    """
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
