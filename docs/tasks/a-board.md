# ชุด A: บอร์ดประกาศ

> ความยาก ★★★ (function หลัก 6 ตัว + หน้าจอ 4 หน้า) ส่วนนี้คือตัวหลักของโปรแกรมเลย
> ถ้าจะเลือกชุดนี้ ไปเปิด Issue ที่ติดป้าย `pkg: A-board` แล้ว assign ตัวเองได้เลย

## ชุดนี้ทำอะไร

ทุกอย่างที่เกี่ยวกับประกาศอยู่ในชุดนี้หมด ตั้งแต่โพสต์ขอความช่วยเหลือ ค้นหาประกาศ สมัครช่วย ส่งงาน ให้ผู้ขอยืนยันงาน ไปจนถึงปิดรับ

## File ที่ต้องดูแล

| File | ต้องเขียนอะไรบ้าง |
| --- | --- |
| `chuaynoi/board/service.py` | `create_request`, `apply_to_request`, `submit_work`, `approve_work`, `close_request` |
| `chuaynoi/board/search.py` | `search_requests` |
| `chuaynoi/board/menu.py` | `screen_board`, `screen_post`, `screen_my_requests`, `screen_my_jobs` |

## ของคนอื่นที่ต้องเรียกใช้

| ใช้อะไร | มาจากไหน | เอาไปทำอะไร |
| --- | --- | --- |
| `HelpRequest`, `Engagement` | แกนกลาง `core/models.py` | สร้างประกาศ กับงานของผู้ช่วย |
| `app.find_request()`, `app.find_engagement()`, `app.next_id()` | แกนกลาง `core/storage.py` | หา data และสร้างรหัสใหม่ |
| `add_transaction()`, `get_balance()` | แกนกลาง `wallet/service.py` | กันแต้ม โอนแต้ม คืนแต้ม |
| `input_int()`, `input_text()`, `input_choice()`, `input_yes_no()` | ชุด B `ui/inputs.py` | รับ input จากผู้ใช้ในหน้าจอ |
| `print_table()`, `print_header()`, `print_menu()` | แกนกลาง `ui/display.py` | โชว์ตาราง หัวจอ และเมนู `[1] ... [0] กลับ` |

## แผนแต่ละสัปดาห์

- [ ] สัปดาห์ 1: ลงเครื่องมือให้เรียบร้อย เลือกชุด อ่าน [01](../01-overview.md) กับ [02](../02-design.md) แล้วเขียน `search_requests` จากนั้นร่าง flowchart ของ `create_request` กับ `approve_work` บนกระดาษไว้ก่อน
- [ ] สัปดาห์ 2: `create_request`, `apply_to_request`, `submit_work` (ส่ง PR ทีละ function นะ)
- [ ] สัปดาห์ 3: `approve_work`, `close_request` แล้วก็หน้าจอทั้ง 4
- [ ] สัปดาห์ 4: ทำ test case A1–A16 และเขียนรายงานส่วนของตัวเอง
- [ ] สัปดาห์ 5: ทำคลิปส่วนของตัวเอง

## Pattern ที่ทุก function ใน `service.py` ใช้

```python
def ชื่อฟังก์ชัน(app, ...):
    # 1. หาข้อมูลที่ต้องใช้
    # 2. ตรวจกติกาทีละข้อ ข้อไหนไม่ผ่าน return (False, "เหตุผล") ทันที
    # 3. ผ่านครบแล้วจึงเปลี่ยนข้อมูล
    # 4. return (True, "ข้อความสำเร็จ")
```

ถ้ามี rule ไหนไม่ผ่าน **ห้ามแก้ data อะไรเลย** เพราะเราเช็กทุกข้อให้ครบก่อนแก้เสมอ

เวลาปัจจุบันให้ใช้ `datetime.now().strftime(config.TIME_FORMAT)` ตัวนี้ import ไว้ใน file ให้แล้ว

## Function ทีละตัว

### 1. `search_requests(requests, keyword, category, min_reward, only_open, sort_by)`

return list ใหม่ที่มีแต่ประกาศที่ตรงทุกเงื่อนไข ห้ามไปแก้ list เดิม

1. เริ่มจาก `results = []`
2. วน `for request in requests:` เจอประกาศที่ไม่ตรงก็ข้ามไปเลย (`continue`) ซึ่งก็คือกรณีพวกนี้
   - `only_open` เป็น `True` และ `request.status != config.REQ_OPEN`
   - `category` ไม่ว่าง และ `request.category != category`
   - `request.reward < min_reward`
   - `keyword` ไม่ว่าง และ `keyword.lower()` ไม่อยู่ใน `(request.title + " " + request.detail).lower()`
