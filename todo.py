todolist = []
def add():
    task = input("Enter a task: ")
    todolist.append(task)
    print(f"Added: {task}")

def track():
    if not todolist:
        print("No tasks yet.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(todolist, 1):
            print(f"{i}. {task}")

def delete():
    track()
    try:
        task_no = int(input("Enter the number of the task to remove: "))
        if 1 <= task_no <= len(todolist):
            removed_task = todolist.pop(task_no - 1)
            print(f"Removed: {removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add()
    elif choice == "2":
        track()
    elif choice == "3":
        delete()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid Entry TRY AGAIN")
