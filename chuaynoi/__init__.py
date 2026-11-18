"""ChuayNoi (ช่วยหน่อย) บอร์ดขอให้ช่วยงานสั้น ๆ ในหมู่นักศึกษา จ่ายกันด้วยแต้มน้ำใจ

โครง package คร่าว ๆ (ละเอียดกว่านี้อยู่ใน docs/02-design.md)
    app.py      main menu ที่ต่อทุก feature เข้าด้วยกัน
    config.py   ค่าคงที่กับ rule ทั้งหมด
    core/       data class กับการอ่าน/เขียนไฟล์ (ทุกชุดใช้)
    ui/         รับ input กับแสดงผลบนจอ (ทุกชุดใช้)
    accounts/   สมัคร / login
    wallet/     แต้มน้ำใจ
    board/      โพสต์ประกาศกับ flow การช่วยงาน
    reports/    สถิติกับ export รายงาน
"""
