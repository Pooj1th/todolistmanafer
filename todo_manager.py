
from datetime import datetime, timedelta
import json

FILENAME = "tasks.json"

def load_tasks(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")
    task = {
        "description": description,
        "due_date": due_date if due_date else "None",
        "status": "Pending"
    }
    tasks.append(task)
    print("Task added successfully.")

def view_tasks(tasks, filter_type=None):
    if not tasks:
        print("No tasks available.")
        return

    print("\n=== TASK LIST ===")
    today = datetime.today().date()
    for i, task in enumerate(tasks):
        task_due = task["due_date"]
        task_status = task["status"]
        show = False

        if filter_type == "completed" and task_status == "Completed":
            show = True
        elif filter_type == "pending" and task_status == "Pending":
            show = True
        elif filter_type == "due_soon":
            if task_due != "None":
                try:
                    due_date_obj = datetime.strptime(task_due, "%Y-%m-%d").date()
                    if 0 <= (due_date_obj - today).days <= 3:
                        show = True
                except:
                    pass
        elif filter_type is None:
            show = True

        if show:
            print(f"{i+1}. {task['description']} | Due: {task['due_date']} | Status: {task['status']}")

def mark_completed(tasks):
    view_tasks(tasks, "pending")
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["status"] = "Completed"
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def edit_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to edit: ")) - 1
        if 0 <= index < len(tasks):
            new_desc = input("Enter new description (leave blank to keep current): ")
            new_due = input("Enter new due date (YYYY-MM-DD) or leave blank: ")
            if new_desc:
                tasks[index]["description"] = new_desc
            if new_due:
                tasks[index]["due_date"] = new_due
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def main():
    tasks = load_tasks(FILENAME)
    while True:
        print("\n=== TO-DO LIST MANAGER ===")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. View completed tasks")
        print("4. View pending tasks")
        print("5. View tasks due soon (within 3 days)")
        print("6. Mark a task as completed")
        print("7. Edit a task")
        print("8. Delete a task")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks, "completed")
        elif choice == "4":
            view_tasks(tasks, "pending")
        elif choice == "5":
            view_tasks(tasks, "due_soon")
        elif choice == "6":
            mark_completed(tasks)
        elif choice == "7":
            edit_task(tasks)
        elif choice == "8":
            delete_task(tasks)
        elif choice == "9":
            save_tasks(tasks, FILENAME)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