3. ถ้าผ่านครบทุกข้อ ก็ `results.append(request)`
4. สุดท้ายเรียงตาม `sort_by` โดยใช้ `sorted(results, key=..., reverse=...)`

| `sort_by` | เรียงยังไง |
| --- | --- |
| `"newest"` | `created_at` มากไปน้อย |
| `"reward_high"` | `reward` มากไปน้อย |
| `"reward_low"` | `reward` น้อยไปมาก |
| `"minutes_short"` | `minutes` น้อยไปมาก |

```python
def get_reward(request):          # ฟังก์ชันเล็ก ๆ บอก sorted ว่าให้เรียงด้วยค่าอะไร
    return request.reward

results = sorted(results, key=get_reward, reverse=True)
```

ใช้เรื่อง: loop `for`, `if` + `continue`, `and`, `in`, `.lower()`, `sorted()`

### 2. `create_request(app, owner_id, title, detail, category, reward, slots, minutes)`

โพสต์ประกาศใหม่ แล้วกันแต้มไว้

1. เอา `title + " " + detail` มาต่อกัน แล้ววน `for word in config.BANNED_WORDS:` ถ้า `word in` ข้อความนั้นเมื่อไหร่ ให้ `return (False, "ประกาศนี้ขอให้ทำงานแทน ผิดกติกา 'ช่วยได้ ไม่ทำแทน'")` เลย
2. เช็กว่า `reward` อยู่ระหว่าง `config.REWARD_MIN` ถึง `config.REWARD_MAX`, `slots` อยู่ระหว่าง `config.SLOTS_MIN` ถึง `config.SLOTS_MAX` และ `category in config.CATEGORIES`
3. คิด `cost = reward * slots`
4. `available, held = get_balance(app, owner_id)` แล้วถ้า `available < cost` ให้ `return (False, "แต้มไม่พอ ต้องใช้ 60 มี 55")`
5. สร้างรหัสด้วย `request_id = app.next_id("R", [r.request_id for r in app.requests], 4)`
6. สร้าง `HelpRequest(...)` ให้สถานะเป็น `config.REQ_OPEN` แล้ว `app.requests.append(...)`
7. บันทึกการกันแต้มด้วย `add_transaction(app, owner_id, config.TXN_HOLD, -cost, cost, request_id, "กันแต้ม 15 x 3 คน")`
8. จบด้วย `return (True, "โพสต์ประกาศ R0004 แล้ว กันแต้มไว้ 45 แต้ม")`

ใช้เรื่อง: loop `for`, `in`, เงื่อนไขเช็กช่วงค่า, การคูณ, เรียก function จาก module อื่น, สร้าง object

### 3. `apply_to_request(app, helper_id, request_id)`

สมัครช่วยงาน ถ้ายังมีที่ว่างก็ได้งานทันที ตรงนี้แต้มไม่ขยับนะ เพราะกันไว้แล้วตั้งแต่ตอนโพสต์

1. `request = app.find_request(request_id)` ถ้าได้ `None` ตอบ "ไม่พบประกาศ"
2. ถ้า `request.status != config.REQ_OPEN` ตอบ "ประกาศนี้ปิดรับแล้ว"
3. ถ้า `request.owner_id == helper_id` ตอบ "ช่วยงานของตัวเองไม่ได้"
4. วน `app.engagements` หาอันที่ `request_id` ตรง, `helper_id` ตรง และสถานะไม่ใช่ `config.ENG_WITHDRAWN` ถ้าเจอ ตอบ "คุณรับงานนี้ไปแล้ว"
5. ถ้า `request.count_used_slots(app.engagements) >= request.slots` ตอบ "ที่เต็มแล้ว"
6. สร้างรหัสด้วย `engagement_id = app.next_id("E", ..., 4)` แล้วสร้าง `Engagement(..., status=config.ENG_ACCEPTED, result="", revisions=0, ...)` จากนั้น append
7. `return (True, "รับงาน R0002 แล้ว รหัสงานของคุณคือ E0003")`

### 4. `submit_work(app, helper_id, engagement_id, result)`

1. `engagement = app.find_engagement(engagement_id)` ถ้าได้ `None` หรือ `engagement.helper_id != helper_id` ตอบ "ไม่พบงานนี้ในงานที่คุณรับไว้"
2. ถ้า `result.strip()` ว่าง ตอบ "กรุณาใส่ผลงาน"
3. เปลี่ยนสถานะแบบนี้

   ```python
   try:
       engagement.change_status(config.ENG_SUBMITTED)
   except ValueError as error:
       return (False, str(error))
   ```

