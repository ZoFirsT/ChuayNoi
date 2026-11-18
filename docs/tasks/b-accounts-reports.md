# ชุด B: ผู้ใช้, การรับ input และรายงาน

> ความยาก ★★ (function หลัก 6 ตัว + หน้าจอ 3 หน้า) ชุดนี้ **เริ่มได้เลย ไม่ต้องรอใคร**
> เลือกชุดนี้ก็ไปเปิด Issue ที่ติดป้าย `pkg: B-accounts-reports` แล้ว assign ตัวเอง

## ชุดนี้ทำอะไร

1. รับ input จากผู้ใช้แบบที่พิมพ์ผิดแล้วโปรแกรมไม่พัง (หน้าจอของทุกคนใช้ function ชุดนี้หมด)
2. สมัครและเข้าสู่ระบบด้วยรหัสนักศึกษา
3. สรุปสถิติของบอร์ด แล้ว export ออกมาเป็น file `.txt`

## File ที่ต้องดูแล

| File | ต้องเขียนอะไรบ้าง |
| --- | --- |
| `chuaynoi/ui/inputs.py` | `input_int`, `input_text`, `input_choice`, `input_yes_no` |
| `chuaynoi/accounts/service.py` | `register_user`, `login_user` |
| `chuaynoi/accounts/menu.py` | `screen_register`, `screen_login` |
| `chuaynoi/reports/service.py` | `summarize_board`, `export_summary_txt` |
| `chuaynoi/reports/menu.py` | `screen_reports` |

## ของคนอื่นที่ต้องเรียกใช้

| ใช้อะไร | มาจากไหน | เอาไปทำอะไร |
| --- | --- | --- |
| `User` | แกนกลาง `core/models.py` | สร้างผู้ใช้ใหม่ |
| `app.find_user()` | แกนกลาง `core/storage.py` | เช็กรหัสซ้ำ และใช้ตอนเข้าสู่ระบบ |
| `add_transaction()` | แกนกลาง `wallet/service.py` | ให้ 100 แต้มตอนสมัคร |
| `print_table()`, `print_header()`, `print_menu()` | แกนกลาง `ui/display.py` | โชว์สถิติเป็นตาราง หัวจอ และเมนู `[1] ... [0] กลับ` |

ส่วน `ui/inputs.py` ไม่ต้องพึ่งของใครเลย เลยเริ่มเขียนและ test ได้ตั้งแต่วันแรก

## แผนแต่ละสัปดาห์

- [ ] สัปดาห์ 1: ลงเครื่องมือ เลือกชุด อ่าน [01](../01-overview.md) กับ [02](../02-design.md) แล้วเขียน `ui/inputs.py` ให้ครบทั้ง 4 function
- [ ] **ภายใน 26 พ.ย.**: PR `ui/inputs.py` ต้อง merge เรียบร้อยแล้ว เพราะทุกหน้าจอรอตัวนี้อยู่
- [ ] สัปดาห์ 2: `register_user`, `login_user`, `screen_register`, `screen_login`
- [ ] สัปดาห์ 3: `summarize_board`, `export_summary_txt`, `screen_reports`
- [ ] สัปดาห์ 4: ทำ test case B1–B13 และเขียนรายงานส่วนของตัวเอง
- [ ] สัปดาห์ 5: ทำคลิปส่วนของตัวเอง

## Function ใน `ui/inputs.py`

ทุก function ในนี้ใช้ `while True:` ถามวนไปเรื่อย ๆ จนกว่าจะได้ค่าที่ถูก แล้วค่อย `return`

### 1. `input_int(prompt, min_value, max_value)`

1. `text = input(prompt).strip()`
2. แปลงเป็นตัวเลขแบบนี้

   ```python
   try:
       number = int(text)
   except ValueError:
       print("[!] กรุณาพิมพ์ตัวเลข")
       continue
   ```

3. ถ้า `number < min_value` หรือ `number > max_value` ให้พิมพ์ `[!] ต้องอยู่ระหว่าง 5 ถึง 100` แล้ว `continue`
4. ผ่านแล้วก็ `return number`

