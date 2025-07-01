#To do list
def main():

    import json

    def load_tasks():#Reads the json as a list
        try:
            with open("tasks.json", "r") as tasks_file:
                return json.load(tasks_file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    tasks = load_tasks() #Converts the json into a list
    def save_tasks(): #Saves a file
        with open("tasks.json", "w") as tasks_file:
            json.dump(tasks, tasks_file, indent=4)
        print("Tasks saved successfully")

    def print_tasks():
        #Prints the elements on the list
        if not tasks:
            print("No tasks found")
            return

        print("\nCurrent Tasks:")
        print("-" * 30)
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else " "
            print(f"{i}: [{status}] {task['task']} (ID: {task['id']})")
        print("-" * 30)

    def add_task():
        task_description = input("\n\nWhat task do you want to add?  \n\n").strip()
        if not task_description:
            print("\nNo task description provided")
            return

        new_id = max(task["id"] for task in tasks) +1 if tasks else 1

        new_task = {
            "id": new_id,
            "task": task_description,
            "done": False,
        }
        tasks.append(new_task)
        print(f"Task {task_description} has been added with ID {new_id}")


    def del_task():
        while True: #Infinite loop until cancel or correct input
            print_tasks()
            try:
                task_num = input("\n\nEnter the number of the task you want to delete or enter x to cancel: \n\n")

                if task_num.lower() == "x": #Turns X into x
                    print("No task has been deleted.")
                    return #Ends the loop

                task_num = int(task_num)

                if 0 <= task_num < len(tasks): #Verifies input as an option
                    deleted_task = tasks.pop(task_num) #Deletes and returns the task in a variable
                    print(f"Task '{deleted_task["task"]}' ID {deleted_task["id"]}has been deleted.")
                    save_tasks()
                    break
                else:
                    print("Please enter a valid task number.")
            except ValueError:
                print("Please enter a valid number.")

    def toggle_task_status():
        print_tasks()
        try:
            task_num = input("\nEnter the number of the task to toggle status (✓/ ) or 'x' to cancel: ").strip()

            if task_num.lower() == "x":
                return

            task_num = int(task_num)
            if 0 <= task_num < len(tasks):
                tasks[task_num]["done"] = not tasks[task_num]["done"]
                status = "completed" if tasks[task_num]["done"] else "pending"
                print(f"Task '{tasks[task_num]['task']}' marked as {status}")
                save_tasks()
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

    def exit_tasks():
        choice = str(input("Do you want to exit? (y/n): ").lower()).strip()
        if choice == "y":
            print("Goodbye")
            return True
        if choice == "n":
            return False
        return False

    options = {
        "1": ("Add task", add_task),
        "2": ("Delete task", del_task),
        "3": ("View tasks", print_tasks),
        "4": ("Toggle task status", toggle_task_status),
        "5": ("Exit", exit_tasks),
    }

    while True:
        print("\nWelcome to the tasks manager.\nPlease choose from the following options:")
        for key, (option, action) in options.items():
            print(f"{key}: {option}")
        try:
            choice = input("\nEnter your choice: ").strip()
            if choice in options:
                _, task = options[choice]
                should_exit = task()
                if should_exit:
                    break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()