import model
import view

def run():
    main_menu()

def user_menu(user_account):
    while True:
        view.show_user_menu()
        selection = view.get_input()
        if selection == "4":
            return
        elif selection == "1":
            view.show_balance(model.get_balance(user_account))
        elif selection == "2":
            print("wit")
            withdraw_amount = int(view.subtract_funds())
            current_balance = int(model.get_balance(user_account))
            if withdraw_amount > current_balance:
                print("insufficient funds")
            else:
                model.withdraw_funds(user_account, withdraw_amount)

        elif selection == "3":
            add_amount = view.add_funds()
            model.add_funds(user_account, add_amount)
        else:
            view.bad_input()

def main_menu():
    while True:
        view.show_menu()
        selection = view.get_input()
        if selection == "3":
            return
        elif selection == "1":
            new_user = view.new_account()
            new_account_num = model.create_new_account()
            new_user_full = new_user[0] + " " + new_user[1]
            model.add_name(new_account_num, new_user_full)
            model.add_pin_code(new_account_num, new_user[2])

        elif selection == "2":
            account_num = view.get_account()
            account_details = model.get_account_details(account_num[0])
            if str(account_num[1]) == str(account_details["pin_code"]):
                view.display_user_details(account_details)
                user_menu(account_num[0])
            else:
                view.bad_input
                return
            
        else:
            view.bad_input()

if __name__ == "__main__":
    run()