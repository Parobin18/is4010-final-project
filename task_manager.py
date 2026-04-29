import argparse
import json
import os

DEFAULT_FILE = "tasks.json"

# --- Core Logic ---

def load_tasks(filepath=DEFAULT_FILE):
    """Loads tasks from the JSON file."""
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks, filepath=DEFAULT_FILE):
    """Saves tasks to the JSON file."""
    with open(filepath, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(title, filepath=DEFAULT_FILE):
    """Adds a new task."""
    tasks = load_tasks(filepath)
    tasks.append({"title": title, "done": False})
    save_tasks(tasks, filepath)
    return f"Added task: '{title}'"

def list_tasks(filepath=DEFAULT_FILE):
    """Returns a formatted string of all tasks."""
    tasks = load_tasks(filepath)
    if not tasks:
        return "No tasks found."
    
    output = []
    for i, task in enumerate(tasks, 1):
        status = "[x]" if task["done"] else "[ ]"
        output.append(f"{i}. {status} {task['title']}")
    return "\n".join(output)

def complete_task(index, filepath=DEFAULT_FILE):
    """Marks a task as done by its 1-based index."""
    tasks = load_tasks(filepath)
    if index < 1 or index > len(tasks):
        return f"Error: Task #{index} does not exist."
    
    tasks[index - 1]["done"] = True
    save_tasks(tasks, filepath)
    return f"Marked task #{index} as complete."

# --- CLI Implementation ---

def main():
    parser = argparse.ArgumentParser(description="A simple CLI Task Manager.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 'add' command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("title", type=str, help="Title of the task")

    # 'list' command
    subparsers.add_parser("list", help="List all tasks")

    # 'done' command
    parser_done = subparsers.add_parser("done", help="Mark a task as done")
    parser_done.add_argument("index", type=int, help="Task number to complete")

    args = parser.parse_args()

    # Route the command
    if args.command == "add":
        print(add_task(args.title))
    elif args.command == "list":
        print(list_tasks())
    elif args.command == "done":
        print(complete_task(args.index))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()