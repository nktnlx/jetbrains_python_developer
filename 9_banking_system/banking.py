# STAGE 1
# import random


# greeting by a main menu
# def menu():
#     choice = input('''1. Create an account
# 2. Log into account
# 0. Exit\n''')
#     return choice
#
#
# # creating a card number + pin and adding this data to a dictionary
# def create_account(card_pin=None):
#     if card_pin is None:
#         card_pin = {}
#     default_value = 4 * 10 ** 15  # Issuer Identification number is 400000
#     account_num_str = ''.join([str(i) for i in random.sample(range(10), 10)])
#     card_number = default_value + int(account_num_str)  # creating card number
#     pin = ''.join([str(i) for i in random.sample(range(10), 4)])  # creating pin
#     card_pin[card_number] = pin  # creating card_number: pin dictionary
#     print(f'\nYour card has been created\nYour card number:\n{card_number}\nYour card PIN:\n{pin}\n')
#     return card_pin
#
#
# # printing balance when logged in
# def balance():
#     while True:
#         choice = input('''1. Balance
# 2. Log out
# 0. Exit\n''')
#         if choice == '1':
#             print('\nBalance: 0')
#         elif choice == '2':
#             print('\nYou have successfully logged out!')
#             break
#         elif choice == '0':
#             return '0'
#
#
# # checking card number and pin data to log in a user
# def log_in(customers_data):
#     card = int(input('Enter your card number:\n'))
#     pin = input('Enter your PIN:\n')
#     if pin == customers_data.get(card):
#         print('\nYou have successfully logged in!\n')
#         return balance()
#     else:
#         print('\nWrong card number or PIN!')
#
#
# # running the script
# def main():
#     customers_data = {}
#     while True:
#         user_choice = menu()
#         if user_choice == '1':  # create an account
#             customers_data = create_account(customers_data)
#
#         elif user_choice == '2':  # log into account
#             output = log_in(customers_data)
#             if output == '0':
#                 break
#
#         elif user_choice == '0':  # exit
#             print('\nBye!')
#             break
#
#
# main()


# STAGE 2
import random


# greeting by a main menu
def menu():
    choice = input('''1. Create an account
2. Log into account
0. Exit\n''')
    return choice


# creating a card number + pin and adding this data to a dictionary
# Luhn Algorithm applied to generate card number
def create_account(card_pin=None):
    if card_pin is None:
        card_pin = {}
    # creating a random 15-digit number with a pre-defined Issuer Identification number
    account_num = [4, 0, 0, 0, 0, 0]  # Issuer Identification number is 400000
    account_num.extend([int(i) for i in random.sample(range(10), 9)])

    # applying Luhn Algorithm to check the number and produce a check sum
    # multiply every odd digits by 2
    account_num_by2 = [account_num[i] * 2 if i % 2 == 0 else account_num[i] for i in range(len(account_num))]
    # subtract 9 to numbers over 9
    account_num_minus9 = [num - 9 if num > 9 else num for num in account_num_by2]
    # summing numbers
    sum_of_numbers = sum(account_num_minus9)

    # finding the last digit(our checksum)
    # if the received number is divisible by 10 with the remainder equal to zero, then this number is valid
    last_digit = 0
    for i in range(10):
        if (sum_of_numbers + i) % 10 == 0:
            last_digit = i
    account_num.append(last_digit)  # adding checksum number as a last digit to our card number

    # creating card number and pin
    account_num_str = ''.join([str(i) for i in account_num])
    card_number = int(account_num_str)
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

































