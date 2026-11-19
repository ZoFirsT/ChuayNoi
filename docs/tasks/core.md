# ชุดแกนกลาง: คลาสข้อมูล ไฟล์ แต้ม และเมนูหลัก

เจ้าของ repo ดูแลชุดแกนกลางด้วยไฟล์นี้ และ AI ที่ช่วยเป็นติวเตอร์ก็อ่านไฟล์นี้ ส่วนบนสุดเขียนให้ AI อ่าน ส่วนที่เหลือบอกว่าแกนกลางมีอะไรให้ชุดอื่น ทำงานยังไงข้างใน test case C1–C14 และของที่ต้องใส่ในรายงานกับคลิป ถ้าใช้ AI บนเว็บ ให้ copy ทั้งไฟล์นี้ไปวางเป็นข้อความแรกของแชทใหม่ แล้วพิมพ์ต่อว่าวันนี้อยากทำอะไร

## ถึง AI ที่อ่านไฟล์นี้

คนที่คุยกับคุณอยู่เป็นนักศึกษาที่เพิ่งเรียน programming เป็นเจ้าของ repo และทำชุดแกนกลางของโปรเจกต์ ChuayNoi นอกจาก code ของตัวเองแล้วยังดูแลทีมด้วย ช่วยเป็นติวเตอร์ให้ ใช้ไทยปน English แบบเพื่อนคุยกัน ตอบสั้น ทีละเรื่อง แล้วเช็กว่าเข้าใจก่อนไปต่อ ในไฟล์นี้ "คุณ" คือ AI และ "เพื่อน" คือเจ้าของ repo คนนั้น

<!-- mirror: AGENTS.md "คุณเป็นติวเตอร์ ไม่ใช่คนเขียนแทน" -->
โจทย์ให้ใช้ AI ได้ แต่ code ที่ส่งต้องอธิบายเองได้ทุกบรรทัด และอาจารย์จะถามจริง ทีมเลยตกลงกันว่า AI ช่วยได้แบบนี้

ทำได้

- อธิบาย concept กับ syntax ด้วยตัวอย่างสั้น ๆ ที่ไม่ใช่ function ในงาน
- แตก function เป็น step แล้วพาเขียนทีละ step ด้วยคำถามนำกับ hint
- review code ที่เพื่อนเขียนเอง ชี้ว่าผิด rule ข้อไหนหรือเสี่ยงพังตรงไหน
- อธิบาย error และสอนอ่าน Traceback
- ช่วยคิด test case และเช็กว่า test ครบตาม doc
- ช่วยวางโครงรายงาน ร่างเนื้อหาให้เพื่อนเอาไปแก้เป็นคำของตัวเอง และตรวจภาษา แล้วเตือนให้จดลง `docs/ai-log.md` ว่าส่วนไหน AI ร่าง

ห้ามทำ

- เขียน function หรือหน้าจอในงานให้ทั้งตัว หรือแก้ไฟล์แทนเพื่อน ถ้าโดนขอแบบนี้ ให้บอกดี ๆ ว่าจะพาทำทีละ step แทน
- แต่งผล test, output หรือภาพหน้าจอ ผล test ต้องมาจากการ run จริง
- เดา rule เอง rule ทุกข้ออยู่ใน `docs/` ถ้าหาไม่เจอให้บอกเพื่อนไปถามในกลุ่ม

ถ้าเพื่อนติดจริง ๆ หลังได้ hint ไปแล้ว 2 รอบ โชว์ได้ทีละบรรทัดพร้อมอธิบาย แล้วให้เพื่อนพิมพ์เองและอธิบายกลับมาว่าบรรทัดนั้นทำอะไร
<!-- /mirror -->

กติกาของ code ที่ผิดบ่อย

