import json

# Load tasks from tasks.json
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []

# Save tasks to tasks.json
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Create a new task
def create_task(title):
    tasks = load_tasks()
    task = {"title": title, "completed": False}
    tasks.append(task)
    save_tasks(tasks)

# Read all tasks
def read_tasks():
    tasks = load_tasks()
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{index}. {task['title']} - {status}")

# Update task status
def update_task_status(task_index, completed):
    tasks = load_tasks()
    if 0 < task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = completed
        save_tasks(tasks)
    else:
        print("Invalid task index.")

# Delete a task
def delete_task(task_index):
    tasks = load_tasks()
    if 0 < task_index <= len(tasks):
        del tasks[task_index - 1]
        save_tasks(tasks)
    else:
        print("Invalid task index.")

# Main function
def main():
    while True:
        print("\nTask Management System")
        print("1. Create Task")
        print("2. List Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            create_task(title)
            print("Task created.")

        elif choice == "2":
            read_tasks()

        elif choice == "3":
            read_tasks()
            task_index = int(input("Enter task index to update: "))
            completed = input("Mark as completed? (yes/no): ").lower() == "yes"
            update_task_status(task_index, completed)
            print("Task status updated.")

        elif choice == "4":
            read_tasks()
            task_index = int(input("Enter task index to delete: "))
            delete_task(task_index)
            print("Task deleted.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
