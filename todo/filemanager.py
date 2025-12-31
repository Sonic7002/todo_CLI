# filemanager.py
"""
Handles reading and writing tasks to a JSON file.
"""

from .taskengine import Taskmanager
import json

class Filehandler:
    """Manages loading and saving task data to 'tasks.json'."""

    def __init__(self):
        self.name = "tasks.json"
        
    def load(self) -> list[dict]:
        """
        Load task data from the JSON file.

        Returns:
            list[dict]: List of tasks. Returns empty list if file is missing or invalid.
        """
        try:
            with open(self.name, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def save(self, data: list[dict]):
        """
        Save task data to the JSON file.

        Args:
            data (list[dict]): List of task dictionaries to save.
        """
        with open(self.name, 'w') as f:
            json.dump(data, f, indent=4)
