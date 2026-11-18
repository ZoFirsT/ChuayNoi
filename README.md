# ChuayNoi (ช่วยหน่อย)

บอร์ดให้นักศึกษาโพสต์ขอให้เพื่อนช่วยงานสั้น ๆ มีระบบ **แต้มน้ำใจ** ตอนโพสต์ระบบกันแต้มไว้ก่อน แล้วจ่ายตอนงานผ่าน
เป็น Python console app ทำส่งโปรเจกต์วิชา CS102 Fundamental of Computer Programming เทอม 1/2569

หน้านี้สำหรับคนที่เพิ่งเปิด repo อ่านก่อน แล้วไปต่อที่ `docs/00-start-here.md`

## วิธีรัน

ใช้ Python 3.10 ขึ้นไป ไม่ต้องลง library เพิ่ม

```bash
python tools/reset_data.py
```

```bash
python main.py
```

คำสั่งแรกสร้าง folder `data/` จาก sample data รันตอนใช้ครั้งแรก และทุกครั้งที่อยากเริ่ม test ใหม่ ใครใช้ macOS พิมพ์ `python3` แทน

## เอกสาร

| ไฟล์ | อ่านตอนไหน |
| --- | --- |
| [docs/00-start-here.md](docs/00-start-here.md) | เพิ่งเข้าทีม อ่านอันนี้ก่อน |
| [docs/01-overview.md](docs/01-overview.md) | อยากรู้ว่าโปรแกรมทำอะไร กติกาแต้ม และคำศัพท์ |
| [docs/02-design.md](docs/02-design.md) | ก่อนเริ่มเขียน code: โครงสร้าง class ไฟล์ data ข้อมูลตัวอย่าง |
| [docs/03-workflow.md](docs/03-workflow.md) | ตั้งค่าเครื่อง push ขึ้น GitHub ทีละปุ่ม ตารางงานรายสัปดาห์ |
| [docs/04-submit.md](docs/04-submit.md) | ส่งโปรเจกต์: ZIP รายงาน PDF และคลิป |
| [docs/05-contracts.md](docs/05-contracts.md) | สิ่งที่แต่ละชุดสัญญากันไว้ เช่น หน้าจอ log การขยับแต้ม |
| [docs/tasks/](docs/tasks/README.md) | เลือกชุดงาน และดูงานของชุดตัวเอง |
| [docs/ai-log.md](docs/ai-log.md) | จดทุกครั้งที่ใช้ AI |
| [AGENTS.md](AGENTS.md) | ให้ AI ใน editor อ่านก่อนช่วยงาน |

## ทีม

| ชุดงาน | ทำอะไรบ้าง |
| --- | --- |
| แกนกลาง | class ข้อมูล, ไฟล์, ระบบแต้ม, ตาราง, เมนูหลัก |
| ชุด A: บอร์ดประกาศ | โพสต์, ค้นหา, รับช่วย, ส่งผลงาน, ยืนยัน, ปิดรับ |
| ชุด B: ผู้ใช้ การรับข้อมูล และรายงาน | รับ input จากผู้ใช้, สมัคร/login, สถิติ, export รายงาน |
