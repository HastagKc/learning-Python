# Task
# First ask the user to login or register
# If register ask for username and password then store that data in a file
# Else if login ask for username and password then compare it with the data in the file where user data is stored
# While login If the user is a valid user then ask him/her for three options : check balance, add balance
# Add balance : ask the amount to add then add the amount with balance as a dictionary {'ram':23000}-{'ram':50000} store this data in a file
# Check blanace : read the file where amount is being stored then print the summation of every data which matches with user's username
# Extra requirement : If the user has not balance during check balance the print will be 0, instead of 0 only print You should store certain amount using add balance

import json

def check_balance(username):
    f = open('E:/#LearningPython/07_file_handling.py/accounting2/user_amount.txt','r')

    file_data = f.read()

    f.close()

    list_user_account_data = file_data.split('-')

    user_total_amount = 0

    for i in list_user_account_data:
        if i != '':
            dict_user_account_data = json.loads(i)
            if username in dict_user_account_data:
                user_amount = dict_user_account_data.get(username)
                int_user_amount = int(user_amount)
                user_total_amount += int_user_amount

    if user_total_amount == 0:
        print('You should store certain amount using add balance')

    else:
        print(f'Your tatal balance is: {user_total_amount}')


# checking is provided value is numerical or not 
def is_numerical(input_str):
    try:
        float(input_str)  
        return True
    except ValueError:
        return False

def add_balance(username):
    user_amount = input('Enter the amount to store in your account : ')
    if is_numerical(user_amount):
        user_amount_data = {username:user_amount}
        json_user_amount_data = json.dumps(user_amount_data)
        f = open('E:/#LearningPython/07_file_handling.py/accounting2/user_amount.txt','a')

        f.write(json_user_amount_data + '-')

        f.close()
        print(f'{user_amount} is add sucessfully in your account.')
    else:
        print('Please enter valid input ')


def register():
    username = input('Enter your username : ')
    password = input('Enter your password : ')

    user_data = {username:password}

    f = open('E:/#LearningPython/07_file_handling.py/accounting2/user_data.txt','a')

    json_user_data = json.dumps(user_data) # To convert dictionary data to json data

    f.write(json_user_data + '-') # Writing json data in the file

    f.close()
    print('Register sucessfully')

def login():
    username = input('Enter your username : ')
    password = input('Enter your password : ')

    f = open('E:/#LearningPython/07_file_handling.py/accounting2/user_data.txt','r')

    user_datas = f.read()

    f.close()

    list_user_datas = user_datas.split('-')
    user_login = False
    for i in list_user_datas:
        if i != '':
            dict_data = json.loads(i)
            if username in dict_data and dict_data.get(username) == password:
                user_login = True


    if user_login == True:
        print('Login successfull!')
        user_accont_choice = input('Do you want to :\n 1. check balance \n 2. add balance \n').strip()
        if user_accont_choice == '1':
            check_balance(username)
        elif user_accont_choice == '2':
            add_balance(username)

    else:
        print('Invalid credentials')


user_choice = input('Do you want to: \n1: login \n2: register? \n').lower().strip()

if user_choice == 'register' or user_choice == '1':
    login()
elif user_choice == 'login' or user_choice == '2':
    register() 
else:
    print('Invalid input!')