"""รับ input จาก user แล้วเช็กว่าถูกไหม (ชุด B)

ทุก function ถามวนซ้ำ (while loop) จนกว่าจะได้ค่าที่ถูก user พิมพ์ผิดแค่ไหนโปรแกรมก็ต้องไม่ error
ข้อความเตือนขึ้นต้นด้วย "[!] " ทุกครั้ง
รายละเอียดอยู่ใน docs/tasks/b-accounts-reports.md
"""


def input_int(prompt, min_value, max_value):
    """ถามตัวเลขจำนวนเต็มในช่วง min_value..max_value แล้ว return เป็น int"""
    raise NotImplementedError("TODO(ชุด B): input_int")


def input_text(prompt, min_len, max_len):
    """ถามข้อความ ตัด space หัวท้ายออก ความยาวต้องอยู่ในช่วง min_len..max_len แล้ว return เป็น str"""
    raise NotImplementedError("TODO(ชุด B): input_text")


def input_choice(prompt, options):
    """โชว์ options เป็นข้อ ๆ ให้พิมพ์เลขข้อ แล้ว return ตัวเลือกที่เลือก (str)"""
    raise NotImplementedError("TODO(ชุด B): input_choice")


def input_yes_no(prompt):
    """ถาม y/n แล้ว return True (y) หรือ False (n) เป็นฟังก์ชันช่วย ไม่นับใน 19 function หลัก"""
    raise NotImplementedError("TODO(ชุด B): input_yes_no")
