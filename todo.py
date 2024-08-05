class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def update_task(self, index, task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['task'] = task

    def complete_task(self, index):
        if index >= 0 and index < len(self.tasks):
            self.tasks[index]['completed'] = True


    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            status = 'Done' if task['completed'] else 'Not Done'
            print(f"{i}. {task['task']} [{status}]")


def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. List Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter the task number to update: "))
            task = input("Enter the new task: ")
            todo_list.update_task(index, task)
        elif choice == '3':
            index = int(input("Enter the task number to complete: "))
            todo_list.complete_task(index)
        elif choice == '4':
            index = int(input("Enter the task number to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            todo_list.list_tasks()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
