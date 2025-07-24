import os
import json
TASK_FILE = "tasks.txt"
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeERROR:
                return[]
    return[]
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file)
def main():
    tasks = load_tasks()
    while True:
        print("\n==== To-Do List ====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            n_tasks = int(input("How many tasks do you want to add? "))

            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")
        elif choice == '2':
                if not tasks:
                    print("No tasks to show.")
                else:
                    print("\nTasks:")
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - {status}")
        elif choice == '3':
                        try:
                            task_index = int(input("Enter the task number to mark as done: ")) 
                            if 0 <= task_index < len(tasks):
                                tasks[task_index]["done"] = True
                                print("Task marked as done!")
                            else:
                                print("Invalid task number.")
                        except ValueError:
                            print("Please enter a valid number.")
        elif choice == '4':
            try:
                task_index = int(input("Enter the task number to delete:")) - 1
                if 0 <= task_index < len(tasks):
                    deleted = tasks.pop(task_index)
                    print(f"Deleted task: {deleted['task']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting the To-Do List.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()


            
