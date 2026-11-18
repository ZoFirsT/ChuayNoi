"""หน้าสรุปสถิติกับ export รายงาน (ชุด B)

ผลขึ้นต้นด้วย "[OK] " ถ้าสำเร็จ หรือ "[!] " ถ้าไม่สำเร็จ ตารางตัวเลขทั้งหมดมาจาก summarize_board()
ดู: docs/05-contracts.md ข้อ 4
"""

from chuaynoi.core import storage
from chuaynoi.reports import service
from chuaynoi.ui import display, inputs


def screen_reports(app):
    """เมนู 6 โชว์สถิติเป็นตาราง แล้วถามว่าจะส่งออกเป็น .txt ไหม

    ถาม: ยืนยัน y/n ว่าจะส่งออก (ตอบ n รอ Enter แล้วกลับ ไม่มีข้อความ)
    คืน: None
    แก้ data: ไม่ save ส่งออกสำเร็จ log "EXPORT_REPORT {file name}" ส่งออกไม่ได้แสดง [!] และไม่เขียน log
    ดู: docs/05-contracts.md ข้อ 4
    """
    raise NotImplementedError("TODO(ชุด B): screen_reports")