<!-- mirror: docs/02-design.md "กฎเหล็ก" -->
1. `service.py` กับ `search.py` ไม่มี `input()` และ `print()`
2. เช็กกฎให้ครบก่อน ผ่านแล้วค่อยแก้ data ผิดข้อไหน data ต้องเหมือนเดิม
3. ตัวเลขกับตัวเลือกเอามาจาก `config.py` ไม่พิมพ์ตัวเลขลอย ๆ
4. แต้มขยับผ่าน `add_transaction()` เท่านั้น แต้มรวม (ใช้ได้ + กันไว้) ของทุกคน = 100 × จำนวนผู้ใช้เสมอ
5. ห้ามเปลี่ยนชื่อหรือ parameter ของ function ที่มีอยู่ และไม่แก้ไฟล์ของชุดอื่น
6. เปิด CSV ทุกครั้งใส่ `newline=""` กับ `encoding=config.CSV_ENCODING`
7. ไม่เขียน `except:` เปล่า ๆ และไม่จับ `KeyboardInterrupt` (ให้ `app.run()` จัดการ)
<!-- /mirror -->

สัญญาที่แกนกลางให้ชุดอื่น และที่ชุดอื่นให้แกนกลาง อยู่ใน `docs/05-contracts.md` ไฟล์นี้ไม่ได้ copy มา ถ้าต้องดูข้ามชุด ขอให้เพื่อน paste `docs/05-contracts.md` ตามมา และ attribute ของ class กับข้อมูลตัวอย่างอยู่ใน `docs/02-design.md`

### หาว่าตอนนี้ทำถึงไหน

ชุดนี้ไม่ได้วัดความคืบหน้าด้วยการค้น `TODO` เริ่มคุยครั้งไหนก็หาก่อนว่าเพื่อนอยู่ช่วงไหน

1. ให้เพื่อนดู PR ที่ merge แล้วกับ PR ที่ยังรออยู่ใน GitHub และสถานะของ Issue #10–#13 (ถ้า run command เองได้ ใช้ `git log --oneline` ดู commit ล่าสุด) อย่าเดาจากความจำ
2. ถามวันที่วันนี้ ถ้ายังไม่รู้
3. ถามเรื่องทีม: เพื่อนสองคนเลือกชุดกันแล้วหรือยัง มี PR ของเพื่อนรอ review อยู่มั้ย
4. เทียบกับตารางงานข้างล่าง สรุปว่า "น่าจะอยู่ช่วง ... งานถัดไปคือ ..." แล้วถามว่าใช่มั้ย ถ้าช่วงไหนช้ากว่าแผน ให้บอกตรง ๆ แล้วช่วยเลือกว่าจะทำอะไรก่อน งานที่เพื่อนในทีมรออยู่มาก่อนเสมอ เช่น review PR

### งานที่เจ้าของ repo ทำซ้ำทุกสัปดาห์

นอกจาก code ของแกนกลาง เจ้าของ repo ทำเรื่องพวกนี้ ช่วยพาทำทีละเรื่องเหมือน function

- review PR ของเพื่อนทุกอัน ตาม checklist ข้างล่าง
- เช็กว่ารวมกันแล้วทำงานได้ ตามข้อ 8 ของ `docs/05-contracts.md` (run `python tools/reset_data.py` แล้ว `python main.py` ต้องไม่มี error ใหม่)
- ดูแล mirror ให้ตรงกัน ถ้าแก้ tutor block ใน `AGENTS.md`, "กฎเหล็ก" ใน `docs/02-design.md` หรือตารางงานใน `docs/03-workflow.md` ต้องแก้สำเนาในไฟล์ของแกนกลาง ชุด A และชุด B ใน PR เดียวกัน
- ตอบ Issue ที่เพื่อนเปิดมาขอเปลี่ยนสัญญา (ขั้นตอนอยู่ข้อ 9 ของ `docs/05-contracts.md`) แล้วแก้ไฟล์ต้นทางกับสำเนาทุกที่ใน PR เดียว
- กด Squash and merge เอง คนอื่นกดไม่ได้ และ repo ตั้งให้ merge ได้แบบนี้แบบเดียว

### checklist ตอน review PR ของเพื่อน

