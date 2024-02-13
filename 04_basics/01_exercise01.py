# 1. Bank Account Management System:
# -> Create a class representing a bank account with methods to deposit, withdraw, and display balance.

# class BankAccount:
#     def __init__(self, account_number, account_holder, total_balance=0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = total_balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited {amount} successfully.")
#         else:
#             print("Invalid deposit amount. Please enter a positive number.")

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrawn {amount} successfully.")
#         else:
#             print("Invalid withdrawal amount. Please check your balance and try again.")

#     def display_balance(self):
#         print(f"Account Holder: {self.account_holder}")
#         print(f"Account Number: {self.account_number}")
#         print(f"Current Balance: {self.balance}")

# # Example usage:
# account1 = BankAccount("123456789", "Alice")
# account1.deposit(1000)
# account1.withdraw(500)
# account1.display_balance()


# requirement account no 
# account holder 
# initial balance 
# deposite_amount 
# withdraw amount 
class Bank:
    def __init__(self, account_no, account_holder, total_balance=0):
        self.account_no = account_no
        self.account_holder = account_holder
        self.total_balance = total_balance

    def deposit(self, deposite_amount):
        if deposite_amount > 0:
            self.total_balance += deposite_amount
            print(f"{deposite_amount} has been successfully deposited into your account")
        else:
            print("Invalid amount, please enter a valid amount")

    def withdraw(self, withdraw_amount):
        if self.total_balance >= withdraw_amount > 0:
            self.total_balance -= withdraw_amount
            print(f"{withdraw_amount} has been successfully withdrawn from your account")
        else:
            print("Insufficient balance or invalid amount")

    def display_details(self):
        print(f"Your account no: {self.account_no}")
        print(f"Your account holder: {self.account_holder}")
        print(f"Your Total balance: {self.total_balance}")

# Example usage:
account1 = Bank(account_holder="ks", account_no="123456789")
account1.deposit(25000)
account1.display_details()

account1.withdraw(10000)
account1.display_details()
