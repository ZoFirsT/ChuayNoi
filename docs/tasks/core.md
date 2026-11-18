# ชุดแกนกลาง: คลาสข้อมูล ไฟล์ แต้ม และเมนูหลัก

> คนทำ: เรา (เจ้าของ repo), ความยาก ★★★, function หลัก 7 ตัว + 5 class + เมนูหลัก
> models, storage, wallet/service ต้องเสร็จก่อนคนอื่น ภายใน **22 พ.ย. 2569**

## File ที่เราดูแล

| File | ต้องเขียนอะไร |
| --- | --- |
| `chuaynoi/core/models.py` | `User`, `HelpRequest`, `Engagement`, `Transaction` (`__init__`, `to_row`, `from_row` กับ method เฉพาะของแต่ละตัว) |
| `chuaynoi/core/storage.py` | `AppData`, `load_csv`, `save_csv`, `append_log`, `load_all`, `save_all` |
| `chuaynoi/wallet/service.py` | `add_transaction`, `get_balance`, `list_history` |
| `chuaynoi/wallet/menu.py` | `screen_wallet` |
| `chuaynoi/ui/display.py` | `display_width`, `print_table`, `print_header`, `print_menu` |
| `chuaynoi/app.py` | `run`, `start_screen`, `main_menu` |
| `chuaynoi/config.py` | ดูแลค่าคงที่ (ทุกคนอ่านได้ แต่ถ้าจะแก้ต้องบอกทีมก่อน) |

## Plan รายสัปดาห์

- [ ] สัปดาห์ 1: `models.py` ครบ 4 class, `storage.py`, `wallet/service.py`, `display.py` แล้วเปิด PR "แกนกลางพร้อม" และเชิญเพื่อน ๆ เข้ามาเป็น collaborator
- [ ] สัปดาห์ 2: `app.py` (หน้าเริ่มต้น เมนูหลัก Ctrl+C) กับ `wallet/menu.py` และรีบ review PR `ui/inputs.py` ของชุด B
- [ ] สัปดาห์ 3: รวมทุกเมนูเข้า `app.py` แล้ว test ทั้งโปรแกรม review PR ของเพื่อน ถ้ามีเวลาเหลือค่อยทำ feature Could
- [ ] สัปดาห์ 4: test case C1–C14 และรายงานส่วนของตัวเอง
- [ ] สัปดาห์ 5: สร้าง PDF รายงาน แพ็ก ZIP และคลิปส่วนของตัวเอง

## รายละเอียด

### class ใน `models.py`

