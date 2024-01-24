import json

def load_tasks():
    """Loads tasks from the JSON file."""
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Saves tasks to the JSON file."""
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def add_task(task):
    """Adds a task to the list."""
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def list_tasks():
    """Lists all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def update_task(task_id, new_task):
    """Updates a task with the given ID."""
    tasks = load_tasks()
    if task_id <= 0 or task_id > len(tasks):
        print("Invalid task ID.")
    else:
        tasks[task_id - 1] = new_task
        save_tasks(tasks)
        print("Task updated successfully!")

def delete_task(task_id):
    """Deletes a task with the given ID."""
    tasks = load_tasks()
    if task_id <= 0 or task_id > len(tasks):
        print("Invalid task ID.")
    else:
        del tasks[task_id - 1]
        save_tasks(tasks)
        print("Task deleted successfully!")

def main():
    """Main function to handle user interaction."""
    while True:
        print("\nWelcome to your Todo List!")
        print("1. Add task")
        print("2. List tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            new_task = input("Enter new task: ")
            update_task(task_id, new_task)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
