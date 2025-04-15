from datetime import datetime


tasks = [
    {"name": "خرید لبنیات", "start": "2025-04-01", "duration": 5, "status": "completed"},
    {"name": "مطالعه کتاب", "start": "2025-04-03", "duration": 10, "status": "in-progress"},
    {"name": "جلسه", "start": "2025-04-02", "duration": 12, "status": "not-started"},
    {"name": "پختن شام", "start": "2025-04-15", "duration": 7, "status": "not-started"},
    {"name": "تسویه بدهی", "start": "2025-04-10", "duration": 3, "status": "completed"}
]

completed_tasks = [task for task in tasks if task["status"] == "completed"]
print("✅ Completed Tasks:")
for task in completed_tasks:
    print(task)


not_started_tasks = [task for task in tasks if task["status"] == "not-started"]

if not_started_tasks:
    earliest_task = min(not_started_tasks, key=lambda x: datetime.strptime(x["start"], "%Y-%m-%d"))
    print("\n🕒 Not Started Task with Earliest Start Date:")
    print(earliest_task)
else:
    print("No tasks with 'not-started status")
