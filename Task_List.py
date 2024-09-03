
# TO-DO LIST APPLICATION
print("Welcome to To-do list application!")
task = []

# Add task
def add_task():
    try:
        user_input = input("\nEnter task to add to your list: ") 
        task.append(user_input)
        print(f"{user_input} added.")
        print("Sr./t/tTask/t/tStatus ")
        for i, item in enumerate(task,1):
            print(f"{i}. {item}")


    except:
        print("An error occured while adding task.")     


# Replace task
def replace_task():
    try:
        if not task:
                print("Your To-do list is empty.")
        else:
            rep_task = input("\nEnter task to Replace\n")
            if rep_task in task:
                index = task.index(rep_task)
                new_task = input("Enter new task\t")
                task[index] = new_task
                print(rep_task, " is replaced with ", new_task)
            else:
                print(rep_task, " not found in your To-do list")
    except:
        print("An error occured while replacing task.")


# Delete task
def delete_task():
    try:
        if not task:
            print("Your To-do list is empty.")
        else:
            del_task = input("\nEnter task to delete\t")
            if del_task in task:
                task.remove(del_task)
                print(del_task, " deleted successfully!")
            else:
                print(del_task, " not found in your list")
    except:
        print("An error occured while deleting task.")


# View tasks
def view_task():
    try:
        if task:
            print("\nYour current To-Do List is given below:\n")
            for i,item in enumerate(task,1):
                print(f"{i}. {item}")
        else:
            print("Your To-Do List is empty.\n")  
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
                print("Your To-do list has been cleared.")
            else:
                print("Invalid Input")
    except:
        print("An error occured while adding task.")


# Main program of file
while True:
    choice = input("""\nKindly enter your choice:
1. Add task\t
2. Replace existing task\t
3. Delete task\t
4. View tasks\t
5. Clear your list\t
6. Exit\t
    ----------
Your choice:    """)

    # Add value to list
    if choice == "1":
       add_task()

    # Replace task
    elif choice == "2":
        replace_task()
        
    # Delete task
    elif choice == "3":
        delete_task()

    # View list
    elif choice == "4":
        view_task()

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

