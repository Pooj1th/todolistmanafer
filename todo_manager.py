# To-Do List Manager
# Mini Project by Poojith R

tasks = []

def show_menu():
    print("\n=== TO-DO LIST MANAGER ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty.")

def view_tasks():
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            status = "✓ Completed" if t["completed"] else "✗ Not Completed"
            print(f"{i}. {t['task']} — {status}")

def mark_completed():
    view_tasks()
    if tasks:
        try:
            task_no = int(input("\nEnter task number to mark as completed: "))
            if 1 <= task_no <= len(tasks):
                tasks[task_no - 1]["completed"] = True
                print(f"Task {task_no} marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_no = int(input("\nEnter task number to delete: "))
            if 1 <= task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"Task '{removed['task']}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting... Thank you for using To-Do List Manager!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()

