
# todo project using file handling
# add new task 
# can view task 
# mark as complete 
# update 
# delete task 

# show task
def show_menu():
    print('1. Add new task')
    print('2. View all task')
    print('3. Marked as completed')
    print('4. Delete a task')
    print('5. Quit')
    

# add new task 
def add_new_task(task):
    with open('todo_file.txt','a') as f:
        f.write(task +"\n")


# view task
def view_task():
    try: 
        with open('todo_file.txt','r') as f:
           tasks = f.readlines()
           if tasks: 
               for i, task in enumerate(tasks, 1):
                print(f'{i}: {task.strip()}')
           else:
                print('Task Not found')
            
    except FileNotFoundError:
        print('task not found')

# creating main function 
def main():
    show_menu()
    choice = input("Enter your choice: ")
    if choice=='1':
        task = input("Add task: ")
        add_new_task(task=task)
        print('Task is added sucessfully')

    elif choice=='2':
        view_task()

    else:
        print("Invalid Input")


if __name__ == "__main__":
    main()
        
    