4. เก็บค่า `engagement.result` กับ `engagement.updated_at`
5. `return (True, "ส่งงาน E0004 แล้ว รอผู้ขอยืนยัน")`

### 5. `approve_work(app, owner_id, engagement_id)`

ฝั่งผู้ขอยืนยันงาน แล้วโอนแต้มให้ผู้ช่วย

1. หา `engagement` และ `request = app.find_request(engagement.request_id)` ถ้าไม่เจอ หรือ `request.owner_id != owner_id` ตอบ "ไม่พบงานนี้ในประกาศของคุณ"
2. ถ้า `engagement.status != config.ENG_SUBMITTED` ตอบ "ยืนยันได้เฉพาะงานที่ส่งแล้ว"
3. `engagement.change_status(config.ENG_APPROVED)` แล้วเก็บ `updated_at`
4. ฝั่งผู้ขอ: `add_transaction(app, owner_id, config.TXN_PAY, 0, -request.reward, ...)`
5. ฝั่งผู้ช่วย: `add_transaction(app, engagement.helper_id, config.TXN_EARN, request.reward, 0, ...)`
6. นับงานของประกาศนี้ที่ยังอยู่ใน `config.ACTIVE_ENGAGEMENT_STATUSES` ถ้านับได้ 0 **และ** (ประกาศเป็น `REQ_CLOSED` **หรือ** ที่ถูกใช้ครบ `slots` แล้ว) ให้ตั้ง `request.status = config.REQ_COMPLETED`
7. `return (True, "ยืนยันงานแล้ว โอน 15 แต้มให้ ฟ้าใส สดใส")`

### 6. `close_request(app, owner_id, request_id)`

ปิดรับ ไม่ให้ผู้ช่วยสมัครเพิ่มแล้ว จากนั้นคืนแต้มของที่ว่างที่เหลือ

1. หา `request` ถ้าไม่เจอ หรือคนที่กดไม่ใช่เจ้าของ ตอบ "ไม่พบประกาศนี้ในประกาศของคุณ"
2. ถ้า `request.status != config.REQ_OPEN` ตอบ "ปิดรับได้เฉพาะประกาศที่เปิดอยู่"
3. คิด `used = request.count_used_slots(app.engagements)` กับ `unused = request.slots - used`
4. ถ้า `unused > 0` ให้คิด `refund = unused * request.reward` แล้ว `add_transaction(app, owner_id, config.TXN_REFUND, refund, -refund, ...)`
5. ตั้งสถานะใหม่ตามตารางนี้

   | เงื่อนไข | สถานะ |
   | --- | --- |
   | `used == 0` (ไม่มีใครรับเลย) | `REQ_CANCELLED` |
   | ไม่มีงานที่ยัง active แล้ว | `REQ_COMPLETED` |
   | ยังมีงานที่รอยืนยันอยู่ | `REQ_CLOSED` |

6. `return (True, "ปิดรับ R0001 แล้ว คืน 15 แต้ม")`

## หน้าจอใน `menu.py`

ทุกหน้าจอใช้ flow เดียวกันหมด

1. รับ input ด้วย `inputs`
2. เรียก service
3. พิมพ์ `[OK] ข้อความ` หรือ `[!] ข้อความ`
4. ถ้าสำเร็จ เรียก `storage.save_all(app)` และ `storage.append_log(app.current_user_id, "CREATE_REQUEST R0004")`

| หน้าจอ | เมนู | ทำอะไร |
| --- | --- | --- |
| `screen_board` | 1 | ถามคำค้น หมวด (มีตัวเลือก "ทุกหมวด") แต้มขั้นต่ำ และการเรียง แล้วส่งให้ `search_requests` เอาผลมาโชว์เป็นตาราง รหัส/หัวข้อ/แต้ม/ที่ว่าง จากนั้นให้พิมพ์รหัสเพื่อสมัครช่วย หรือ 0 เพื่อกลับ |
| `screen_post` | 2 | ถามหัวข้อ รายละเอียด หมวด แต้มต่อคน จำนวนคน และเวลา แล้วโชว์ "กันแต้ม 10 x 3 = 30 แต้ม ใช้ได้หลังโพสต์ 25" ให้ดูก่อน ถามยืนยันด้วย `input_yes_no` แล้วค่อยเรียก `create_request` |
| `screen_my_requests` | 3 | โชว์ตารางประกาศของฉัน ให้เลือกประกาศ แล้วโชว์ตารางผู้ช่วยกับผลงาน มีให้เลือก [1] ยืนยันงาน [2] ปิดรับ [0] กลับ (ถาม y/n ก่อนทุกครั้ง) |
| `screen_my_jobs` | 4 | โชว์ตารางงานที่ฉันรับไว้ ให้เลือกงาน ถามผลงาน แล้วเรียก `submit_work` |

