import os

from chuaynoi.core import storage
from chuaynoi.reports import service
from chuaynoi.ui import display, inputs


def show_summary(summary):
    display.print_table(
        ["หัวข้อ", "ค่า"],
        [
            ["ผู้ใช้ทั้งหมด", summary["total_users"]],
            ["ประกาศทั้งหมด", summary["total_requests"]],
            ["แต้มที่โอนให้ผู้ช่วยแล้ว", summary["points_paid"]],
            ["แต้มต่อคนเฉลี่ยต่อประกาศ", summary["avg_reward"]],
        ],
    )

    category_rows = []
    for category in summary["by_category"]:
        category_rows.append([category, summary["by_category"][category]])
    display.print_table(["หมวด", "จำนวน"], category_rows)

    status_rows = []
    for status in summary["by_status"]:
        status_rows.append([status, summary["by_status"][status]])
    display.print_table(["status", "จำนวน"], status_rows)

    helper_rows = []
    for i in range(len(summary["top_helpers"])):
        name, points, jobs = summary["top_helpers"][i]
        helper_rows.append([i + 1, name, points, jobs])
    display.print_table(["อันดับ", "ชื่อ", "แต้ม", "งาน"], helper_rows)


def screen_reports(app):
    summary = service.summarize_board(app)
    display.print_header("สรุปสถิติ / ส่งออกรายงาน")
    show_summary(summary)

    if inputs.input_yes_no("ส่งออกเป็นไฟล์ .txt?"):
        path = service.export_summary_txt(summary)
        if path == "":
            print("[!] ส่งออกไม่สำเร็จ")
        else:
            print("[OK] ส่งออกรายงานแล้ว: " + path)
            storage.append_log(
                app.current_user_id, "EXPORT_REPORT " + os.path.basename(path)
            )

    input("กด Enter เพื่อกลับเมนูหลัก")
