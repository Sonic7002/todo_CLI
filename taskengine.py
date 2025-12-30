# this task engine manages all operations on tasks
from model import task

def add(msg: str, data: list[dict]) -> list[dict]:
    if data == []:
        new = task(1, msg)
        return data.append(new)
    new = task(data[-1]["ID"] + 1, msg)
    return data.append(new)

            