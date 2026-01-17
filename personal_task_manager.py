import json
import os

# -----------------------------
# Task Entity
# -----------------------------
class Task:
    def __init__(self, task_id, title, description, completed=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

# -----------------------------
# Task Manager
# -----------------------------
class TaskManager:
    def __init__(self, storage_file="storage.json"):
        self.storage_file = storage_file
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "r") as file:
                data = json.load(file)
                for item in data:
                    task = Task(
                        item["task_id"],
                        item["title"],
                        item["description"],
                        item["completed"]
                    )
                    self.tasks.append(task)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.storage_file, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title, description):
        task_id = len(self.tasks) + 1
        task = Task(task_id, title, description)
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        return self.tasks

    def update_task(self, task_id, new_title, new_description):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = new_title
                task.description = new_description
                self.save_tasks()
                return True
        return False

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = True
                self.save_tasks()
                return True
        return False

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.save_tasks()

# -----------------------------
# Application Entry Point
# -----------------------------
def main():
    manager = TaskManager()

    while True:
        print("\n--- Personal Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Task Title: ")
            description = input("Task Description: ")
            manager.add_task(title, description)
            print("Task added successfully.")

        elif choice == "2":
            tasks = manager.view_tasks()
            if not tasks:
                print("No tasks available.")
            for task in tasks:
                status = "Completed" if task.completed else "Pending"
                print(f"{task.task_id}. {task.title} | {status}")

        elif choice == "3":
            task_id = int(input("Task ID: "))
            title = input("New Title: ")
            description = input("New Description: ")
            if manager.update_task(task_id, title, description):
                print("Task updated successfully.")
            else:
                print("Task not found.")

        elif choice == "4":
            task_id = int(input("Task ID: "))
            if manager.mark_completed(task_id):
                print("Task marked as completed.")
            else:
                print("Task not found.")

        elif choice == "5":
            task_id = int(input("Task ID: "))
            manager.delete_task(task_id)
            print("Task deleted successfully.")

        elif choice == "6":
            print("Exiting Personal Task Manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()