ใช้เรื่อง: `while`, `try / except ValueError`, `int()`, `continue`, `or`

### 2. `input_text(prompt, min_len, max_len)`

1. `text = input(prompt).strip()`
2. ถ้า `len(text)` น้อยกว่า `min_len` หรือมากกว่า `max_len` ให้พิมพ์ `[!] ต้องยาว 5 ถึง 60 ตัวอักษร` แล้วถามใหม่ (กรณี `min_len` เป็น 0 ให้ใช้ข้อความ `[!] ต้องไม่เกิน 300 ตัวอักษร` แทน)
3. `return text`

### 3. `input_choice(prompt, options)`

1. print `prompt` ออกมาก่อน
2. วน print ตัวเลือกทีละตัวพร้อมเลขข้อ

   ```python
   for number in range(1, len(options) + 1):
       print("  [" + str(number) + "] " + options[number - 1])
   ```

3. รับเลขด้วย `choice = input_int("พิมพ์หมายเลข (1-" + str(len(options)) + "): ", 1, len(options))`
4. `return options[choice - 1]` ตรงนี้ return เป็น **ข้อความ** ที่เลือก ไม่ใช่ตัวเลขนะ

### 4. `input_yes_no(prompt)`

1. `answer = input(prompt + " (y/n): ").strip().lower()`
2. ถ้าได้ `"y"` หรือ `"yes"` ให้ return `True` ถ้าได้ `"n"` หรือ `"no"` ให้ return `False`
3. ถ้าเป็นอย่างอื่น ให้พิมพ์ `[!] กรุณาพิมพ์ y หรือ n` แล้วถามใหม่

### ลอง run ดูได้เลย

```bash
python -c "from chuaynoi.ui.inputs import input_int; print(input_int('เลข (1-5): ', 1, 5))"
```

## Function ใน `accounts/service.py`

### 5. `register_user(app, student_id, name, faculty, skills)`

1. ถ้า `student_id.isdigit()` เป็น `False` หรือ `len(student_id) != config.STUDENT_ID_LENGTH` ให้ `return (False, "รหัสนักศึกษาต้องเป็นตัวเลข 10 หลัก")`
2. ถ้า `app.find_user(student_id)` ไม่ใช่ `None` ตอบ "มีผู้ใช้รหัสนี้แล้ว"
3. ถ้าความยาวชื่อไม่อยู่ในช่วง `config.NAME_MIN` ถึง `config.NAME_MAX` หรือ `faculty not in config.FACULTIES` ให้ปฏิเสธแล้วบอกเหตุผลด้วย
4. สร้าง `User(student_id, name, faculty, skills, เวลาปัจจุบัน)` แล้ว `app.users.append(...)`
5. ให้แต้มเริ่มต้นด้วย `add_transaction(app, student_id, config.TXN_SIGNUP, config.START_POINTS, 0, "", "แต้มเริ่มต้น")`
6. `return (True, "สมัครสำเร็จ ได้รับ 100 แต้ม")`

`skills` เป็น list ของ str เช่น `["Python", "ตรวจภาษา"]` จะว่างก็ได้ ตอนหน้าจอถาม ให้ผู้ใช้พิมพ์มาเป็นข้อความเดียวคั่นด้วย `,` แล้วเราค่อยใช้ `.split(",")` แยก

### `login_user(app, student_id)` (function ช่วย)

ถ้าเจอผู้ใช้ ให้ตั้ง `app.current_user_id = student_id` แล้ว return `(True, "สวัสดี มะลิ ใจดี")` ถ้าไม่เจอ return `(False, "ไม่พบรหัสนักศึกษานี้ กรุณาสมัครก่อน")`

## Function ใน `reports/service.py`

### 6. `summarize_board(app)`

return เป็น dict ที่มี key ตามนี้

