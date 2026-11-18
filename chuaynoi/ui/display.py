"""แสดงผลบนจอให้ดูเป็นระเบียบ ภาษาไทยก็ไม่เบี้ยว (ชุดแกนกลาง)

สระบน/ล่างกับวรรณยุกต์ไทยไม่กินที่บนจอ แต่ len() ดันนับเป็น 1
เวลาจัด column เลยต้องใช้ display_width() แทน len() ไม่งั้นตารางภาษาไทยจะเบี้ยว
รายละเอียดอยู่ใน docs/tasks/core.md
"""

import unicodedata

from chuaynoi import config


def display_width(text):
    """ความกว้างจริงของข้อความตอนขึ้นจอ เช่น display_width("ที่ว่าง") ต้องได้ 4 ไม่ใช่ 7"""
    raise NotImplementedError("TODO(แกนกลาง): display_width")


def print_table(headers, rows):
    """พิมพ์ตารางแบบมีเส้นขอบ column ต้องตรงกันแม้มีภาษาไทย ตัวเลขชิดขวา ถ้า rows ว่างให้พิมพ์ "[i] ไม่มีข้อมูล" แทน"""
    raise NotImplementedError("TODO(แกนกลาง): print_table")


def print_header(title, subtitle=""):
    """หัวของแต่ละหน้าจอ: เส้น "=" ยาว config.SCREEN_WIDTH ตามด้วยชื่อหน้ากับบรรทัดรอง (ฟังก์ชันช่วย)"""
    raise NotImplementedError("TODO(แกนกลาง): print_header")
