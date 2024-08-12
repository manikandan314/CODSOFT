def add_task(tasks):
    name = input("Enter task name: ")
    due_date = input("Enter due date (optional): ")
    priority = input("Enter priority (optional): ")
    task = {
        'name': name,
        'due_date': due_date,
        'priority': priority,
        'completed': False
    }
    tasks.append(task)
    print(f"Task '{name}' added successfully.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, 1):
        status = "Done" if task['completed'] else "Not Done"
        print(f"{i}. Task: {task['name']}, Due: {task['due_date']}, Priority: {task['priority']}, Status: {status}")

def delete_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter task number to delete: "))
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['name']}' deleted successfully.")
    else:
        print("Invalid task number.")

def update_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter task number to update: "))
    if 0 < task_number <= len(tasks):
        task = tasks[task_number - 1]
        name = input(f"Enter new task name (press Enter to keep '{task['name']}'): ") or task['name']
        due_date = input(f"Enter new due date (press Enter to keep '{task['due_date']}'): ") or task['due_date']
        priority = input(f"Enter new priority (press Enter to keep '{task['priority']}'): ") or task['priority']
        task.update({'name': name, 'due_date': due_date, 'priority': priority})
        print(f"Task '{name}' updated successfully.")
    else:
        print("Invalid task number.")

def mark_task_complete(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter task number to mark complete: "))
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        print(f"Task '{tasks[task_number - 1]['name']}' marked as complete.")
    else:
        print("Invalid task number.")

def main():
    tasks = []

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_task_complete(tasks)
        elif choice == "6":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
