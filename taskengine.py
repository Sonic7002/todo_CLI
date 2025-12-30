# this task engine manages all operations on tasks
from model import task, timelog

def add(msg: str, data: list[dict]):
    if data == []:
        new = task(1, msg)
        data.append(new)
    new = task(data[-1]["ID"] + 1, msg)
    data.append(new)

def update (identity: int, msg: str, data: list[dict]): 
    for task in data:
        if task["ID"] == identity:
            task["description"] = msg
            task["updated"] = timelog()
            
