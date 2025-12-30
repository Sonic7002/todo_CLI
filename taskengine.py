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
        identity = self.data[-1]["ID"] + 1
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
        return self.data.copy()
    
    def list_done(self) -> list[dict]:
        done = []
        for task in self.data():
            if task["status"] == "complete":
                done.append(task)
        return done
    
    def list_inprogress(self) -> list[dict]:
        inprogress = []
        for task in self.data():
            if task["status"] == "in progress":
                inprogress.append(task)
        return inprogress
    
    def list_todo(self) -> list[dict]:
        todo = []
        for task in self.data():
            if task["status"] == "todo":
                todo.append(task)
        return todo
    