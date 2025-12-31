# this file contains the main method and ui logic
import argparse
from todo.taskengine import Taskmanager
from todo.filemanager import Filehandler

def print_task(arr: list[dict]):
    for index, item in enumerate(arr, start = 1):
        print(f"{index}. [{item['ID']}] {item['description']} ({item['status']})")

def main():
    main_parser = argparse.ArgumentParser(prog = "todo")
    subparsers = main_parser.add_subparsers(dest = "command", required = True)

    # todo add <"task">
    parser = subparsers.add_parser("add")
    parser.add_argument("task")

    # todo update  <ID> <"task">
    parser = subparsers.add_parser("update")
    parser.add_argument("id", type = int)
    parser.add_argument("task")

    # todo delete <ID>
    parser = subparsers.add_parser("delete")
    parser.add_argument("id", type = int)

    # todo mark-in-progress <ID>
    parser = subparsers.add_parser("mark-in-progress")
    parser.add_argument("id", type = int)

    # todo mark-done <ID>
    parser = subparsers.add_parser("mark-done")
    parser.add_argument("id", type = int)

    # todo list
    # todo list done
    # todo list todo
    # todo list in-progress
    parser = subparsers.add_parser("list")
    parser.add_argument(
        "type",
        nargs="?",
        choices=["done", "todo", "in-progress"]
    )

    args = main_parser.parse_args()

    store = Filehandler()
    data = store.load()
    manager = Taskmanager(data)

    try:

        match(args.command):

            case "add":
                task_id = manager.add(args.task)
                store.save(data)
                print(f"Task aded successfully (ID: {task_id})")

            case "update":
                manager.update(args.id, args.task)
                store.save(data)
                print("Task updated sucessfully")
                
            case "delete":
                manager.delete(args.id)
                store.save(data)
                print("Task deleted sucessfully")

            case "mark-in-progress":
                manager.mark_inprogress(args.id)
                store.save(data)
                print("Task marked in progress")

            case "mark-done":
                manager.mark_done(args.id)
                store.save(data)
                print("Task marked completed")
                
            case "list":
                match(args.type):

                    case None:
                        print_task(manager.list_all())
                        
                    case "done":
                        print_task(manager.list_done())
                    
                    case "todo":
                        print_task(manager.list_todo())

                    case "in-progress":
                        print_task(manager.list_inprogress())
                    
                    case _:
                        print("No command found")
            case _:
                print("No command found")

    except ValueError as e:
        print(e)