ช่วยเช็กตามนี้ แล้วให้เจ้าของ repo เป็นคนพิมพ์ comment และกดเอง

- แก้เฉพาะไฟล์ของชุดตัวเองมั้ย
- ชื่อ function กับ parameter ตรงกับ doc มั้ย
- `service.py` กับ `search.py` มี `input()` หรือ `print()` หลุดมามั้ย
- เช็ก rule ครบก่อนแก้ data มั้ย
- ใช้ค่าจาก `config` มั้ย ไม่มีตัวเลขลอย ๆ
- แต้มขยับผ่าน `add_transaction()` อย่างเดียวมั้ย
- มี `except:` เปล่า ๆ หรือจับ `KeyboardInterrupt` มั้ย
- PR บอกรหัส test case ที่ run ไปแล้ว และ run ซ้ำได้จริงบนเครื่องเจ้าของ repo มั้ย (สลับไป branch นั้นใน GitHub Desktop แล้ว run ดู)
- ให้เพื่อนอธิบาย code สักบรรทัดสองบรรทัดใน comment ถ้าอธิบายไม่ได้ ยังไม่ควร merge

## ชุดนี้ทำอะไร

ทุกอย่างที่ชุด A กับชุด B ยืนอยู่บนมัน ได้แก่ class ข้อมูล 5 ตัว (`User`, `HelpRequest`, `Engagement`, `Transaction`, `AppData`) การอ่านเขียน CSV ระบบแต้มน้ำใจ ตารางกับหัวจอ และเมนูหลักที่เรียกหน้าจอของทุกชุด มี function หลัก 7 ตัวกับ 5 class

## ตารางงาน

<!-- mirror: docs/03-workflow.md "แกนกลาง" -->
| สัปดาห์ | ภายใน | Issue | ทำอะไร |
| --- | --- | --- | --- |
| 1 | 23 พ.ย. 2569 | #10 | `core/models.py`, `core/storage.py`, `wallet/service.py`, `ui/display.py` |
| 2 | 30 พ.ย. 2569 | #11 | `app.py` (หน้าแรก เมนูหลัก Ctrl+C), `wallet/menu.py` และ review PR `ui/inputs.py` |
| 3 | 7 ธ.ค. 2569 | #12 | รวมทุกเมนูใน `app.py` ทดสอบทั้งโปรแกรม review PR |
| 4 | 14 ธ.ค. 2569 | #13 | test C1–C14 และรายงานส่วนแกนกลาง |
| 5 | 21 ธ.ค. 2569 | #9 | รวมรายงาน PDF แพ็ก ZIP คลิปส่วนของตัวเอง |
<!-- /mirror -->

## ไฟล์ที่ดูแล

| ไฟล์ | มีอะไร |
| --- | --- |
| `chuaynoi/core/models.py` | `User`, `HelpRequest`, `Engagement`, `Transaction` |
| `chuaynoi/core/storage.py` | `AppData`, `load_csv`, `save_csv`, `append_log`, `load_all`, `save_all` |
| `chuaynoi/wallet/service.py` | `add_transaction`, `get_balance`, `list_history` |
| `chuaynoi/wallet/menu.py` | `screen_wallet` |
| `chuaynoi/ui/display.py` | `display_width`, `print_table`, `print_header`, `print_menu` |
| `chuaynoi/app.py` | `run`, `start_screen`, `main_menu` |
| `chuaynoi/config.py` | ค่าคงที่ทุกตัว ทุกคนอ่านได้ ถ้าจะแก้ต้องเปิด Issue ก่อน |

## สิ่งที่แกนกลางให้คนอื่น

สัญญาเต็มอยู่ใน `docs/05-contracts.md` ข้อ 2 ตารางนี้บอกแค่ว่ามีอะไรให้เรียก

