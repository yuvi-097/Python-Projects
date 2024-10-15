tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Pending"
            print(f"{index}. [{status}] {task['task']}")

def mark_task_done(index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["done"] = True
        print(f"Task {index} marked as done.")
    else:
        print("Invalid task index.")

def delete_task(index):
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        print(f"Task {index} deleted.")
    else:
        print("Invalid task index.")

while True:
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)

    elif choice == '2':
        view_tasks()

    elif choice == '3':
        index = int(input("Enter task index to mark as done: "))
        mark_task_done(index)

    elif choice == '4':
        index = int(input("Enter task index to delete: "))
        delete_task(index)

    elif choice == '5':
        print("Thank you for using the To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
