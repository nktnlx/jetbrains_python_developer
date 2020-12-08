# STAGE 1
import random


# greeting by a main menu
def menu():
    choice = input('''1. Create an account
2. Log into account
0. Exit\n''')
    return choice


# creating a card number + pin and adding this data to a dictionary
def create_account(card_pin=None):
    if card_pin is None:
        card_pin = {}
    default_value = 4 * 10 ** 15  # Issuer Identification number is 400000
    account_num_str = '0'  # starting value
    while len(account_num_str) != 10:  # guarantee to have a 16-digit card number
        account_num_str = ''.join([str(i) for i in random.sample(range(10), 10)])
    card_number = default_value + int(account_num_str)  # creating card number
    pin = ''.join([str(i) for i in random.sample(range(10), 4)])  # creating pin
    card_pin[card_number] = pin  # creating card_number: pin dictionary
    print(f'\nYour card has been created\nYour card number:\n{card_number}\nYour card PIN:\n{pin}\n')
    return card_pin


# printing balance when logged in
def balance():
    while True:
        choice = input('''1. Balance
2. Log out
0. Exit\n''')
        if choice == '1':
            print('\nBalance: 0')
        elif choice == '2':
            print('\nYou have successfully logged out!')
            break
        elif choice == '0':
            return '0'


# checking card number and pin data to log in a user
def log_in(customers_data):
    card = int(input('Enter your card number:\n'))
    pin = input('Enter your PIN:\n')
    if pin == customers_data.get(card):
        print('\nYou have successfully logged in!\n')
        return balance()
    else:
        print('\nWrong card number or PIN!')


# running the script
def main():
    customers_data = {}
    while True:
        user_choice = menu()
        if user_choice == '1':  # create an account
            customers_data = create_account(customers_data)

        elif user_choice == '2':  # log into account
            output = log_in(customers_data)
            if output == '0':
                break

        elif user_choice == '0':  # exit
            print('\nBye!')
            break


main()
