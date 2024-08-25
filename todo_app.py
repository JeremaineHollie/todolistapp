# todo_app.py

# List to hold tasks
tasks = []

def display_welcome_message():
    print("Welcome to the To-Do List App!")

def display_menu():
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task():
    try:
        task = input("Enter the task: ")
        if not task.strip():
            raise ValueError("Task cannot be empty.")
        tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")
    except ValueError as e:
        print(f"Error: {e}")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "X" if task["completed"] else " "
            print(f"{i}. [{status}] {task['task']}")

def mark_task_complete():
    try:
        view_tasks()
        task_index = int(input("Enter the task number to mark as complete: ")) - 1
        if task_index < 0 or task_index >= len(tasks):
            raise IndexError("Task number out of range.")
        tasks[task_index]["completed"] = True
        print(f"Task '{tasks[task_index]['task']}' marked as complete.")
    except (IndexError, ValueError) as e:
        print(f"Error: {e}")

def delete_task():
    try:
        view_tasks()
        task_index = int(input("Enter the task number to delete: ")) - 1
        if task_index < 0 or task_index >= len(tasks):
            raise IndexError("Task number out of range.")
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['task']}' deleted.")
    except (IndexError, ValueError) as e:
        print(f"Error: {e}")

def main():
    display_welcome_message()
    
    while True:
        display_menu()
        try:
            choice = int(input("Select an option: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                mark_task_complete()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print("Quitting the application.")
                break
            else:
                raise ValueError("Invalid option. Please select a number between 1 and 5.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
