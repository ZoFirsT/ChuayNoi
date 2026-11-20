from chuaynoi.core import storage
from chuaynoi.reports import service
from chuaynoi.ui import display, inputs


def show_summary(summary):
    display.print_table(
        ["รายการ", "ค่า"],
        [
            ["ผู้ใช้ทั้งหมด (คน)", summary["total_users"]],
            ["ประกาศทั้งหมด (รายการ)", summary["total_requests"]],
            ["แต้มที่โอนให้ผู้ช่วยแล้ว (แต้ม)", summary["points_paid"]],
            ["แต้มเฉลี่ยต่อคน (แต้ม)", summary["avg_reward"]],
        ],
    )

    print("\nจำนวนประกาศตามหมวด")
    category_rows = []
    for category in summary["by_category"]:
        category_rows.append([category, summary["by_category"][category]])
    display.print_table(["หมวด", "จำนวน"], category_rows)

    print("\nจำนวนประกาศตามสถานะ")
    status_rows = []
    for status in summary["by_status"]:
        status_rows.append([status, summary["by_status"][status]])
    display.print_table(["สถานะ", "จำนวน"], status_rows)

    print("\nอันดับผู้ช่วย")
    helper_rows = []
    for i in range(len(summary["top_helpers"])):
        name, points, jobs = summary["top_helpers"][i]
        helper_rows.append([i + 1, name, points, jobs])
    display.print_table(["อันดับ", "ชื่อ", "แต้มที่ได้", "งานที่ยืนยัน"], helper_rows)


def screen_reports(app):
    summary = service.summarize_board(app)
    display.print_header("สรุปสถิติของบอร์ด")
    show_summary(summary)

    if inputs.input_yes_no("ส่งออกเป็นไฟล์ .txt?"):
        path = service.export_summary_txt(summary)
        if path == "":
            print("[!] ส่งออกไม่สำเร็จ ตรวจสอบสิทธิ์เขียนไฟล์ในโฟลเดอร์ reports")
        else:
            print("[OK] ส่งออกรายงานแล้ว: " + path)
            storage.append_log(summary_user_id(app), "EXPORT_REPORT")

    input("กด Enter เพื่อกลับเมนูหลัก")


def summary_user_id(app):
    return app.current_user_id
