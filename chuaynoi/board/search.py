"""ค้นหา filter แล้วเรียงประกาศ ไฟล์นี้ห้ามมี input/print (ชุด A)

รายละเอียดอยู่ใน docs/tasks/a-board.md
"""

from chuaynoi import config

SORT_OPTIONS = ("newest", "reward_high", "reward_low", "minutes_short")


def search_requests(requests, keyword="", category="", min_reward=0,
                    only_open=True, sort_by="newest"):
    """return list ใหม่ของ HelpRequest ที่ตรงทุกเงื่อนไข เรียงตาม sort_by (ห้ามไปแก้ list เดิม)"""
    raise NotImplementedError("TODO(ชุด A): search_requests")
