
# Todo List Application

A simple Python application to manage a to-do list using various data structures such as lists, dictionaries, and classes.

## Features
1. Add tasks with a description and due date.
2. View all tasks.
3. Mark tasks as completed.
4. Delete tasks.
5. Save and load tasks from a file.

## Data Structures Used
1. **List**: To store tasks.
2. **Dictionary**: To represent each task with its details.
3. **Class (optional)**: To encapsulate task attributes and methods.

## Implementation

```python
import json

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def __repr__(self):
        status = 'Done' if self.completed else 'Not Done'
        return f"Task(description='{self.description}', due_date='{self.due_date}', status='{status}')"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)
        print(f"Added task: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

    def mark_task_completed(self, index):
        try:
            task = self.tasks[index - 1]
            task.completed = True
            print(f"Task marked as completed: {task}")
        except IndexError:
            print("Invalid task index.")

    def delete_task(self, index):
        try:
            task = self.tasks.pop(index - 1)
            print(f"Deleted task: {task}")
        except IndexError:
            print("Invalid task index.")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            tasks_data = [{'description': task.description, 'due_date': task.due_date, 'completed': task.completed} for task in self.tasks]
            json.dump(tasks_data, file)
        print("Tasks saved to file.")

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(task['description'], task['due_date']) for task in tasks_data]
                for i, task in enumerate(self.tasks):
                    task.completed = tasks_data[i]['completed']
            print("Tasks loaded from file.")
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON from file.")

# Example usage
def main():
    todo_list = TodoList()
    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Load Tasks")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            todo_list.add_task(description, due_date)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_task_completed(index)
        elif choice == '4':
            index = int(input("Enter task index to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            filename = input("Enter filename to save tasks: ")
            todo_list.save_tasks(filename)
        elif choice == '6':
            filename = input("Enter filename to load tasks: ")
            todo_list.load_tasks(filename)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

## Explanation

1. **Task Class**: Represents each task with a description, due date, and completion status.
2. **TodoList Class**: Manages the list of tasks and provides methods to add, view, mark as completed, delete, save, and load tasks.
3. **Main Function**: Provides a simple command-line interface for interacting with the Todo List Application.

This project demonstrates practical use of lists and dictionaries, and optionally, classes to create a more organized and manageable application.
