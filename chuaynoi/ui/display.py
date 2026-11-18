"""แสดงผลบนจอให้ดูเป็นระเบียบ ภาษาไทยก็ไม่เบี้ยว (ชุดแกนกลาง)

สระบน/ล่างกับวรรณยุกต์ไทยไม่กินที่บนจอ แต่ len() ดันนับเป็น 1
เวลาจัด column เลยต้องใช้ display_width() แทน len() ไม่งั้นตารางภาษาไทยจะเบี้ยว
รายละเอียดอยู่ใน docs/tasks/core.md
"""

import unicodedata

from chuaynoi import config


def display_width(text):
    """ความกว้างจริงของข้อความตอนขึ้นจอ เช่น display_width("ที่ว่าง") ต้องได้ 4 ไม่ใช่ 7"""
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
    """แปลงค่า 1 ช่องเป็นข้อความที่กว้างเท่า width ตัวเลขชิดขวา ที่เหลือชิดซ้าย"""
    text = str(value)
    spaces = " " * (width - display_width(text))
    if isinstance(value, (int, float)):
        return spaces + text
    return text + spaces


def format_line(values, widths):
    """ประกอบ 1 แถวของตาราง"""
    line = "|"
    for i in range(len(values)):
        line += " " + format_cell(values[i], widths[i]) + " |"
    return line


def print_table(headers, rows):
    """พิมพ์ตารางแบบมีเส้นขอบ column ต้องตรงกันแม้มีภาษาไทย ตัวเลขชิดขวา ถ้า rows ว่างให้พิมพ์ "[i] ไม่มีข้อมูล" แทน"""
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


def print_header(title, subtitle=""):
    """หัวของแต่ละหน้าจอ: เส้น "=" ยาว config.SCREEN_WIDTH ตามด้วยชื่อหน้ากับบรรทัดรอง (ฟังก์ชันช่วย)"""
    line = "=" * config.SCREEN_WIDTH
    print(line)
    print(" " + title)
    if subtitle != "":
        print(" " + subtitle)
    print(line)
