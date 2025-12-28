tasks = []

while True:
    print("\n TO DO LIST")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        if len(tasks) == 0:
            print("No tasks in the list ")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i+1,".",tasks[i])
    elif choice == "2":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added.")
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(i+1,".",tasks[i])
            task_num = int(input("Enter the task number to remove: "))
            if task_num>0 and task_num<=len(tasks):
                tasks.pop(task_num-1)
                print("Task removed.")
            else:
                print("Invalid task number.")
    elif choice == "4":
        print("Byee!!!")
        break
else:
    print("Invalid choice. Please enter a number between 1 and 4.")
