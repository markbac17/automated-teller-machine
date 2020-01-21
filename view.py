def get_account():
    print()
    user_account_num = input("Enter account number: ")
    user_input_pin = input("Enter pin: ")
    user_login_details = [user_account_num, user_input_pin]
    return user_login_details

def show_menu():
    print()
    print("Welcome to Mark's Savings Bank")
    print("Select one of the choices below:")
    print("1. Create new account.")
    print("2. Log in to account.")
    print("3. Quit")
    # return input("Enter choice: ")

def show_user_menu():
    print()
    # print("Welcome to Users menu")
    print("Select one of the choices below:")
    print("1. Check balance.")
    print("2. Withdraw funds.")
    print("3. Deposit funds.")
    print("4. Sign out.")
    # return input("Enter choice: ")

def new_account():
    print()
    print("Create new account")
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    pin_code = input("Enter new four digit pin code: ")
    print()
    user_details = [f_name, l_name, pin_code]
    return user_details

def show_balance(current_balance):
    print()
    print("Your current balance is: " + str(current_balance))

def add_funds():
    print()
    return input("How much would you like to deposit? " )

def subtract_funds():
    print()
    return input("How much would you like to take out? " )

def display_user_details(account_details):
    print()
    print("User name: " + account_details["user_name"])
    print("Hello, " + account_details["user_name"] + " (account num)")

def get_input():
    return input("Enter choice: ")

def bad_input():
    print("Option not available, please retry.")