| มีอะไร | ไว้ทำอะไร |
| --- | --- |
| `User`, `HelpRequest`, `Engagement`, `Transaction` | object ของ data แต่ละแถวใน CSV |
| `app.find_user()`, `find_request()`, `find_engagement()`, `next_id()` | หา object และสร้างรหัสใหม่ |
| `load_all()`, `save_all(app)`, `append_log()` | โหลด บันทึก และเขียน log |
| `add_transaction()`, `get_balance()`, `list_history()` | ขยับแต้ม ดูยอด ดูประวัติ |
| `print_table()`, `print_header()`, `print_menu()` | แสดงผลบนจอ |

## รายละเอียด

### models.py

มี 4 class ตรงกับ 4 ไฟล์ CSV attribute ของแต่ละ class อยู่ใน `docs/02-design.md`

- `__init__` เก็บ parameter เป็น attribute ชื่อเดียวกัน
- `to_row()` คืน list เรียงตาม `config.*_FIELDS` ส่วน `skills` ของ `User` ต่อกันด้วย `config.SKILL_SEPARATOR`
- `from_row(row)` รับ dict จาก `csv.DictReader` แปลง `int()` ให้ column ที่เป็นตัวเลข ถ้าแปลงไม่ได้หรือค่าไม่อยู่ในรายการที่อนุญาต จะ raise `ValueError` ให้ `load_csv` ข้ามแถวนั้น
- `HelpRequest.total_cost()` คืน `reward × slots`
- `HelpRequest.count_used_slots(engagements)` นับ engagement ของประกาศนี้ที่ status อยู่ใน `ACTIVE_ENGAGEMENT_STATUSES` หรือเป็น `ENG_APPROVED`
- `Engagement.change_status(new_status)` เปลี่ยนได้เฉพาะเส้นทางใน `ALLOWED_TRANSITIONS` ถ้าไม่ได้ raise `ValueError("เปลี่ยน status จาก {เดิม} ไป {ใหม่} ไม่ได้")` และไม่แก้อะไร

### storage.py

| function | ทำอะไร |
| --- | --- |
| `AppData.next_id(prefix, existing_ids, digits)` | หาเลขมากสุดใน `existing_ids` บวก 1 แล้วเติม 0 ให้ครบ `digits` หลัก ถ้า list ว่างเริ่มที่ 1 |
| `load_csv(path, fields, from_row)` | สร้าง folder `data/` กับไฟล์ที่มีแค่ header ถ้ายังไม่มี แล้วคืน `([], 0)` ถ้ามีไฟล์ อ่านทีละแถว แถวที่ `from_row` raise `ValueError`, `KeyError`, `TypeError` หรือ `AttributeError` ถูกข้ามและนับ (แถวที่ column ไม่ครบ `DictReader` ใส่ `None` ให้ช่องที่ขาด จึงเกิดสองตัวหลัง) สุดท้ายคืน `(items, skipped)` |
| `save_csv(path, fields, items)` | เขียน header แล้วตามด้วย `item.to_row()` ทุกตัว ถ้าเจอ `OSError` คืน `False` |
| `append_log(student_id, action)` | ต่อท้าย `activity_log.txt` เป็น `[YYYY-MM-DD HH:MM] รหัส action` ถ้าเจอ `OSError` พิมพ์ `[!] ไม่สามารถเขียน log ได้: ...` แล้วทำต่อ |
| `load_all()` | โหลดทั้ง 4 ไฟล์เข้า `AppData` และรวมจำนวนแถวที่ข้ามไว้ใน `app.skipped_rows` |
| `save_all(app)` | เขียนทับ users, requests, engagements และคืน `True` ถ้าเขียนครบ ไม่แตะ transactions เพราะ `add_transaction` ต่อท้ายไฟล์ให้ทุกครั้งอยู่แล้ว |

action ที่ใช้ใน log: `REGISTER`, `LOGIN`, `CREATE_REQUEST`, `APPLY`, `SUBMIT`, `APPROVE`, `CLOSE`, `EXPORT_REPORT`

### wallet/service.py

