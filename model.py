import json

def create_new_account():
    data = load()
    account_num = int(len(data) + 1)
    data[account_num] = {"user_name": "temp name", "pin_code": "temp_pin_code", "balance": 0}
    save(data)
    return account_num

def add_name(by_account_num, new_user_name):
    data = load()
    data[str(by_account_num)]["user_name"] = new_user_name
    save(data)

def add_pin_code(by_account_num, new_pin_code):
    data = load()
    data[str(by_account_num)]["pin_code"] = new_pin_code
    save(data)

def get_balance(by_account_num):
    data = load()
    account_balance = data[by_account_num]["balance"]
    # print(account_balance)
    return account_balance

def add_funds(by_user_account, add_amount):
    data = load()
    account_balance = data[by_user_account]["balance"]
    data[str(by_user_account)]["balance"] = int(account_balance) + int(add_amount)
    save(data)

def withdraw_funds(by_user_account, subtract_amount):
    data = load()
    account_balance = data[by_user_account]["balance"]
    data[str(by_user_account)]["balance"] = int(account_balance) - int(subtract_amount)
    save(data)

def get_account_details(account_num):
    data = load()
    user_details = data[str(account_num)]
    return user_details

def load():
    with open('atm.json', 'r') as f_object:
        data = json.load(f_object)
    return data

def save(data):
    with open('atm.json', 'w') as f_object:
        json.dump(data, f_object, indent=2)