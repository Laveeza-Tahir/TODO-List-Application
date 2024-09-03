
# TO-DO LIST APPLICATION
print("Welcome to To-do list application!")
task: dict = {}

# Add task
def add_task():
    try:
        user_input = input("Enter task:\t") 
        status = input("Enter status:\t") 
        task[user_input] = status
        view_task()
    except:
        print("An error occured while adding task.")


# Update task
def update_task():
    try:
        if not task:
            print("Your To-do list is empty.")
            return
        else:
            new_tasks: dict = {}
            view_task()
            rep_task = input("\nEnter task to Update\n")
            if rep_task in task:  
                new = input ("Enter new task:\t")
                t_id = input("Enter status:\t")
                for item,i in task.items():
                    if item == rep_task:
                        new_tasks[new] =  t_id
                    else:
                        new_tasks[item] = i
        
                task.clear()
                task.update(new_tasks)
                view_task()
            else:
                print(rep_task, " not found.")
            
    except:
        print("An error occured while replacing task.")


# Delete task
def delete_task():
    try:
        if not task:
            print("Your To-do list is empty.")
        else:
            del_task = int(input("Enter task number to delete\t"))
            if del_task.index() in task:
                del task[del_task]
                view_task()
            else:
                print(del_task, " not found in your list")
    except:
        print("An error occured while deleting task.")


# View tasks
def view_task():
    try:
        if task:
            max_key_len = max(len(key) for key in task.keys())
            max_value_len = max(len(value) for value in task.values())
            header = f"\n\n{'Sr. No.':<7} | {'Task':<{max_key_len}} | {'Status':<{max_value_len}}"
            print(header)
            print("-" * len(header))
            for i,(item,status) in enumerate(task.items()):
                print(f"{i+1:<7} | {item:<{max_key_len}} | {status:<{max_value_len}}")
        else:
            
            print("Your To-Do List is empty.")  
    except:
        print("An error occured while showing list.")


# Clear list
def clear_list():
    try:
        if not task:
            print("Your To-do list is empty.")
        else:
            key = input("\nPress Y to continue... ")
            if key == "Y" or key == "y":
                task.clear()
                view_task()
            else:
                print("Invalid Input")
    except:
        print("An error occured while adding task.")


# Main program of file
while True:
    choice = input("""\t----------
Kindly enter your choice:
1. View tasks\t
2. Add task\t                  
3. Update existing task\t
4. Delete task\t
5. Clear list\t
6. Exit\t
    ----------
Your choice:    """)

    # Add value to list
    if choice == "1":
       view_task()

    # update task
    elif choice == "2":
        add_task()
        
    # Delete task
    elif choice == "3":
        update_task()

    # View list
    elif choice == "4":
        delete_task()

    # Clear list
    elif choice == "5":
       clear_list()

    # Exit application
    elif choice == "6":
        print ("\nThanks for using application.")
        break

    # Invalid input
    else:
        print("\nInvalid Input, please try again")

