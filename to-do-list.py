class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")

def main():
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == '4':
            print("Quitting the to-do list application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
