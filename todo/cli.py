"""
cli.py

Main entry point for the Todo CLI application.

Provides a Git-style command-line interface to manage tasks:
add, update, delete, mark-in-progress, mark-done, and list tasks.
"""

import argparse
import sys
from .taskengine import Taskmanager
from .filemanager import Filehandler


def print_task(arr: list[dict]):
    """Print a list of tasks to the console."""
    if not arr:
        print("No tasks found")
        return
    for item in arr:
        print(f"[{item['ID']}] {item['description']} ({item['status']})")


def main():
    """Parse command-line arguments and execute the appropriate task command."""
    main_parser = argparse.ArgumentParser(
        prog="todo",
        description="A simple CLI todo manager. Manage your tasks from the terminal.\nDeveloped by: Srijan Kargupta",
        epilog="""Examples:
  todo add "Buy groceries"
  todo update 1 "Buy groceries and lunch"
  todo list
  todo list done
  todo mark-in-progress 2
  todo mark-done 1
  todo delete 3""",
        formatter_class=argparse.RawTextHelpFormatter
    )

    subparsers = main_parser.add_subparsers(
        dest="command",
        required=True,
        title="Commands",
        description="Available commands"
    )

    # --- Commands ---
    parser = subparsers.add_parser("add", help="Add a new task", description="Add a new task with the given description.")
    parser.add_argument("task", help="The task description in quotes.")

    parser = subparsers.add_parser("update", help="Update an existing task", description="Update the description of an existing task by ID.")
    parser.add_argument("id", type=int, help="ID of the task to update.")
    parser.add_argument("task", help="The new description of the task.")

    parser = subparsers.add_parser("delete", help="Delete a task", description="Delete a task by its ID.")
    parser.add_argument("id", type=int, help="ID of the task to delete.")

    parser = subparsers.add_parser("mark-in-progress", help="Mark a task as in-progress", description="Mark a task as in-progress by its ID.")
    parser.add_argument("id", type=int, help="ID of the task to mark in-progress.")

    parser = subparsers.add_parser("mark-done", help="Mark a task as complete", description="Mark a task as complete by its ID.")
    parser.add_argument("id", type=int, help="ID of the task to mark done.")

    parser = subparsers.add_parser("list", help="List tasks", description="List tasks optionally filtered by status: done, to-do, in-progress.")
    parser.add_argument("type", nargs="?", choices=["done", "to-do", "in-progress"], help="Optional filter for task status.")

    args = main_parser.parse_args()

    store = Filehandler()
    data = store.load()
    manager = Taskmanager(data)

    try:
        match args.command:
            case "add":
                task_id = manager.add(args.task)
                store.save(data)
                print(f"Task added successfully (ID: {task_id})")

            case "update":
                manager.update(args.id, args.task)
                store.save(data)
                print("Task updated successfully")

            case "delete":
                manager.delete(args.id)
                store.save(data)
                print("Task deleted successfully")

            case "mark-in-progress":
                manager.mark_inprogress(args.id)
                store.save(data)
                print("Task marked in progress")

            case "mark-done":
                manager.mark_done(args.id)
                store.save(data)
                print("Task marked complete")

            case "list":
                match args.type:
                    case None:
                        print_task(manager.list_all())
                    case "done":
                        print_task(manager.list_done())
                    case "to-do":
                        print_task(manager.list_todo())
                    case "in-progress":
                        print_task(manager.list_inprogress())
                    case _:
                        print("No command found")
            case _:
                print("No command found")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    sys.exit(0)