- `__init__` เก็บ parameter เป็น attribute ตามตารางใน [02-design.md](../02-design.md#4-คลาสและ-attribute)
- `to_row()` return list เรียงตาม `config.*_FIELDS` (`skills` ให้ join ด้วย `config.SKILL_SEPARATOR`)
- `from_row(row)` รับ dict จาก `csv.DictReader` แล้วแปลง `int()` ให้คอลัมน์ที่เป็นตัวเลข ถ้าแปลงไม่ได้ หรือค่าไม่อยู่ในรายการที่อนุญาต ให้ปล่อย `ValueError` ออกมา
- `HelpRequest.count_used_slots(engagements)` นับ engagement ของประกาศนี้ที่ status อยู่ใน `ACTIVE_ENGAGEMENT_STATUSES` หรือเป็น `ENG_APPROVED`
- `Engagement.change_status(new_status)` ถ้า `new_status` ไม่อยู่ใน `ALLOWED_TRANSITIONS[self.status]` ให้ `raise ValueError("เปลี่ยนจาก ... เป็น ... ไม่ได้")`

### `storage.py`

| Function | ทำอะไร |
| --- | --- |
| `AppData.next_id(prefix, existing_ids, digits)` | หาเลขที่มากที่สุดใน `existing_ids` แล้วบวก 1 เติม 0 ข้างหน้าให้ครบ `digits` หลัก ถ้า list ว่างให้เริ่มที่ 1 |
| `load_csv(path, fields, from_row)` | เรียก `os.makedirs(DATA_DIR, exist_ok=True)` ก่อน ถ้าไม่มี file ให้สร้าง file ที่มีแค่หัวตารางแล้ว return `([], 0)` แถวไหนที่ `from_row` ปล่อย `ValueError`/`KeyError` ให้ข้ามแล้วนับไว้ สุดท้าย return `(items, skipped)` |
| `save_csv(path, fields, items)` | เขียนหัวตารางแล้วตามด้วย `item.to_row()` ทุกตัวด้วย `csv.writer` ถ้าเจอ `PermissionError`/`OSError` ให้จับไว้แล้ว return `False` |
| `append_log(student_id, action)` | เขียน `[YYYY-MM-DD HH:MM] รหัส การกระทำ` ต่อท้าย `activity_log.txt` ถ้าเจอ `OSError` ให้จับไว้แล้วพิมพ์เตือน |
| `load_all()` / `save_all(app)` | เรียก `load_csv` / `save_csv` กับ users, requests, engagements (transactions โหลดอย่างเดียว) |

action ที่ใช้ใน log: `REGISTER`, `LOGIN`, `CREATE_REQUEST`, `APPLY`, `SUBMIT`, `APPROVE`, `CLOSE`, `EXPORT_REPORT`

### `wallet/service.py`

- `add_transaction(...)` ทำตามลำดับนี้
  1. เช็ก `kind`
  2. เรียก `app.next_id("T", [t.txn_id for t in app.transactions], 6)` เอา id ใหม่
  3. สร้าง `Transaction` แล้วเพิ่มเข้า `app.transactions`
  4. เปิด file โหมด `"a"` แล้วเขียน 1 แถว (ถ้า file ว่างอยู่ให้เขียนหัวตารางก่อน)
  5. return `Transaction`
- `get_balance(app, student_id)` วนดู `app.transactions` แล้วรวม `d_available` กับ `d_held` ของคนนี้ return `(available, held)`
- `list_history(app, student_id, limit)` รายการของคนนี้ เอาอันล่าสุดขึ้นก่อน

### `ui/display.py`

- `display_width(text)`: วนทีละตัวอักษร ถ้า `unicodedata.category(ch) == "Mn"` นับเป็น 0, ถ้า `unicodedata.east_asian_width(ch) in ("W", "F")` นับเป็น 2 ที่เหลือนับ 1
- `print_table(headers, rows)`: ความกว้างคอลัมน์คือ `display_width` ที่มากที่สุดในคอลัมน์นั้น เติมช่องว่างเท่ากับความกว้างคอลัมน์ − `display_width(ค่า)` ส่วนตัวเลขให้ชิดขวา
- `print_header(title, subtitle)`: เส้น `=` กว้างเท่า `config.SCREEN_WIDTH`
- `print_menu(options, zero_label)`: พิมพ์ `[1]` ถึง `[n]` ตาม `options` ปิดด้วย `[0] zero_label` แล้วตามด้วยเส้น `-` ใช้ทั้งเมนูหลักและเมนูย่อยของทุกชุด

### `app.py`

- `run()`: เรียก `load_all()` ก่อน ถ้า `app.skipped_rows > 0` ให้เตือน จากนั้นวน `start_screen` แล้วต่อด้วย `main_menu` จนกว่าจะเลือกออก ทั้งหมดนี้ครอบด้วย `try / except KeyboardInterrupt` ให้ `save_all` แล้วพิมพ์ "บันทึกข้อมูลแล้ว ลาก่อน"
- `start_screen(app)`: ใช้ `inputs.input_int` ให้เลือก แล้วเรียก `accounts_menu.screen_login` / `screen_register`
- `main_menu(app)`: หัวจอโชว์ชื่อกับยอดแต้ม แล้วเรียกหน้าจอตามเมนูที่เลือก (`board_menu.screen_board`, `screen_post`, `screen_my_requests`, `screen_my_jobs`, `wallet_menu.screen_wallet`, `reports_menu.screen_reports`)

## Test case

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

- รายงานต้องมีบทการออกแบบ (กติกาแต้ม สถานะ ไฟล์ข้อมูล), Flowchart ภาพรวมโปรแกรม, คำอธิบาย function ของตัวเอง, คู่มือเมนูหลักและกระเป๋าแต้ม, ผล C1–C14 แล้วสร้าง PDF ด้วย `build_pdf.py`
- คลิปอธิบายโครงสร้างโปรแกรมกับระบบแต้ม แล้วเปิดโค้ด `get_balance` หรือ `add_transaction` ให้ดู