| Key | Type | คิดยังไง |
| --- | --- | --- |
| `total_users` | int | `len(app.users)` |
| `total_requests` | int | `len(app.requests)` |
| `by_category` | dict | ตั้งทุกหมวดใน `config.CATEGORIES` เป็น 0 ก่อน แล้ววนประกาศ `+1` ตามหมวด |
| `by_status` | dict | ทำแบบเดียวกัน แต่ใช้ `config.REQUEST_STATUSES` |
| `points_paid` | int | ผลรวม `d_available` ของรายการที่ `kind == config.TXN_EARN` |
| `avg_reward` | float | ผลรวม `reward` ÷ จำนวนประกาศ ปัด 2 ตำแหน่งด้วย `round()` (ถ้าไม่มีประกาศเลยให้เป็น 0) |
| `top_helpers` | list ของ tuple | `(ชื่อ, แต้มที่ได้, จำนวนงานที่ยืนยันแล้ว)` เอาแค่ 3 อันดับแรก เรียงตามแต้มจากมากไปน้อย |

`top_helpers` ทำแบบนี้

1. สร้าง dict `points = {}` แล้ววนรายการ `TXN_EARN` บวกแต้มเข้า `points[student_id]`
2. สร้าง dict `jobs = {}` แล้ววน engagement ที่สถานะเป็น `config.ENG_APPROVED` นับเข้า `jobs[helper_id]`
3. วน `points` เพื่อสร้าง list ของ `(ชื่อ, แต้ม, จำนวนงาน)` ส่วนชื่อหาได้จาก `app.find_user(...)`
4. เรียงด้วย `sorted(..., key=..., reverse=True)` แล้วตัดเอาแค่ `[:3]`

ใช้เรื่อง: dict สำหรับนับจำนวน, loop `for`, `if`, การหาร, `round()`, tuple, `sorted()`

### 7. `export_summary_txt(summary, folder)`

1. สร้าง folder ก่อนด้วย `os.makedirs(folder, exist_ok=True)`
2. ตั้งชื่อ file เป็น `"summary_" + datetime.now().strftime("%Y%m%d_%H%M") + ".txt"` แล้วต่อ path ด้วย `os.path.join`
3. เปิด file โหมด `"w"` ใส่ `encoding=config.TEXT_ENCODING` แล้วเขียนทีละบรรทัด
4. ครอบด้วย `try / except OSError:` ถ้าเขียนไม่ได้ให้ `return ""`
5. สุดท้าย `return path` ของ file ที่สร้าง

หน้าตา file ที่ได้จะประมาณนี้

```text
รายงานสรุป ChuayNoi
สร้างเมื่อ 2026-12-01 14:30
========================================
ผู้ใช้ทั้งหมด            4 คน
ประกาศทั้งหมด           3 รายการ
แต้มที่โอนให้ผู้ช่วยแล้ว   15 แต้ม
แต้มเฉลี่ยต่อคน          13.33 แต้ม

จำนวนประกาศตามหมวด
  ทดสอบเว็บ/แอป            1
  ตรวจสไลด์/เอกสาร         1
  ...

อันดับผู้ช่วย
  1. ต้นกล้า รักเรียน   15 แต้ม   1 งาน
```

## หน้าจอ

ทุกหน้าจอใช้ flow เดียวกัน

1. รับ input ด้วย `inputs`
2. เรียก service
3. พิมพ์ `[OK]` หรือ `[!]`
4. ถ้าสำเร็จ เรียก `storage.save_all(app)` และ `storage.append_log(...)` (action ที่ใช้คือ `REGISTER`, `LOGIN`, `EXPORT_REPORT`)

| หน้าจอ | ทำอะไร |
| --- | --- |
| `screen_register` | ถามรหัสนักศึกษา ชื่อ ให้เลือกคณะ แล้วถามทักษะ จากนั้นเรียก `register_user` ถ้าสมัครสำเร็จก็เข้าสู่ระบบให้เลยแล้ว return `True` |
| `screen_login` | ถามรหัสนักศึกษา แล้วเรียก `login_user` ถ้าสำเร็จ return `True` |
| `screen_reports` | เรียก `summarize_board` แล้วโชว์ผลเป็นตาราง ถามด้วย `input_yes_no("ส่งออกเป็นไฟล์ .txt?")` ถ้าตอบ y ก็เรียก `export_summary_txt` แล้วบอก path ของ file ที่ได้ |

