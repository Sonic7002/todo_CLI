# import json
# task = [
#     {"id": 1, "title": "complete homework", "completed": False},
#     {"id": 2, "title": "grind leetcode", "completed": True},
#     {"id": 3, "title": "work on projects", "completed": False}
#     ]

# with open("tasks.json", 'w') as f:
#     json.dump(task, f)

# with open("tasks.json", 'r') as f:
#     data = json.load(f)
# print(data)

import datetime

today = datetime.date.today()
print(type(today))
today = str(today)
print(today)
print(type(today))
time = datetime.now()
print(str(time))