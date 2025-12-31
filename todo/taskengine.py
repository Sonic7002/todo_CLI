# taskengine.py
"""
Task manager module for handling all operations on tasks.
"""

from .model import task_model, timelog

class Taskmanager:
    """Manages task creation, updates, deletion, status changes, and queries."""

    def __init__(self, data: list[dict]):
        """
        Initialize the Taskmanager with existing task data.

        Args:
            data (list[dict]): List of existing task dictionaries.
        """
        self.data = data
        self.identity = self._next_id()

    # --- Internal methods ---

    def _next_id(self) -> int:
        """Return the next available task ID."""
        if not self.data:
            return 1
        return max(task["ID"] for task in self.data) + 1

    def _findbyid(self, identity: int) -> dict:
        """
        Find a task by its ID.

        Args:
            identity (int): Task ID to search for.

        Returns:
            dict: The task dictionary.

        Raises:
            ValueError: If no tasks exist or ID not found.
        """
        if not self.data:
            raise ValueError("No tasks are present")
        for task in self.data:
            if task["ID"] == identity:
                return task
        raise ValueError("No tasks found with the given ID")

    # --- Commands ---

    def add(self, msg: str) -> int:
        """
        Add a new task.

        Args:
            msg (str): Task description.

        Returns:
            int: ID of the newly created task.
        """
        task_id = self.identity
        self.data.append(task_model(task_id, msg))
        self.identity += 1
        return task_id

    def update(self, identity: int, msg: str):
        """Update the description of a task by ID."""
        task = self._findbyid(identity)
        task["description"] = msg
        task["updatedAt"] = timelog()

    def delete(self, identity: int):
        """Delete a task by ID."""
        task = self._findbyid(identity)
        self.data.remove(task)

    def mark_inprogress(self, identity: int):
        """Mark a task as in-progress by ID."""
        task = self._findbyid(identity)
        if task["status"] == "in-progress":
            raise ValueError("Task is already in progress")
        if task["status"] == "complete":
            raise ValueError("Task is already complete")
        task["status"] = "in-progress"
        task["updatedAt"] = timelog()

    def mark_done(self, identity: int):
        """Mark a task as complete by ID."""
        task = self._findbyid(identity)
        if task["status"] == "complete":
            raise ValueError("Task is already complete")
        task["status"] = "complete"
        task["updatedAt"] = timelog()

    # --- Queries ---

    def list_all(self) -> list[dict]:
        """Return a copy of all tasks."""
        return [task.copy() for task in self.data]

    def list_done(self) -> list[dict]:
        """Return a copy of all completed tasks."""
        return [task.copy() for task in self.data if task["status"] == "complete"]

    def list_inprogress(self) -> list[dict]:
        """Return a copy of all in-progress tasks."""
        return [task.copy() for task in self.data if task["status"] == "in-progress"]

    def list_todo(self) -> list[dict]:
        """Return a copy of all pending (todo) tasks."""
        return [task.copy() for task in self.data if task["status"] == "todo"]
