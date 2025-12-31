# this file handles all file handling operations
from taskengine import Taskmanager
import json

class Filehandler:
    def __init__(self):
        self.name = "tasks.json"
        
    def load(self) -> list[dict]:
        try:
            with open(self.name, 'r') as f:
                data = json.load(f)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def save(self, data: list[dict]):
            with open(self.name, 'w') as f:
                json.dump(data, f)