```text
---------------- โพสต์ขอความช่วยเหลือ ----------------
หัวข้อ (5-60 ตัวอักษร): ช่วยทดสอบแอปจองห้องสมุด
รายละเอียด (ไม่เกิน 300 ตัวอักษร, เว้นว่างได้): ลองจองห้อง 1 ครั้ง
เลือกหมวด
  [1] ทดสอบเว็บ/แอป
  [2] ตรวจสไลด์/เอกสาร
  ...
พิมพ์หมายเลข (1-6): 1
แต้มต่อคน (5-100): 10
จำนวนผู้ช่วย (1-10): 3
เวลาโดยประมาณ นาที (5-120): 15

สรุป: กันแต้ม 10 x 3 = 30 แต้ม | ใช้ได้หลังโพสต์ 25 แต้ม
ยืนยันโพสต์? (y/n): y
[OK] โพสต์ประกาศ R0004 แล้ว กันแต้มไว้ 30 แต้ม
```

## Test case

รัน `python tools/reset_data.py` ครั้งเดียวก่อน แล้วไล่ทำ A1–A16 **ตามลำดับ** ให้จบในรอบเดียว เพราะผลของข้อหลังขึ้นอยู่กับข้อก่อนหน้า

| TC | ทดสอบอะไร | ทำยังไง | ผลที่ต้องได้ |
| --- | --- | --- | --- |
| A1 | ค้นหาคำ | คำค้น `สไลด์` | พบ R0002 อันเดียว |
| A2 | กรอง | หมวด `ทดสอบเว็บ/แอป` แต้มขั้นต่ำ 10 | พบ R0001 อันเดียว |
| A3 | เรียง | เรียง `reward_high` | R0002, R0001, R0003 |
| A4 | ไม่พบ | คำค้น `ดาวอังคาร` | `[i] ไม่พบประกาศที่ตรงเงื่อนไข` |
| A5 | โพสต์สำเร็จ | `9990000003` โพสต์ 15 × 3 | ได้ R0004, ยอดเป็น `(55, 45)` |
| A6 | แต้มไม่พอ | `9990000001` โพสต์ 30 × 2 | ปฏิเสธ ยอดยัง `(55, 30)` ไม่มี R0005 |
| A7 | คำต้องห้าม | หัวข้อ `ช่วยทำการบ้านให้หน่อย` | ปฏิเสธพร้อมบอกกติกา |
| A8 | ช่วยงานตัวเอง | `9990000001` สมัคร R0001 | ปฏิเสธ |
| A9 | สมัครซ้ำ | `9990000002` สมัคร R0001 | ปฏิเสธ |
| A10 | ที่เต็ม | `9990000001` สมัคร R0002 แล้ว `9990000003` สมัคร R0002 | คนแรกได้ E0003, คนที่สองถูกปฏิเสธ |
| A11 | ยืนยันก่อนส่ง | `9990000002` สมัคร R0003 (ได้ E0004) แล้ว `9990000004` ยืนยัน E0004 | ปฏิเสธ สถานะยัง ACCEPTED |
| A12 | ส่งงาน | `9990000002` ส่งงาน E0004 | สถานะเป็น SUBMITTED |
| A13 | ยืนยันและโอนแต้ม | `9990000001` ยืนยัน E0002 | `9990000003` เป็น `(70, 45)`, `9990000001` เป็น `(55, 15)` |
| A14 | ปิดรับ คืนที่ว่าง | `9990000001` ปิด R0001 | คืน 15, `9990000001` เป็น `(70, 0)`, R0001 เป็น COMPLETED |
| A15 | ปิดรับไม่มีคนรับ | `9990000003` ปิด R0004 | คืน 45, `9990000003` เป็น `(115, 0)`, R0004 เป็น CANCELLED |
| A16 | แต้มรวม | รวมใช้ได้ + กันไว้ ของทุกคน | `400` |

## รายงานและคลิป

- ในรายงานต้องมี flowchart ของ `create_request` และ `approve_work`, คำอธิบาย function ทั้ง 6 ตัว (ชื่อ รับอะไร คืนอะไร ทำอะไร), คู่มือเมนู 1–4 พร้อมภาพหน้าจอจริง และผล A1–A16
- ในคลิปให้ demo ตั้งแต่โพสต์ รับงาน ส่งงาน ไปจนกดยืนยัน (ให้เห็นว่าแต้มโอนจริง) โชว์กรณีแต้มไม่พอด้วย แล้วเปิด code `create_request` อธิบาย
