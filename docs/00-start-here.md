# เริ่มตรงนี้ก่อน

เพิ่งเข้าทีมมาใช่มั้ย อ่านหน้านี้หน้าเดียวก่อนก็พอ จบแล้วจะรู้ว่าต้องทำอะไรต่อ ส่วนที่เหลือตามลิงก์ไปอ่านทีหลังได้

## โปรเจกต์นี้คืออะไร

ChuayNoi (ช่วยหน่อย) เป็น Python console app ของวิชา CS102 เป็นบอร์ดให้เพื่อนโพสต์ขอให้ช่วยงานสั้น ๆ แล้วจ่ายกันด้วยแต้มน้ำใจ เขียนด้วย Python ล้วน ไม่ต้องลง library เพิ่ม

อยากเห็นภาพรวมเต็ม ๆ อ่าน [01-overview.md](01-overview.md)

## งานแบ่งยังไง

มี 3 ชุด แกนกลางเจ้าของ repo ทำเอง อีก 2 ชุดให้เลือกคนละชุด

| ชุด | ทำอะไร | ขนาดงาน |
| --- | --- | --- |
| แกนกลาง | class, อ่าน/เขียนไฟล์, ระบบแต้ม, เมนูหลัก | 7 function + 5 class |
| ชุด A บอร์ดประกาศ | โพสต์ ค้นหา รับช่วย ส่งผลงาน ยืนยันงาน ปิดรับ | 6 function + 4 หน้าจอ |
| ชุด B ผู้ใช้ การรับข้อมูล และรายงาน | รับ input สมัคร/login สถิติ export รายงาน | 6 function + 3 หน้าจอ |

ได้ชุดไหนไปก็รับผิดชอบชุดนั้นทั้งหมด ทั้ง code, test, ส่วนของตัวเองในรายงาน และคลิป เทียบสองชุดแบบละเอียดดูใน [tasks/README.md](tasks/README.md)

## ทำตอนนี้เลย

1. ส่ง username GitHub มาในกลุ่ม เจ้าของ repo จะเชิญเข้า repo แล้วอย่าลืมกด Accept ในอีเมล
2. ลง Python 3.10 ขึ้นไป, VS Code และ GitHub Desktop ใครใช้ Windows ตอนลง Python ติ๊ก **Add python.exe to PATH**
3. clone repo ผ่าน GitHub Desktop แล้วเปิด Terminal ใน VS Code รันสองคำสั่งนี้

   ```bash
   python tools/reset_data.py
   ```

   ```bash
   python main.py
   ```

   ใครใช้ macOS พิมพ์ `python3` แทน ถ้าเห็นหน้าแรก แล้วขึ้น `NotImplementedError` ที่มีคำว่า `TODO(ชุด …)` ถือว่าปกติ แปลว่ายังมี function ที่ไม่มีใครเขียน ขั้นตอนละเอียดอยู่ใน [03-workflow.md](03-workflow.md)
4. อ่าน [tasks/README.md](tasks/README.md) แล้วเลือกชุด A หรือชุด B
5. ไปแท็บ Issues เปิด [#14 ชุด A](https://github.com/ZoFirsT/ChuayNoi/issues/14) หรือ [#15 ชุด B](https://github.com/ZoFirsT/ChuayNoi/issues/15) กด Assignees เลือก assign yourself แล้ว comment ว่า "เลือกชุดนี้"

ถ้าสองคนอยากได้ชุดเดียวกัน คุยกันในกลุ่มแล้วตัดสินให้จบภายใน 20 พ.ย. 2569

## อ่านอะไรตามบทบาท

| ตอนนี้ทำอะไร | อ่านตามลำดับนี้ |
| --- | --- |
| เพิ่งเข้าทีม | [01-overview.md](01-overview.md), [tasks/README.md](tasks/README.md), ไฟล์ของชุดตัวเองใน `docs/tasks/` |
| กำลังเขียน function หรือหน้าจอ | ไฟล์ของชุดตัวเองใน `docs/tasks/`, [05-contracts.md](05-contracts.md), [02-design.md](02-design.md), [03-workflow.md](03-workflow.md) |
| จะ review PR (เจ้าของ repo) | [05-contracts.md](05-contracts.md) ข้อ 8, [tasks/core.md](tasks/core.md) |

## ทำงานร่วมกันยังไง

- push เข้า `main` ตรง ๆ ไม่ได้ ทำใน branch ของตัวเองแล้วเปิด PR
- ทำทีละ function หรือทีละหน้าจอ เสร็จชิ้นไหนเปิด PR ชิ้นนั้น
- คนที่ review และ merge มีแค่เจ้าของ repo ถ้าโดนขอให้แก้ ก็แก้ใน branch เดิมแล้ว push อีกรอบ
- ชื่อ branch กับประเภท commit อยู่ใน [03-workflow.md](03-workflow.md)
- ก่อน test ทุกรอบ run `python tools/reset_data.py` ผลจะได้ตรงกับ test case ใน doc

## ใช้ AI ช่วยยังไง

ใช้ได้ แต่ต้องอธิบาย code ของตัวเองได้ทุกบรรทัด (อาจารย์ถามแน่) และจดลง [ai-log.md](ai-log.md) ทุกครั้งที่ใช้ AI ในทีมนี้เป็นติวเตอร์ ไม่เขียน function ให้

- AI ใน editor (Copilot, Cursor และตัวอื่น ๆ) อ่าน [AGENTS.md](../AGENTS.md) ที่ root เองอยู่แล้ว ถ้าตัวไหนไม่อ่านเอง พิมพ์บอกว่า "อ่าน AGENTS.md กับ docs/tasks/a-board.md ก่อน" (เปลี่ยนเป็นไฟล์ของชุดตัวเอง)
- ChatGPT หรือ Gemini บนเว็บอ่านไฟล์ใน repo ไม่ได้ เปิดไฟล์ของชุดตัวเองใน `docs/tasks/` บน GitHub กด Copy raw file แล้ววางทั้งไฟล์เป็นข้อความแรกของแชท ถ้า AI ขอดูสัญญาข้ามชุด ให้วาง `docs/05-contracts.md` ตามไปด้วย
- เปิดแชทใหม่แล้ววางไฟล์ใหม่ทุกครั้งที่เริ่มงานชิ้นใหม่ AI จะได้ไม่สับสนกับเรื่องเก่า

ประโยคเริ่มคุยที่ใช้บ่อย

- "ช่วยดูหน่อยว่าตอนนี้ถึงไหนแล้ว ต้องทำอะไรต่อ"
- "พาเขียน `input_int` ทีละ step หน่อย"
- "review code นี้ให้หน่อย ผิด rule ตรงไหนมั้ย" แล้ววาง code ตามไป
- "error นี้แปลว่าอะไร" แล้ววาง Traceback ทั้งก้อน
- "ช่วยเช็กว่า test case ที่ run มาครบตาม doc ยัง" แล้ววางผลที่ run จริง

## ติดตรงไหน

ถามในกลุ่ม หรือเปิด Issue แบบ "ถามคำถาม" ถ้าเจอ bug ใช้แบบ "แจ้งบั๊ก"
