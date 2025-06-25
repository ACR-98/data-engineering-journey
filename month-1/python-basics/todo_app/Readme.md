TO-DO LIST MANAGER
==================

A simple command-line task management application built with Python.

FEATURES
--------
- Add new tasks
- Delete existing tasks
- View all tasks
- Save tasks to JSON file
- Persistent storage between sessions

INSTALLATION
------------
1. Ensure you have Python 3.x installed
2. Download the script (todo.py)
3. No additional dependencies required

USAGE
-----
Run the application by executing:
python todo.py

Menu Options:
1. Add task: Enter a new task to your list
2. Delete task: Remove a task by its number
3. View tasks: Display all current tasks
4. Save and exit: Save tasks to file and quit

DATA STORAGE
------------
Tasks are automatically saved to 'tasks.json' in the same directory. The file will be created automatically if it doesn't exist.

CODE STRUCTURE
--------------
- main(): Entry point of the application
- load_tasks(): Loads tasks from JSON file
- save_tasks(): Saves tasks to JSON file
- print_tasks(): Displays all tasks with indexes
- add_task(): Adds a new task to the list
- del_task(): Removes a task from the list

ERROR HANDLING
--------------
The application handles:
- Invalid menu choices
- Invalid task numbers
- JSON file corruption
- File not found cases

EXAMPLE SESSION
---------------
Welcome to the tasks manager.
Please choose from the following options:

1. Add task
2. Delete task
3. View tasks
4. Save and exit

Enter your choice: 1

What task do you want to add?

Buy groceries
Buy groceries has been added

LICENSE
-------
This project is unlicensed. Feel free to use and modify as needed.