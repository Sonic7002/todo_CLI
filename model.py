# this model file contains template for all tasks
from datetime import datetime

def task(identity: int, msg: str) -> dict:
    new = {
            "ID": identity,
            "description": msg,
            "status": "todo",
            "created": str(datetime.now().strftime('%H:%M:%S %d-%m-%Y')),
            "updated": str(datetime.now().strftime('%H:%M:%S %d-%m-%Y'))
        }
    return new
