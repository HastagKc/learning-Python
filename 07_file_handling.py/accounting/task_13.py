# Task
# First ask the user to login or register
# If register ask for username and password then store that data in a file
# Else if login ask for username and password then compare it with the data in the file where user data is stored
# While login If the user is a valid user then ask him/her for three options : check balance, add balance and redeem balance
# Add balance : ask the amount to add then add the amount with balance as a dictionary {'ram':23000}-{'ram':50000} store this data in a file
# Check blanace : read the file where amount is being stored then print the summation of every data which matches with user's username



import json

# register function
def register():
    username = input('Enter your username : ').strip()
    password = input('Enter your password : ').strip()

    user_data = {username:password}
    # print(type(user_data)) #<class 'dict'>

    f = open('D:/MindRisers/task13/userdetails.txt','a')

    json_user_data = json.dumps(user_data) # converting dict data to json data 

    f.write(json_user_data + '-') # writing json data in the file 

    f.close()
    print('Register Sucessfull')


# creating login 
def login():
    user_name = input("Enter username: ").strip()
    user_password = input("Enter password: ").strip()

    try:
        loggedin_user = ''
        is_login = False
        f = open('D:/MindRisers/task13/userdetails.txt', 'r')
        user_datas = f.read()
        list_user_datas = user_datas.split('-')  # Splitting data by '-'
        for data in list_user_datas:
            if data.strip():  # Checking if data is not empty
                dict_data = json.loads(data)  # Converting JSON string to dictionary
                if user_name in dict_data and dict_data[user_name] == user_password:
                    loggedin_user = user_name
                    is_login = True
                    break
        f.close()      
        if is_login: 
            print('Login Sucessfull') 
            return loggedin_user 
        else:
            print('invalid Credential')
            loggedin_user = ''
            return loggedin_user     
                

    except FileNotFoundError:
        print('User data file not found')

# show option
def show_option():
    print('Select an option:\n1: Check balance\n2: Add balance \n')

# checking total balance of user
def check_balance(user):
    file_path = f'D:/MindRisers/task13/{user}.txt'
    f = open(file_path, 'r')
    total_balance = 0
    balance = f.readlines()
    # print(type (balance))
    for i in balance:
        # print(type(i)) 
        balance = int(i.strip()) 
        total_balance = total_balance + balance
    print(f'Your Total balance is :{total_balance}')
    f.close()

# add balance 
def add_balance(user):
    file_path = f'D:/MindRisers/task13/{user}.txt'
    f = open(file_path, 'a')
    add_amount = int(input('Enter Your amount: '))
    if add_amount < 0:
        print("Add amount can't be negative")

    else:
         f.write(str(add_amount) + "\n")
         print(f'{add_amount} is add sucessfully: ')
    f.close()
    

# main function
def main():
    choice = input('Do you want to 1.login or 2.register: ').strip().lower()
    if choice == 'register' or choice=='2':
        register()

    elif choice == 'login' or choice=='1':
        logged_user = login()
        if logged_user != '':
            print(logged_user)
            # creating file for all user 
            file_path = f'D:/MindRisers/task13/{logged_user}.txt'
            f = open(file_path, 'a')
            f.close()
            show_option()
            user_option = input('Enter your option: ').lower().strip()

            if user_option == 'check balance' or user_option == '1':
                check_balance(logged_user)

            elif user_option == 'add balance' or user_option == '2':
                add_balance(logged_user)

    else:
        print('invalid Input')    

# main function call 
if __name__ == "__main__":
    main()


    