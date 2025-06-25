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
        i=0
        for task in tasks:
            print(f"{i}: {task}")
            i+=1

    def add_task():
        task = input("\n\nWhat task do you want to add?  \n\n")
        tasks.append(task) #Adds task at the end of the list
        print(f"{task} has been added")


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
                    print(f"Task '{deleted_task}' has been deleted.")
                    break
                else:
                    print("Please enter a valid task number.")

            except ValueError:
                print("Please enter a valid number.")

    while True:
        print("\nWelcome to the tasks manager.\nPlease choose from the following options:")
        print("\n1. Add task\n2. Delete task\n3. View tasks\n4. Save and exit")
        try:
            choice = int(input("\nEnter your choice: "))
            if choice < 1 or choice > 4:
                print("Please enter a valid choice.")
                continue
            if choice == 1:
                add_task()
            elif choice == 2:
                del_task()
            elif choice == 3:
                print_tasks()
            elif choice == 4:
                save_tasks()
                print("\n\nThank you for using the tasks manager. Goodbye.\n\n")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()