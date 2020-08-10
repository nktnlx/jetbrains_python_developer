import sys
from math import log
from math import ceil

calc_type = input('''What do you want to calculate?
type "n" - for count of months,
type "a" - for annuity monthly payment,
type "p" - for credit principal:
''')


def count_of_month():
    try:
        credit_principal = float(input('\nEnter credit principal:\n'))
        monthly_payment = float(input('Enter monthly payment:\n'))
        credit_interest = float(input('Enter credit interest:\n'))

        i = credit_interest / (12 * 100)  # monthly interest rate
        count_of_periods = ceil(log(monthly_payment / (monthly_payment - i * credit_principal), 1+i))

        if count_of_periods < 12:
            print(f'You need {int(count_of_periods)} month to repay this credit!\n')
        elif count_of_periods == 12:
            print('You need 1 year to repay this credit!\n')
        else:
            print(f'You need {int(count_of_periods // 12)} years and {int(count_of_periods % 12)} month to repay this credit!\n')
        sys.exit('Thanks for using the credit calculator.')

    except ValueError:
        print('\nSomething went wrong.. Try another input parameters')
        count_of_month()


def annuity_monthly_payment():
    try:
        credit_principal = float(input('Enter credit principal:\n'))
        count_of_periods = int(input('Enter count of periods:\n'))
        credit_interest = float(input('Enter credit interest:\n'))

        i = credit_interest / (12 * 100)  # monthly interest rate
        annuity_payment = credit_principal * (i * (1 + i) ** count_of_periods) / ((1 + i) ** count_of_periods - 1)

        print(f'Your annuity payment = {ceil(annuity_payment)}!\n')
        sys.exit('Thanks for using the credit calculator.')

    except ValueError:
        print('\nSomething went wrong.. Try another input parameters')
        count_of_month()


def credit_principal_calc():
    try:
        monthly_payment = float(input('Enter monthly payment:\n'))
        count_of_periods = int(input('Enter count of periods:\n'))
        credit_interest = float(input('Enter credit interest:\n'))

        i = credit_interest / (12 * 100)  # monthly interest rate
        credit_principal = monthly_payment / ((i * (1 + i) ** count_of_periods) / ((1 + i) ** count_of_periods - 1))

        print(f'Your credit principal = {credit_principal: .0f}!\n')
        sys.exit('Thanks for using the credit calculator.')

    except ValueError:
        print('\nSomething went wrong.. Try another input parameters')
        count_of_month()


def choice(user_choice):
    if user_choice == 'n':
        count_of_month()
    if user_choice == 'a':
        annuity_monthly_payment()
    if user_choice == 'p':
        credit_principal_calc()
    else:
        print('\nBe careful, when typing your answer! Available options are: n, a, p')
        calc_type = input('Please, enter a valid value: ')
        choice(calc_type)


choice(calc_type)