## Test case

ก่อนเริ่ม test ให้รัน `python tools/reset_data.py` หนึ่งรอบ

| TC | ทดสอบอะไร | ทำยังไง | ผลที่ต้องได้ |
| --- | --- | --- | --- |
| B1 | พิมพ์ตัวอักษร | `input_int(..., 0, 7)` พิมพ์ `abc` | `[!] กรุณาพิมพ์ตัวเลข` แล้วถามใหม่ |
| B2 | นอกช่วง | `input_int(..., 0, 7)` พิมพ์ `9` | `[!] ต้องอยู่ระหว่าง 0 ถึง 7` |
| B3 | ค่าขอบ | `input_int(..., 5, 100)` พิมพ์ `4`, `101`, `5` และ `100` | ปฏิเสธ 4 และ 101, รับ 5 และ 100 |
| B4 | ว่าง | `input_int` กด Enter เฉย ๆ | ถามใหม่ ไม่ error |
| B5 | ข้อความสั้น/ว่าง | `input_text(..., 5, 60)` พิมพ์ `""`, `ช่วย` แล้ว `  ช่วยดูสไลด์  ` | ถามใหม่สองครั้ง แล้วคืน `ช่วยดูสไลด์` |
| B6 | เลือกตัวเลือก | `input_choice(..., config.CATEGORIES)` พิมพ์ `0`, `7`, `x` แล้ว `2` | ถามใหม่สามครั้ง แล้วคืน `ตรวจสไลด์/เอกสาร` |
| B7 | y/n | `input_yes_no` พิมพ์ `Y`, `n`, `maybe` | `True`, `False`, ถามใหม่ |
| B8 | รหัสผิดรูปแบบ | สมัครด้วย `12345` และ `99900000ab` | ปฏิเสธทั้งสองค่า |
| B9 | รหัสซ้ำ | สมัครด้วย `9990000001` | ปฏิเสธ "มีผู้ใช้รหัสนี้แล้ว" |
| B10 | สมัครสำเร็จ | สมัคร `9990000005` คณะบริหารธุรกิจ | ยอด `(100, 0)` และมีแถว SIGNUP ใหม่ใน `transactions.csv` |
| B11 | สถิติ | `summarize_board` กับข้อมูลตัวอย่าง (รีเซ็ตก่อน) | ผู้ใช้ 4, ประกาศ 3, หมวดละ 1 ใน 3 หมวด, OPEN 3, `points_paid` 15, `avg_reward` 13.33, อันดับ 1 คือต้นกล้า 15 แต้ม 1 งาน |
| B12 | ส่งออก | เมนู 6 เลือกส่งออก | มีไฟล์ใหม่ใน `reports/` ตัวเลขตรงกับ B11 |
| B13 | หน้าจอสมัคร | พิมพ์ผิดทุกช่องก่อน แล้วค่อยแก้จนสมัครสำเร็จ | ไม่มี error ตลอดทาง |

## รายงานและคลิป

- ในรายงานต้องมีคำอธิบาย function ทั้ง 6 ตัว, คู่มือหน้าจอสมัคร เข้าสู่ระบบ และสถิติ พร้อมภาพหน้าจอจริง, ตารางการจัดการ input ผิด (พิมพ์อะไรไปแล้วโปรแกรมตอบอะไรกลับมา) และผล B1–B13
- ในคลิปให้ demo ว่าพิมพ์ผิดหลายแบบแล้วโปรแกรมก็ไม่พัง สมัครผู้ใช้ใหม่ให้ดู เปิด file รายงาน `.txt` แล้วเปิด code `input_int` อธิบาย