- `add_transaction(app, student_id, kind, d_available, d_held, request_id="", note="")` ทำตามลำดับ
  1. เช็ก `kind` ถ้าไม่อยู่ใน `config.TRANSACTION_KINDS` raise `ValueError`
  2. ขอรหัสใหม่จาก `app.next_id("T", ..., 6)`
  3. สร้าง `Transaction`
  4. เขียน 1 แถวต่อท้าย `transactions.csv` (ถ้าไฟล์ว่าง เขียน header ก่อน)
  5. เขียนไฟล์สำเร็จแล้วค่อยเพิ่มเข้า `app.transactions` ถ้าเขียนไม่ได้ `OSError` หลุดออกไปตั้งแต่ข้อ 4 และ memory ไม่เปลี่ยน
  6. คืน `Transaction`
- `get_balance(app, student_id)` รวม `d_available` กับ `d_held` ของคนนี้ แล้วคืน `(available, held)`
- `list_history(app, student_id, limit=10)` คืนรายการของคนนี้ ใหม่สุดก่อน ไม่เกิน `limit`

### ui/display.py

- `display_width(text)` วนทีละตัวอักษร ถ้า `unicodedata.category(ch)` เป็น `Mn` นับ 0 ถ้า `unicodedata.east_asian_width(ch)` เป็น `W` หรือ `F` นับ 2 ที่เหลือนับ 1 สระบน/ล่างกับวรรณยุกต์ไม่กินที่บนจอ ตารางเลยตรงแม้มีภาษาไทย
- `print_table(headers, rows)` ความกว้าง column คือ `display_width` ที่มากสุดใน column นั้น ตัวเลขชิดขวา ไม่ตัดข้อความ ถ้า `rows` ว่างพิมพ์ `[i] ไม่มีข้อมูล`
- `print_header(title, subtitle="")` เส้น `=` กว้าง `config.SCREEN_WIDTH` แล้ว title และ subtitle (ถ้าไม่ว่าง)
- `print_menu(options, zero_label)` พิมพ์ `[1]` ถึง `[n]` ตาม `options` แล้ว `[0] {zero_label}` ปิดด้วยเส้น `-` ใช้กับเมนูทุกหน้า

### app.py

- `run()` เรียก `load_all()` ใน `try … except KeyboardInterrupt` ของตัวเอง กด Ctrl+C ตอนกำลังโหลด จะพิมพ์บรรทัดว่างแล้วออกเลยโดยไม่ save เพราะข้อมูลยังโหลดไม่ครบ ถ้า save จะเขียนทับไฟล์ด้วยข้อมูลที่ไม่ครบ โหลดเสร็จแล้วถ้ามีแถวที่ข้าม พิมพ์ `[i] ข้าม {N} แถวที่อ่านไม่ผ่าน` จากนั้นวน `start_screen` แล้ว `main_menu` จนกว่าจะเลือกออก ลูปนี้ครอบด้วย `try … except KeyboardInterrupt` กด Ctrl+C ที่ไหนข้างใน จะพิมพ์บรรทัดว่างแล้ว `save_all` ได้ผลแล้วพิมพ์ `[OK] บันทึกข้อมูลแล้ว` ไม่ได้ผลพิมพ์ `[!] บันทึกข้อมูลไม่สำเร็จ ถ้าเปิดไฟล์ใน Excel ค้างไว้ให้ปิดก่อน` เหมือนเลือก `[0] บันทึกและออก`
- `start_screen(app)` ใช้ `inputs.input_int` ให้เลือก เข้าสู่ระบบ สมัคร หรือออก แล้วเรียก `accounts_menu.screen_login` หรือ `screen_register` คืน `True` เมื่อ login สำเร็จ `False` เมื่อเลือกออก
- `main_menu(app)` โชว์ชื่อกับยอดแต้มล่าสุดทุกครั้งที่กลับจากหน้าจอ แล้วเรียกหน้าจอตามเลขที่เลือก (`board_menu.screen_board`, `screen_post`, `screen_my_requests`, `screen_my_jobs`, `wallet_menu.screen_wallet`, `reports_menu.screen_reports`) คืน `"exit"` หรือ `"logout"`

## test case

run `python tools/reset_data.py` ก่อนเริ่ม test

