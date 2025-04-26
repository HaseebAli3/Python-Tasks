todo_list = []

while True:
    print("--- To-Do List ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Complete Any task")
    print("5. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        if not todo_list:
            print("No tasks found.")
        else:
            counter=1
            for task in todo_list:
                
                if task["completed"]:
                    status="Completed"
                    print(counter, "", task['Task'], "", status)
                    counter+=1
                else:
                    status="Not completed"
                    print(counter, "", task['Task'] , "", status)
                    counter+=1

    elif choice == '2':
        task = input("Enter a new task: ").strip()
        if task:
            todo_list.append({"Task":task ,"completed":False})
            print("Task added")
        else:
            print("You added nothing ")

    elif choice == '3':
        if not todo_list:
            print("No tasks to delete.")
        else:
            counter=1
            for task in todo_list:
                if task['completed']==True:
                    status="completed"
                    print(counter, "", task['Task'] , "", status)
                    counter+=1
                else:
                    status="Not completed"
                    print(counter, "", task['Task'] , "", status)
                    counter+=1
            
            
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(todo_list):
                    removed = todo_list.pop(task_num-1)
                    print("Removed task:")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice =='4':
        compl=int(input("Please Enter the number of task you completed :"))
        if 1 <= compl <= len(todo_list):
            todo_list[compl-1]["completed"]=True
            print("The task is now marked as completed")
        else:
            print("Invalid value bro")
    elif choice == '5':
        print("By")
        break

    else:
        print("Invalid choice. Please try again.")
