"""รับ input จาก user แล้วเช็กว่าถูกต้อง (ชุด B)

ทุก function ถามวนซ้ำจนได้ค่าที่ถูก ข้อความเตือนขึ้นต้นด้วย "[!] "
IN1 ผู้เรียกใส่ช่วงที่รับได้ไว้ใน prompt เอง มีแค่ input_yes_no ที่เติม " (y/n): " ให้
IN2 พิมพ์อะไรมาก็ไม่ raise error ใช้ except ValueError: ครอบแค่ int(...)
IN3 ปล่อย KeyboardInterrupt (Ctrl+C) ผ่านไปถึง app.run() ห้ามมี except: เปล่า ๆ
    หรือ except Exception: ครอบ input()
IN4 EOFError (Ctrl+D, Ctrl+Z แล้ว Enter, input ที่ pipe เข้ามาจบ) อยู่นอกขอบเขต ไม่จับและไม่ทดสอบ
ดู: docs/05-contracts.md ข้อ 3
"""


def input_int(prompt, min_value, max_value):
    """ถามตัวเลขจำนวนเต็มในช่วงที่กำหนด วนถามจนกว่าจะได้ค่าที่ถูก

    รับ: prompt ข้อความถาม (ใส่ช่วงที่รับได้ไว้ในนี้เอง), min_value กับ max_value ขอบเขตที่รวมค่านั้นด้วย
    คืน: int ที่อยู่ในช่วง min_value ถึง max_value (ตัด space หัวท้ายก่อนแปลง)
        ถ้าพิมพ์ตัวอักษร ช่องว่าง ทศนิยม หรือเลขนอกช่วง ให้ถามใหม่
    แก้ data: ไม่แก้อะไร
    error: ไม่ raise อะไร ข้อความเตือนที่ต้องตรงตัว
        "[!] กรุณาพิมพ์ตัวเลข" เมื่อแปลงเป็น int ไม่ได้
        "[!] ต้องอยู่ระหว่าง {min_value} ถึง {max_value}" เมื่อเลขอยู่นอกช่วง
        KeyboardInterrupt ปล่อยผ่าน
    ดู: docs/05-contracts.md ข้อ 3
    """
    raise NotImplementedError("TODO(ชุด B): input_int")


def input_text(prompt, min_len, max_len):
    """ถามข้อความที่ยาวอยู่ในช่วงที่กำหนด วนถามจนกว่าจะได้ค่าที่ถูก

    รับ: prompt ข้อความถาม, min_len กับ max_len ความยาวต่ำสุดกับสูงสุดที่รวมค่านั้นด้วย
    คืน: str ที่ตัด space หัวท้ายแล้ว ความยาวนับด้วย len() ไม่ใช่ความกว้างบนจอ
    แก้ data: ไม่แก้อะไร
    error: ไม่ raise อะไร ข้อความเตือนที่ต้องตรงตัว
        "[!] ต้องยาว {min_len} ถึง {max_len} ตัวอักษร"
        "[!] ต้องไม่เกิน {max_len} ตัวอักษร" เมื่อ min_len เป็น 0
        KeyboardInterrupt ปล่อยผ่าน
    ดู: docs/05-contracts.md ข้อ 3
    """
    raise NotImplementedError("TODO(ชุด B): input_text")


def input_choice(prompt, options):
    """ให้เลือกจากรายการด้วยเลขข้อ

    รับ: prompt หัวข้อที่พิมพ์ก่อนรายการ, options tuple หรือ list ของ str (ไม่ถูกแก้)
    คืน: ตัวเลือกที่เลือก (ข้อความ ไม่ใช่เลขข้อ)
    แก้ data: ไม่แก้อะไร
    พิมพ์ prompt ตามด้วย "  [1] …" ถึง "  [n] …" แล้วถามเลขด้วย input_int("พิมพ์หมายเลข (1-{n}): ", 1, n)
    error: ข้อความเตือนมาจาก input_int KeyboardInterrupt ปล่อยผ่าน
    ดู: docs/05-contracts.md ข้อ 3
    """
    raise NotImplementedError("TODO(ชุด B): input_choice")


def input_yes_no(prompt):
    """ถามคำถามใช่/ไม่ใช่ วนถามจนกว่าจะได้ y หรือ n (function ช่วย ไม่นับใน 19 function หลัก)

    รับ: prompt คำถาม (ไม่ต้องใส่ "(y/n)" เพราะ function เติม " (y/n): " ให้)
    คืน: True ถ้าพิมพ์ y หรือ yes, False ถ้าพิมพ์ n หรือ no (ตัวพิมพ์เล็กหรือใหญ่ก็ได้)
    แก้ data: ไม่แก้อะไร
    error: ไม่ raise อะไร ข้อความเตือนที่ต้องตรงตัว "[!] กรุณาพิมพ์ y หรือ n" KeyboardInterrupt ปล่อยผ่าน
    ดู: docs/05-contracts.md ข้อ 3
    """
    raise NotImplementedError("TODO(ชุด B): input_yes_no")
