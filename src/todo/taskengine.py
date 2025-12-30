# this task engine manages all operations on tasks
from model import task_model, timelog

class Taskmanager:

    def __init__(self, data: list[dict]):
        self.data = data

    # Internal

    def _findbyid(self, identity: int) -> dict:
        if self.data == []:
            raise ValueError("No tasks are present")
        for task in self.data:
            if task["ID"] == identity:
                return task
        raise ValueError("No tasks found with the given ID")
        
    # Commands    

    def add(self, msg: str) -> int:
        if self.data == []:
            new = task_model(1, msg)
            self.data.append(new)
            return 1
        identity = max(task["ID"] for task in self.data)+1
        new = task_model(identity, msg)
        self.data.append(new)
        return identity

    def update (self, identity: int, msg: str): 
        task = self._findbyid(identity)
        task["description"] = msg
        task["updated"] = timelog()
    
    def delete(self, identity: int):
        task = self._findbyid(identity)
        self.data.remove(task)

    def mark_inprogress(self, identity: int):
        task = self._findbyid(identity)
        if task["status"] == "in progress":
            raise ValueError("Task is already in progress")
        if task["status"] == "complete":
            raise ValueError("Task is already complete")
        task["status"] = "in progress"

    def mark_done(self, identity: int):
        task = self._findbyid(identity)
        if task["status"] == "complete":
            raise ValueError("Task is already complete")
        task["status"] = "complete"

    # Queries

    def list_all (self) -> list[dict]:
        return [task.copy() for task in self.data]
    
    def list_done(self) -> list[dict]:
        return [task.copy() for task in self.data if task["status"] == "complete"]

    def list_inprogress(self) -> list[dict]:
        return [task.copy() for task in self.data if task["status"] == "in progress"]
    
    def list_todo(self) -> list[dict]:
        return [task.copy() for task in self.data if task["status"] == "todo"]
