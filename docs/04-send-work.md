# 04: เขียน code เสร็จแล้วส่งยังไง

หน้านี้เขียนไว้ให้คนที่ไม่ค่อยได้ใช้ GitHub ทำตามทีละข้อได้เลย ทุกอย่างทำใน GitHub Desktop ไม่ต้องพิมพ์ command

## กติกาของทีม

- `main` คือ code ตัวจริงที่จะส่งอาจารย์ ไม่มีใครแก้ตรง ๆ ได้
- ทุกคนทำงานใน branch ของตัวเอง เสร็จแล้วเปิด PR (Pull Request) มาขอรวมเข้า `main`
- คนที่ review และกด merge มีแค่เจ้าของ repo (ใช้ AI ช่วยตรวจด้วย) คนอื่นเปิด PR ได้อย่างเดียว ปุ่ม merge จะกดไม่ได้ ไม่ต้องตกใจ
- 1 PR ต่อ 1 function หรือ 1 หน้าจอ ชิ้นเล็ก ๆ review ง่าย ได้ merge ไว

## ก่อนเริ่มเขียนทุกครั้ง

1. เปิด GitHub Desktop เช็กมุมซ้ายบนว่า Current Repository เป็น `ChuayNoi`
2. กด Current Branch แล้วเลือก `main`
3. กด Fetch origin ถ้าปุ่มเปลี่ยนเป็น Pull origin ให้กดอีกที เครื่องเราจะได้ code ล่าสุด
4. กด Current Branch อีกรอบ เลือก New Branch แล้วตั้งชื่อ
   - ชุด A: `a/ชื่องาน` เช่น `a/create-request`
   - ชุด B: `b/ชื่องาน` เช่น `b/input-int`
   - ใช้ตัวเล็กทั้งหมด และใช้ขีดกลางแทนช่องว่าง
5. กด Create Branch (ต้องแตกออกมาจาก `main` นะ)
6. กด Open in Visual Studio Code แล้วเริ่มเขียนได้เลย

## ระหว่างเขียน

- แก้เฉพาะไฟล์ของชุดตัวเอง
- run `python tools/reset_data.py` ก่อน แล้ว test ตาม doc ของชุดตัวเอง
- กด Ctrl+S save บ่อย ๆ

## เขียนเสร็จแล้ว ส่งขึ้น GitHub

### 1. เช็กว่าแก้ไฟล์ไหนไปบ้าง

กลับมาที่ GitHub Desktop ดูแท็บ Changes ทางซ้าย จะเห็นรายชื่อไฟล์ที่แก้ ต้องมีแค่ไฟล์ของชุดตัวเอง ถ้ามีไฟล์ที่ไม่ได้ตั้งใจแก้ ให้คลิกขวาที่ไฟล์นั้นแล้วเลือก Discard changes

### 2. Commit

commit คือการเซฟจุดหนึ่งไว้ในเครื่อง ยังไม่ได้ขึ้นเว็บ

1. ช่อง Summary มุมซ้ายล่าง พิมพ์ว่าทำอะไรไป ขึ้นต้นด้วย `feat:` เช่น `feat: input_int`
2. กดปุ่ม Commit to `b/input-int` (ชื่อ branch ของเรา)

### 3. Push

กด Publish branch ด้านบน (ถ้าเคย push branch นี้แล้ว ปุ่มจะเป็น Push origin) ตอนนี้ code ขึ้น GitHub แล้ว

### 4. เปิด PR

1. ใน GitHub Desktop กดปุ่ม Create Pull Request เว็บ GitHub จะเปิดขึ้นมา
2. ด้านบนต้องเป็น `base: main` กับ `compare: b/input-int` (branch ของเรา)
3. Title ใส่เหมือน commit เช่น `feat: input_int`
4. ช่องคำอธิบายจะมีฟอร์มรออยู่แล้ว
   - ลบชุดที่ไม่ใช่ออก แล้วใส่เลข Issue ของสัปดาห์นั้น
   - เขียนว่าทำอะไรไปบ้าง และ test ยังไง (ใส่รหัส test case ได้ เช่น B1, B2)
   - ติ๊ก checklist ข้อที่ทำแล้ว
   - ถ้าเป็น PR สุดท้ายของสัปดาห์ ให้เขียน `Closes #เลข Issue` ด้วย
5. ไม่ต้องใส่ Reviewer ระบบใส่เจ้าของ repo ให้เอง
6. กด Create pull request แล้วส่งลิงก์ PR ในกลุ่มได้เลย

### 5. รอ review

- ถ้าโอเค เจ้าของ repo จะกด merge ให้เอง branch จะถูกลบให้อัตโนมัติ
- ถ้าขอให้แก้ จะมี comment อยู่ในหน้า PR (ดูแท็บ Conversation กับ Files changed) ให้แก้ใน branch เดิมใน VS Code แล้วทำข้อ 2 กับ 3 อีกรอบ (Commit แล้ว Push origin) PR จะอัปเดตเอง ไม่ต้องเปิดใหม่
- ระหว่างรอ เริ่มงานชิ้นต่อไปได้เลย กลับไปทำ "ก่อนเริ่มเขียนทุกครั้ง" สร้าง branch ใหม่จาก `main` แต่ถ้างานชิ้นใหม่ต้องใช้ code ใน PR ที่ยังไม่ merge ให้รอก่อน หรือถามในกลุ่ม

### 6. หลัง merge

ใน GitHub Desktop เลือก `main` แล้วกด Fetch origin ตามด้วย Pull origin เครื่องเราจะมี code ที่เพิ่ง merge ส่วน branch เก่าในเครื่องลบทิ้งได้ (เมนู Branch แล้วเลือก Delete)

## ปัญหาที่เจอบ่อย

| เจออะไร | ทำยังไง |
| --- | --- |
| ลืมสร้าง branch แก้บน `main` ไปแล้วแต่ยังไม่ commit | สร้าง branch ใหม่ได้เลย GitHub Desktop จะถาม ให้เลือก Bring my changes to (ชื่อ branch ใหม่) |
| เผลอ commit บน `main` ไปแล้ว | กด Undo ตรงมุมซ้ายล่าง (ขึ้นอยู่หลัง commit) แล้วสร้าง branch ใหม่ ค่อย commit ใหม่ในนั้น push ขึ้น `main` ตรง ๆ ไม่ได้อยู่แล้ว |
| push แล้วขึ้น error เรื่อง rules หรือ permission | เช็กว่า Current Branch เป็น branch ของตัวเอง ไม่ใช่ `main` |
| หน้า PR ขึ้นว่า This branch has conflicts | อย่าแก้เอง บอกในกลุ่ม เดี๋ยวเจ้าของ repo ช่วย |
| run แล้วขึ้น `ModuleNotFoundError: No module named 'chuaynoi'` | ต้องเปิดทั้ง folder `ChuayNoi` ใน VS Code (ไม่ใช่เปิดไฟล์เดียว) แล้ว run จาก Terminal ที่อยู่ใน folder นั้น |
| `reset_data.py` บอกว่าคัดลอกไฟล์ไม่ได้ | ปิดไฟล์ใน `data/` ที่เปิดค้างไว้ใน Excel ก่อน แล้ว run ใหม่ |

ไม่แน่ใจอะไร ถามในกลุ่มก่อนกด ไม่มีอะไรพังถาวร เพราะ `main` ล็อกไว้แล้ว
