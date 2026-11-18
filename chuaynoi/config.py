"""ค่าคงที่กับ rule ของ ChuayNoi ที่ทุกชุดใช้ร่วมกัน (แกนกลาง)

ตัวเลข ตัวเลือก และ status อยู่ที่นี่ที่เดียว ไฟล์อื่น import ไปใช้ ไม่พิมพ์ตัวเลขลอย ๆ
ไฟล์นี้ไม่มี function และไม่ใช่งานของชุด A กับชุด B ถ้าต้องเปลี่ยนค่า
ให้เปิด Issue ตามขั้นตอนใน docs/05-contracts.md ข้อ 9 ก่อน
ดู: docs/02-design.md หัวข้อ ข้อตกลงตอนเขียน code
"""

import os

# ---------------------------------------------------------------------------
# path ของไฟล์ทั้งหมด (อิงจากที่อยู่ของไฟล์นี้ เลย run จาก folder ไหนก็ได้)
# ไฟล์นี้อยู่ใน chuaynoi/ เลยต้องถอยขึ้นไปอีกชั้นถึงจะเจอ root ของ repo
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")                # data ที่โปรแกรมใช้จริง (ไม่ขึ้น Git)
SAMPLE_DATA_DIR = os.path.join(BASE_DIR, "sample_data")  # sample data ไว้ reset (ขึ้น Git)
REPORT_DIR = os.path.join(BASE_DIR, "reports")           # ไฟล์ .txt ที่ export จากเมนูสถิติ

USERS_FILE = os.path.join(DATA_DIR, "users.csv")
REQUESTS_FILE = os.path.join(DATA_DIR, "requests.csv")
ENGAGEMENTS_FILE = os.path.join(DATA_DIR, "engagements.csv")
TRANSACTIONS_FILE = os.path.join(DATA_DIR, "transactions.csv")
ACTIVITY_LOG_FILE = os.path.join(DATA_DIR, "activity_log.txt")

CSV_ENCODING = "utf-8-sig"  # utf-8 แบบมี BOM เปิดใน Excel แล้วภาษาไทยไม่เพี้ยน
TEXT_ENCODING = "utf-8"
TIME_FORMAT = "%Y-%m-%d %H:%M"

# ---------------------------------------------------------------------------
# rule ของแต้มน้ำใจ กับช่วงค่าที่ user กรอกได้
# ---------------------------------------------------------------------------
START_POINTS = 100          # แต้มที่ได้ตอนสมัคร
REWARD_MIN = 5              # แต้มต่อผู้ช่วย 1 คน ขั้นต่ำ
REWARD_MAX = 100            # แต้มต่อผู้ช่วย 1 คน สูงสุด
SLOTS_MIN = 1               # รับผู้ช่วยได้กี่คนต่อประกาศ ขั้นต่ำ
SLOTS_MAX = 10              # รับผู้ช่วยได้กี่คนต่อประกาศ สูงสุด
MINUTES_MIN = 5             # เวลาที่น่าจะใช้ (นาที)
MINUTES_MAX = 120
MAX_REVISIONS = 2           # ขอให้แก้งานได้สูงสุดกี่รอบ (feature ระดับ Could)

STUDENT_ID_LENGTH = 10
NAME_MIN, NAME_MAX = 2, 40
TITLE_MIN, TITLE_MAX = 5, 60
DETAIL_MIN, DETAIL_MAX = 0, 300
RESULT_MIN, RESULT_MAX = 5, 300

# ---------------------------------------------------------------------------
# ตัวเลือกให้ user เลือก (ใช้ tuple เพราะไม่ควรมีใครแก้ระหว่าง run)
# ---------------------------------------------------------------------------
CATEGORIES = (
    "ทดสอบเว็บ/แอป",
    "ตรวจสไลด์/เอกสาร",
    "ให้ความเห็นงานออกแบบ",
    "ตอบแบบสอบถาม",
    "ซ้อมนำเสนอ/สัมภาษณ์",
    "อื่น ๆ",
)

FACULTIES = (
    "เทคโนโลยีสารสนเทศและนวัตกรรม",
    "บริหารธุรกิจ",
    "นิเทศศาสตร์",
    "วิศวกรรมศาสตร์",
    "ศิลปกรรมศาสตร์",
    "อื่น ๆ",
)

# rule "ช่วยได้ ไม่ทำแทน" ถ้าประกาศมีคำพวกนี้จะโพสต์ไม่ได้
BANNED_WORDS = (
    "ทำการบ้าน",
    "ทำรายงานแทน",
    "ทำงานแทน",
    "สอบแทน",
    "ทำข้อสอบ",
    "เข้าเรียนแทน",
    "เช็คชื่อแทน",
)

