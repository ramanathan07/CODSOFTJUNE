import os

# Define a list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = input("Enter a task: ")
    category = input("Enter a category: ")
    due_date = input("Enter a due date (YYYY-MM-DD): ")
    priority = input("Enter priority (high, medium, low): ")
    status = "Not Started"
    tasks.append({
        'Task': task,
        'Category': category,
        'Due Date': due_date,
        'Priority': priority,
        'Status': status
    })

# Function to display tasks
def display_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['Task']} ({task['Category']}) - Due: {task['Due Date']} - Priority: {task['Priority']} - Status: {task['Status']}")

# Function to update a task's status
def update_status():
    display_tasks()
    choice = int(input("Enter the task number to update status: ")) - 1
    if 0 <= choice < len(tasks):
        new_status = input("Enter the new status: ")
        tasks[choice]['Status'] = new_status
        print("Status updated successfully.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task():
    display_tasks()
    choice = int(input("Enter the task number to delete: ")) - 1
    if 0 <= choice < len(tasks):
        del tasks[choice]
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

# Main loop
while True:
    print("\nTO-DO LIST")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Quit")
    
    option = input("Select an option: ")
    
    if option == '1':
        add_task()
    elif option == '2':
        display_tasks()
    elif option == '3':
        update_status()
    elif option == '4':
        delete_task()
    elif option == '5':
        break
    else:
        print("Invalid option. Please try again.")
