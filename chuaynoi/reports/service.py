"""คำนวณสถิติแล้วเขียนรายงาน .txt ไฟล์นี้ห้ามมี input (ชุด B)

รายละเอียดอยู่ใน docs/tasks/b-accounts-reports.md
"""

import os
from datetime import datetime

from chuaynoi import config


def summarize_board(app):
    """คำนวณสถิติของทั้งบอร์ดแล้ว return เป็น dict (key ทั้งหมดดูใน docs/tasks/b-accounts-reports.md)"""
    raise NotImplementedError("TODO(ชุด B): summarize_board")


def export_summary_txt(summary, folder=config.REPORT_DIR):
    """เขียน summary ลงไฟล์ summary_YYYYMMDD_HHMM.txt ใน folder แล้ว return path (เขียนไม่ได้ return "" แทน)"""
    raise NotImplementedError("TODO(ชุด B): export_summary_txt")
