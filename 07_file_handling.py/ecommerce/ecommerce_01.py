# Requirements
# Ask user to login or register
# If register ask for username,password and usertype and store the data in a file the format of storing the user data can change because of extra field usertype(buyer/seller)
# If login ask for username and password and check if it matches with any data, if it matches then check the usertype of the data and if the type is buyer give hime option of view product, purchase product,view bill. If the type is seller give him option of add product, view his/her product, view bills
# If the seller user provides option for add product, ask him/her for product name, description, price and the store this data along with user as the seller key value as a json in a file
# If the buyer user provides option for view product, print all the product from the file where product data is stored


import json

def purchaseProduct(usertype,username):
    if usertype == 'buyer':
        f = open('E:/#LearningPython/07_file_handling.py/ecommerce/product.txt','r')
        product_data = f.read()
        list_product_data = product_data.split('-')
        print("Available Products:")
        for i, product in enumerate(list_product_data, start=1):
            if product:
                product_dict_data = json.loads(product)
                print(f"{i}. {product_dict_data['name']} - ${product_dict_data['price']}")

        choice = int(input("Enter the number of the product you want to purchase: ")) - 1
        if 0 <= choice < len(list_product_data):
            # converting into dict
            selected_product = json.loads(list_product_data[choice])
            selected_product['buyer'] = username
            print(f"You have purchased: {selected_product['name']} for ${selected_product['price']}")
            f = open('E:/#LearningPython/07_file_handling.py/ecommerce/purchase_product.txt','a')
            # converting dict to string 
            seleted_product_in_string = json.dumps(selected_product)
            f.write(seleted_product_in_string +'-')
            f.close()



def view_bill(username):
    total = 0.0
    f = open('E:/#LearningPython/07_file_handling.py/ecommerce/purchase_product.txt','r')
    purchase_datas = f.read()
    f.close()
    list_purchase_datas = purchase_datas.split('-')

    for data in list_purchase_datas:
        if data.strip():
            dict_data = json.loads(data)
            if username == dict_data.get('buyer'):
                print(f'Product name: {dict_data.get('name')}')
                print(f'Product price: {dict_data.get('price')}')
                total = total + float(dict_data.get('price'))

            else:
                if username == dict_data.get('seller'):
                    print(f'Product name: {dict_data.get('name')}')
                    print(f'Product price: {dict_data.get('price')}')
                    total = total + float(dict_data.get('price'))

    print(f'Total: {total}')


              
      
def usertypeFun(usertype, username):
    if usertype == 'buyer':
        print('''
            Enter the option from below :
            1. View product
            2. Purchase product
            3. View bill
            ''')
        user_option_choice = input()
        if user_option_choice == '1':
            view_product()

        elif user_option_choice == '2':
            purchaseProduct(usertype,username)
        elif user_option_choice == '3':
            view_bill(username)

        else:
            print('Invalid options, please choose correct option')
            usertypeFun(usertype,username)
        

    elif usertype == 'seller':
        print('''
            Enter the option from below :
            1. Add product
            2. View your product
            3. View your product bill''')
        user_option_choice = input()
        if user_option_choice == '1':
            add_product(username)
        elif user_option_choice == '2':
            view_your_product(username)
        elif user_option_choice == '3':
            view_bill(username)

    else:
        print('''
              Invalid usertypes
              Please Login again
              ''')

        login()


def add_product(seller):
    product_name = input('Enter the product name : ')
    product_price = input('Enter the product price : ')
    product_description = input('Enter the product description : ')

    product_dict_data = {'name':product_name,'description':product_description,'price':product_price,'seller':seller}

    json_product_data = json.dumps(product_dict_data)

    f = open('E:/#LearningPython/07_file_handling.py/ecommerce/product.txt','a')

    f.write(json_product_data +'-')

    f.close()

def view_your_product(seller):
    f = open('E:/#LearningPython/07_file_handling.py/ecommerce/product.txt','r')
    product_data = f.read()
    f.close()

    list_product_data = product_data.split('-')

    for product in list_product_data:
        if product != '':
            product_dict_data = json.loads(product)
            if product_dict_data.get('seller') == seller:
                print(product_dict_data)



def view_product():
    f = open('E:/#LearningPython/07_file_handling.py/ecommerce/product.txt','r')

    product_data = f.read()

    f.close()

    list_product_data = product_data.split('-')

    for product in list_product_data:
        print(product)


def register():
    username = input('Enter your username : ')
    password = input('Enter your password : ')
    usertype = input('Enter your usertype(buyer/seller) : ').lower()

    user_data = {"username":username,"password":password,"usertype":usertype}

    f = open('E:/#LearningPython/07_file_handling.py/ecommerce/userdata.txt','a')

    json_user_data = json.dumps(user_data) # To convert dictionary data to json data

    f.write(json_user_data + '-') # Writing json data in the file

    f.close()
    print('Register Sucessfully')

def login():
    username = input('Enter your username : ')
    password = input('Enter your password : ')

    f = open('E:/#LearningPython/07_file_handling.py/ecommerce/userdata.txt','r')

    user_datas = f.read()

    f.close()

    list_user_datas = user_datas.split('-')
    user_login = False
    usertype = None
    for i in list_user_datas:
        if i != '':
            dict_data = json.loads(i)
            if username == dict_data.get('username') and dict_data.get('password') == password:
                user_login = True
                usertype = dict_data.get('usertype')

    if user_login == True:
        print('Login successfull!')
        usertypeFun(usertype=usertype, username=username)
    
    else:
        print('Invalid credentials')


def main():
    user_choice = input('Do you want to login or register? ').lower().strip()

    if user_choice == 'register':
        register()
    elif user_choice == 'login':
        login()
    else:
        print('Invalid choice. Please try again.')

if __name__ == "__main__":
    main()