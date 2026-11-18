"""ค้นหา กรอง และเรียงประกาศ (ชุด A)

ไม่มี input() กับ print() ไม่รู้จัก app และไม่แตะไฟล์
ดู: docs/tasks/a-board.md หัวข้อ search_requests
"""

from chuaynoi import config

# ค่าที่ sort_by รับได้ ชุด A ต้องทำ SORT_LABELS (ข้อความบนจอ) ใน board/menu.py ให้เรียงลำดับเดียวกัน ดู docs/05-contracts.md ข้อ 4
SORT_OPTIONS = ("newest", "reward_high", "reward_low", "minutes_short")


def search_requests(requests, keyword="", category="", min_reward=0,
                    only_open=True, sort_by="newest"):
    """กรองและเรียงประกาศตามเงื่อนไขที่ให้

    รับ: requests list ของ HelpRequest, keyword คำค้น ("" = ไม่กรอง), category หมวด ("" = ทุกหมวด),
        min_reward แต้มต่อคนขั้นต่ำ, only_open True = เอาเฉพาะประกาศที่ status OPEN,
        sort_by ค่าใดค่าหนึ่งใน SORT_OPTIONS
    คืน: list ใหม่ของ HelpRequest ที่ผ่านทุกกฎ (ว่างได้)
    กฎ: SR1–SR4 (only_open, หมวด, แต้มขั้นต่ำ, คำค้นอยู่ใน title หรือ detail โดยไม่สนตัวพิมพ์เล็กใหญ่)
        การเรียง newest = created_at ใหม่สุดก่อน, reward_high = แต้มมากไปน้อย,
        reward_low = แต้มน้อยไปมาก, minutes_short = เวลาน้อยไปมาก ถ้าเท่ากันคงลำดับเดิม
    แก้ data: ไม่แก้ requests ที่ส่งมา ไม่แตะ app กับไฟล์
    ดู: docs/tasks/a-board.md หัวข้อ search_requests
    """
    raise NotImplementedError("TODO(ชุด A): search_requests")
