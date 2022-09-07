actual_pin = 1234
account_balance = 100


def pin_inquiry():
    user_pin = int(input("Please enter your pin code: "))
    return user_pin == actual_pin


def insufficient_funds(Exception):
    pass

def withdrawal(withdrawal_amount):
    new_balance = account_balance - withdrawal_amount
    return new_balance


def run():
    i = 3
    while i > 0:
        if pin_inquiry() == True:
            i = 0
            withdrawal_amount = int(input("Please enter withdrawal amount: "))
            try:
                if withdrawal_amount > account_balance:
                    raise insufficient_funds
            except:
                print("Insufficient funds.")
            else:
                balance = withdrawal(withdrawal_amount)
                print(f"Withdrawal successful. Your balance is {balance}.")
            finally:
                print("Thank you for using Simple ATM.")
        else:
            print(f"The pin is incorrect. You have {i - 1} more attempts.")
            i = i - 1
            if i == 0:
                print("Your account has been locked.")

