# this file contains template for all tasks and a date time function
from datetime import datetime

def timelog() -> str:
    return str(datetime.now().strftime('%H:%M:%S %d-%m-%Y'))

def task_model(identity: int, msg: str) -> dict:
    new = {
            "ID": identity,
            "description": msg,
            "status": "todo",
            "createdAt": timelog(),
            "updatedAt": timelog()
        }
    return new 