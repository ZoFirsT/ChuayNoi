import os
from datetime import datetime

from chuaynoi import config


def summarize_board(app):
    by_category = {}
    for category in config.CATEGORIES:
        by_category[category] = 0

    by_status = {}
    for status in config.REQUEST_STATUSES:
        by_status[status] = 0

    total_reward = 0
    for request in app.requests:
        by_category[request.category] += 1
        by_status[request.status] += 1
        total_reward += request.reward

    if len(app.requests) == 0:
        avg_reward = 0
    else:
        avg_reward = round(total_reward / len(app.requests), 2)

    points_paid = 0
    for txn in app.transactions:
        if txn.kind == config.TXN_EARN:
            points_paid += txn.d_available

    return {
        "total_users": len(app.users),
        "total_requests": len(app.requests),
        "by_category": by_category,
        "by_status": by_status,
        "points_paid": points_paid,
        "avg_reward": avg_reward,
        "top_helpers": find_top_helpers(app),
    }


def find_top_helpers(app):
    points = {}
    for txn in app.transactions:
        if txn.kind == config.TXN_EARN:
            if txn.student_id not in points:
                points[txn.student_id] = 0
            points[txn.student_id] += txn.d_available

    jobs = {}
    for engagement in app.engagements:
        if engagement.status == config.ENG_APPROVED:
            if engagement.helper_id not in jobs:
                jobs[engagement.helper_id] = 0
            jobs[engagement.helper_id] += 1

    ranking = []
    for student_id in points:
        user = app.find_user(student_id)
        if user is None:
            name = student_id
        else:
            name = user.name
        job_count = 0
        if student_id in jobs:
            job_count = jobs[student_id]
        ranking.append((name, points[student_id], job_count))

    ranking = sorted(ranking, key=lambda item: item[1], reverse=True)
    return ranking[:3]


def build_report_lines(summary, created_at):
    lines = [
        "รายงานสรุป ChuayNoi",
        "สร้างเมื่อ " + created_at,
        "=" * 40,
        f"ผู้ใช้ทั้งหมด            {summary['total_users']} คน",
        f"ประกาศทั้งหมด           {summary['total_requests']} รายการ",
        f"แต้มที่โอนให้ผู้ช่วยแล้ว   {summary['points_paid']} แต้ม",
        f"แต้มเฉลี่ยต่อคน          {summary['avg_reward']} แต้ม",
        "",
        "จำนวนประกาศตามหมวด",
    ]
    for category in summary["by_category"]:
        lines.append(f"  {category}   {summary['by_category'][category]}")

    lines.append("")
    lines.append("จำนวนประกาศตามสถานะ")
    for status in summary["by_status"]:
        lines.append(f"  {status}   {summary['by_status'][status]}")

    lines.append("")
    lines.append("อันดับผู้ช่วย")
    if len(summary["top_helpers"]) == 0:
        lines.append("  ยังไม่มีข้อมูล")
    for i in range(len(summary["top_helpers"])):
        name, points, jobs = summary["top_helpers"][i]
        lines.append(f"  {i + 1}. {name}   {points} แต้ม   {jobs} งาน")
    return lines


def export_summary_txt(summary, folder=config.REPORT_DIR):
    now = datetime.now()
    file_name = "summary_" + now.strftime("%Y%m%d_%H%M") + ".txt"
    path = os.path.join(folder, file_name)
    lines = build_report_lines(summary, now.strftime(config.TIME_FORMAT))

    try:
        os.makedirs(folder, exist_ok=True)
        with open(path, "w", encoding=config.TEXT_ENCODING) as file:
            for line in lines:
                file.write(line + "\n")
    except OSError:
        return ""
    return path