# ---------------------------------------------------------------------------
# status ของประกาศ (HelpRequest)
# ---------------------------------------------------------------------------
REQ_OPEN = "OPEN"              # ยังเปิดรับผู้ช่วยอยู่
REQ_CLOSED = "CLOSED"          # ปิดรับแล้ว แต่ยังมีงานที่ยังไม่ยืนยัน
REQ_COMPLETED = "COMPLETED"    # ยืนยันงานครบทุกชิ้นแล้ว
REQ_CANCELLED = "CANCELLED"    # ปิดรับตอนยังไม่มีใครรับ เลยคืนแต้มทั้งหมด
REQUEST_STATUSES = (REQ_OPEN, REQ_CLOSED, REQ_COMPLETED, REQ_CANCELLED)

# ---------------------------------------------------------------------------
# status ของผู้ช่วยแต่ละคนในประกาศ (Engagement)
# ---------------------------------------------------------------------------
ENG_ACCEPTED = "ACCEPTED"      # รับงานแล้ว กำลังทำอยู่
ENG_SUBMITTED = "SUBMITTED"    # ส่งงานแล้ว รอผู้ขอยืนยัน
ENG_REVISION = "REVISION"      # ผู้ขอขอให้แก้ (Could)
ENG_APPROVED = "APPROVED"      # ยืนยันแล้ว แต้มโอนไปแล้ว
ENG_WITHDRAWN = "WITHDRAWN"    # ผู้ช่วยถอนตัว (Could)
ENGAGEMENT_STATUSES = (ENG_ACCEPTED, ENG_SUBMITTED, ENG_REVISION, ENG_APPROVED, ENG_WITHDRAWN)

# status ที่ยังจองที่และแต้มยังกันไว้ (APPROVED ก็จองที่ แต่แต้มโอนไปแล้ว เลยไม่อยู่ในนี้)
ACTIVE_ENGAGEMENT_STATUSES = (ENG_ACCEPTED, ENG_SUBMITTED, ENG_REVISION)

# state machine: จาก status นี้ไปต่อ status ไหนได้บ้าง
ALLOWED_TRANSITIONS = {
    ENG_ACCEPTED: (ENG_SUBMITTED, ENG_WITHDRAWN),
    ENG_SUBMITTED: (ENG_APPROVED, ENG_REVISION),
    ENG_REVISION: (ENG_SUBMITTED, ENG_WITHDRAWN),
    ENG_APPROVED: (),
    ENG_WITHDRAWN: (),
}

# ---------------------------------------------------------------------------
# ประเภทของรายการแต้มใน transactions.csv
# d_available = แต้มใช้ได้ที่เพิ่ม/ลด, d_held = แต้มกันไว้ที่เพิ่ม/ลด
# ---------------------------------------------------------------------------
TXN_SIGNUP = "SIGNUP"   # สมัครใหม่        ใช้ได้ +100   กันไว้ 0
TXN_HOLD = "HOLD"       # โพสต์ประกาศ      ใช้ได้ -cost  กันไว้ +cost
TXN_PAY = "PAY"         # ผู้ขอจ่าย         ใช้ได้ 0      กันไว้ -reward
TXN_EARN = "EARN"       # ผู้ช่วยได้รับ       ใช้ได้ +reward กันไว้ 0
TXN_REFUND = "REFUND"   # คืนแต้มที่ไม่ได้ใช้   ใช้ได้ +x     กันไว้ -x
TRANSACTION_KINDS = (TXN_SIGNUP, TXN_HOLD, TXN_PAY, TXN_EARN, TXN_REFUND)

# ---------------------------------------------------------------------------
# header ของไฟล์ CSV (ลำดับ column ต้องตรงกับ to_row() ของแต่ละ class)
# ---------------------------------------------------------------------------
USER_FIELDS = ("student_id", "name", "faculty", "skills", "created_at")
REQUEST_FIELDS = (
    "request_id", "owner_id", "title", "detail", "category",
    "reward", "slots", "minutes", "status", "created_at",
)
ENGAGEMENT_FIELDS = (
    "engagement_id", "request_id", "helper_id", "status",
    "result", "revisions", "updated_at",
)
TRANSACTION_FIELDS = (
    "txn_id", "created_at", "student_id", "kind",
    "d_available", "d_held", "request_id", "note",
)

# ---------------------------------------------------------------------------
# หน้าจอ Console
# ---------------------------------------------------------------------------
SCREEN_WIDTH = 64
SKILL_SEPARATOR = ";"   # ไว้คั่นหลายทักษะใน column skills
