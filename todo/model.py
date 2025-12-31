from datetime import datetime

def timelog() -> str:
    """Return current date and time as 'HH:MM:SS DD-MM-YYYY'."""
    return datetime.now().strftime('%H:%M:%S %d-%m-%Y')


def task_model(identity: int, msg: str) -> dict:
    """
    Create a new task dictionary.

    Args:
        identity (int): Unique task ID.
        msg (str): Task description.

    Returns:
        dict: Task with ID, description, status, createdAt, updatedAt.
    """
    return {
        "ID": identity,
        "description": msg,
        "status": "todo",
        "createdAt": timelog(),
        "updatedAt": timelog()
    }
