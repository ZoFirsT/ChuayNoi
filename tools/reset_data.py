"""reset data กลับเป็น sample data (เป็น tool ของทีม ไม่ได้เป็นส่วนของโปรแกรมที่ส่ง)

วิธีใช้ (run จาก root ของ repo):
    python tools/reset_data.py

copy ทุกไฟล์ใน sample_data/ ไปทับใน data/ ให้ run ก่อนเริ่ม test ทุกรอบ ผลจะได้เทียบกันได้
folder data/ ไม่ขึ้น Git อยู่แล้ว data ที่แต่ละคน test เลยไม่ชนกัน
"""

import os
import shutil
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAMPLE_DIR = os.path.join(BASE_DIR, "sample_data")
DATA_DIR = os.path.join(BASE_DIR, "data")


def reset_data():
    """copy sample data ไปไว้ที่ data/ แล้ว return (จำนวนไฟล์ที่ copy ได้, จำนวนที่ copy ไม่ได้)"""
    if not os.path.isdir(SAMPLE_DIR):
        print("[!] ไม่พบโฟลเดอร์ sample_data/")
        return 0, 0
    os.makedirs(DATA_DIR, exist_ok=True)
    copied = 0
    failed = 0
    for name in sorted(os.listdir(SAMPLE_DIR)):
        source = os.path.join(SAMPLE_DIR, name)
        if not os.path.isfile(source):
            continue
        try:
            shutil.copyfile(source, os.path.join(DATA_DIR, name))
        except OSError as error:
            # เจอบ่อยตอนเปิดไฟล์ค้างไว้ใน Excel บน Windows มันจะเขียนทับไม่ได้
            print("[!] คัดลอก " + name + " ไม่ได้: " + str(error.strerror or error))
            failed += 1
            continue
        print("[OK] " + name)
        copied += 1
    return copied, failed


if __name__ == "__main__":
    copied, failed = reset_data()
    if failed:
        print("[!] มี " + str(failed) + " ไฟล์ที่คัดลอกไม่ได้ ถ้าเปิดไฟล์ใน data/ ค้างไว้ (เช่นใน Excel) ให้ปิดก่อนแล้วรันใหม่")
        sys.exit(1)
    if copied == 0:
        print("[!] ไม่มีไฟล์ถูกคัดลอก")
        sys.exit(1)
    print("รีเซ็ตข้อมูลแล้ว " + str(copied) + " ไฟล์")