| TC | Test อะไร | ทำยังไง | Expected |
| --- | --- | --- | --- |
| C1 | ยอดแต้ม | `get_balance(app, "9990000001")` | `(55, 30)` |
| C2 | แต้มรวมทั้งระบบ | เอาแต้มใช้ได้ + กันไว้ ของทุกคนมารวมกัน | `400` (100 × 4 คน) |
| C3 | file หาย | ลบ `data/requests.csv` แล้ว run `load_all()` | ไม่ error และสร้าง file ใหม่ที่มีแค่หัวตาราง |
| C4 | folder หาย | ลบ folder `data/` แล้ว run โปรแกรม | สร้าง folder และ file ใหม่ |
| C5 | แถวเสีย | แก้ reward ของ R0003 เป็น `abc` | `skipped_rows == 1`, ประกาศเหลือ 2 |
| C6 | `,` และ `"` ในข้อความ | save หัวข้อ `ช่วยดู "โลโก้", สีฟ้า` แล้วโหลดใหม่ | ข้อความเหมือนเดิม |
| C7 | Excel | เปิด `data/requests.csv` ด้วย Excel | ภาษาไทยไม่เพี้ยน |
| C8 | แต้มบันทึกทันที | `add_transaction` แล้วปิดโปรแกรมแล้วเปิดใหม่ | รายการยังอยู่ท้าย file |
| C9 | ประเภทผิด | `add_transaction(..., kind="XYZ", ...)` | `ValueError` |
| C10 | ความกว้างภาษาไทย | `display_width("ที่ว่าง")`, `display_width("R0001")` | `4`, `5` |
| C11 | ตารางภาษาไทย | `print_table` กับหัวข้อที่มีสระบน/ล่าง | เส้นขอบตรงกันทุกแถว |
| C12 | status ผิดลำดับ | `Engagement` ที่ status เป็น ACCEPTED เรียก `change_status("APPROVED")` | `ValueError` |
| C13 | log | ทำรายการหนึ่งครั้ง | `activity_log.txt` มีบรรทัดใหม่ที่ format ถูก |
| C14 | Ctrl+C | กด Ctrl+C ตอนอยู่เมนูหลัก | save แล้วออก ไม่มี Traceback |

## รายงานและคลิป

- รายงานส่วนแกนกลางต้องมีบทการออกแบบ (กติกาแต้ม status ไฟล์ข้อมูล), flowchart ภาพรวมโปรแกรม, คำอธิบาย function ของตัวเอง, คู่มือเมนูหลักกับกระเป๋าแต้ม และผล C1–C14 ที่ run จริง
- เจ้าของ repo เป็นคนรวมรายงานทุกส่วนเป็น PDF ฉบับเดียว
- ในคลิปอธิบายโครงสร้างโปรแกรมกับระบบแต้ม แล้วเปิด code `get_balance` หรือ `add_transaction` อธิบาย
- รูปแบบรายงาน ชื่อไฟล์ และ checklist อยู่ใน `docs/04-submit.md` AI ช่วยวางโครง ร่างเนื้อหา และตรวจภาษาได้ แต่เจ้าของ repo ต้องอ่านแก้ให้เป็นคำของตัวเอง อธิบายได้ทุกย่อหน้า และจดลง `docs/ai-log.md` ว่าส่วนไหน AI ร่าง ภาพหน้าจอกับผล test ต้องมาจากของจริง

## ลิงก์

- สัญญาข้ามชุด: https://github.com/ZoFirsT/ChuayNoi/blob/main/docs/05-contracts.md
- design กับ class ทั้งหมด: https://github.com/ZoFirsT/ChuayNoi/blob/main/docs/02-design.md
- ทีมทำงานกันยังไง กับส่งขึ้น GitHub ทีละปุ่ม: https://github.com/ZoFirsT/ChuayNoi/blob/main/docs/03-workflow.md
- Issue แกนกลาง: https://github.com/ZoFirsT/ChuayNoi/issues/16
