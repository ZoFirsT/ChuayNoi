"""แสดงผลบนจอให้เป็นระเบียบ ภาษาไทยไม่เบี้ยว (แกนกลาง)

สระบนล่างกับวรรณยุกต์ไทยไม่กินที่บนจอ แต่ len() นับเป็น 1 ตัว
เลยจัด column ด้วย display_width() แทน len() ตารางถึงไม่เบี้ยว
ดู: docs/05-contracts.md ข้อ 2
"""

import os
import unicodedata

from chuaynoi import config


def display_width(text):
    """วัดความกว้างของข้อความตอนขึ้นจอ

    รับ: text ข้อความ
    คืน: int ตัวอักษรกลุ่ม Mn (สระบน/ล่าง วรรณยุกต์) นับ 0, ตัวกว้าง (East Asian W กับ F) นับ 2, ที่เหลือนับ 1
        เช่น display_width("ที่ว่าง") ได้ 4 ไม่ใช่ 7
    แก้ data: ไม่แก้อะไร
    ดู: docs/05-contracts.md ข้อ 2
    """
    width = 0
    for ch in text:
        if unicodedata.category(ch) == "Mn":
            continue
        if unicodedata.east_asian_width(ch) in ("F", "W"):
            width += 2
        else:
            width += 1

    return width


def format_cell(value, width):
    """จัดค่า 1 ช่องให้กว้างเท่า width ตัวเลข (int, float) ชิดขวา ที่เหลือชิดซ้าย (function ช่วย)"""
    text = str(value)
    spaces = " " * (width - display_width(text))
    if isinstance(value, (int, float)):
        return spaces + text
    return text + spaces


def format_line(values, widths):
    """ประกอบ 1 แถวของตารางจากค่าแต่ละช่องกับความกว้างของ column คั่นด้วย | (function ช่วย)"""
    line = "|"
    for i in range(len(values)):
        line += " " + format_cell(values[i], widths[i]) + " |"
    return line


def print_table(headers, rows):
    """พิมพ์ตารางแบบมีเส้นขอบ column ตรงกันแม้มีภาษาไทย

    รับ: headers list ชื่อ column, rows list ของแถว (แต่ละแถวเป็น list ที่ยาวเท่า headers)
    คืน: ไม่คืนค่า
    แก้ data: ไม่แก้อะไร
    ความกว้างของ column ปรับตามข้อความที่ยาวสุด ไม่ตัดข้อความ ตัวเลขชิดขวา
    ถ้า rows ว่าง พิมพ์ "[i] ไม่มีข้อมูล" แทนตาราง
    ดู: docs/05-contracts.md ข้อ 2
    """
    if len(rows) == 0:
        print("[i] ไม่มีข้อมูล")
        return

    widths = []
    for i in range(len(headers)):
        widest = display_width(str(headers[i]))
        for row in rows:
            cell_width = display_width(str(row[i]))
            if cell_width > widest:
                widest = cell_width
        widths.append(widest)

    border = "+"
    for width in widths:
        border += "-" * (width + 2) + "+"

    print(border)
    print(format_line(headers, widths))
    print(border)
    for row in rows:
        print(format_line(row, widths))
    print(border)


def clear_screen():
    """ล้างหน้าจอ (function ช่วย)"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def print_header(title, subtitle=""):
    """ล้างจอแล้วพิมพ์หัวหน้าจอ: เส้น "=" ยาว config.SCREEN_WIDTH, ชื่อหน้า, บรรทัดรอง (ถ้าไม่ว่าง), แล้วปิดด้วยเส้น "=" (function ช่วย)"""
    clear_screen()
    line = "=" * config.SCREEN_WIDTH
    print(line)
    print(" " + title)
    if subtitle != "":
        print(" " + subtitle)
    print(line)


def print_menu(options, zero_label):
    """พิมพ์ตัวเลือก [1] ถึง [n] ตามด้วย [0] กับเส้น "-" ยาว config.SCREEN_WIDTH (function ช่วย)

    ใช้ได้ทุกหน้าจอ เช่น print_menu(["ยืนยันงาน", "ปิดรับ"], "กลับ")
    """
    for i in range(len(options)):
        print(f" [{i + 1}] {options[i]}")
    print(f" [0] {zero_label}")
    print("-" * config.SCREEN_WIDTH)
