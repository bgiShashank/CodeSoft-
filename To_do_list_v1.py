todo_list = []

def show_task():
    print("=========Your Task List=========")
    if not todo_list:
        print("No tasks in the list.")
    else:
        for ind , task in enumerate(todo_list , 1):
            print(f"{ind}:{task}")

def add_task():
    task = input("enter the task to add: ")
    todo_list.append(task)
    print("Task added successfully")

def update_task():
    task_number = int(input("Enter the task number to update : "))
    if task_number <1 or task_number >len(todo_list):
        print("invalid task number , please re-enter")
        return
    new_task = input("enter the new task:")
    todo_list[task_number - 1 ] = new_task
    print("Task updated successfully")
def delete_task():
    task_number = int(input("Enter the task nuber to delete :"))
    if task_number <1 or task_number > len(todo_list):
        print("Invalid task number , choose a valid task number")
        return
    todo_list.pop(task_number -1)
    print(task_number, "Task deleted successfully")
def save_task_and_exit():
    with open("todo_list.txt","w") as f:
        for task in todo_list:
            f.write(task + "\n")
            print("Task saved successfully")
    print("Exiting the program , Goodbye!")


def menu():
    while True:

        print("=====To_Do List=====")
        print("1.Show task list")
        print("2. Add task to list ")
        print("3. Update task list")
        print("4. Delete task from list")
        print("5. Save and Exit")

        choice = input("Enter your choice (1-5): ")
        if choice =="1":
            show_task()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_task_and_exit()
        else:
            print("Invallid choice. Please choose a valid option ")


menu()