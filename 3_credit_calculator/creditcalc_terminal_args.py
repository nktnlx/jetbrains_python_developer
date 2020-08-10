import argparse
from math import ceil, floor, log

parser = argparse.ArgumentParser(description='Credit Calculator')

parser.add_argument('--type', help='type of your payment: annuity or diff', type=str)
parser.add_argument('--principal', help='principal of your credit', type=int)
parser.add_argument('--periods', help='number of periods', type=int)
parser.add_argument('--interest', help='interest rate of your credit', type=float)
parser.add_argument('--payment', help='your monthly payment', type=float)

args = parser.parse_args()

principal = args.principal
interest = args.interest
payment_type = args.type
periods = args.periods
payment = args.payment

args_lst = [principal, interest, payment_type, periods, payment]


def differential_payment(principal, periods, interest):
    if principal < 0 or periods < 0 or interest < 0:
        return print('Incorrect parameters')

    i = interest / (12 * 100)  # monthly interest rate
    total_paid = 0
    for month_num in range(1, periods + 1):
        diff_payment = (principal / periods) + i * (principal - ((principal * (month_num - 1)) / periods))
        total_paid += ceil(diff_payment)
        print(f'Month {month_num}: paid out {ceil(diff_payment)}')
    overpayment = total_paid - principal
    print(f'\nOverpayment = {ceil(overpayment)}')


def annuity_monthly_payment(principal, periods, interest):
    if principal < 0 or periods < 0 or interest < 0:
        return print('Incorrect parameters')

    i = interest / (12 * 100)  # monthly interest rate
    annuity_payment = ceil(principal * (i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
    overpayment = annuity_payment * periods - principal
    print(f'Your annuity payment = {ceil(annuity_payment)}!')
    print(f'Overpayment = {ceil(overpayment)}')


def principal_calc(payment, periods, interest):
    if payment < 0 or periods < 0 or interest < 0:
        return print('Incorrect parameters')

    i = interest / (12 * 100)  # monthly interest rate
    credit_principal = floor(payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1)))
    overpayment = payment * periods - credit_principal
    print(f'Your credit principal = {credit_principal: .0f}!')
    print(f'Overpayment = {ceil(overpayment)}')


def count_of_month(principal, payment, interest):
    if principal < 0 or payment < 0 or interest < 0:
        return print('Incorrect parameters')

    i = interest / (12 * 100)  # monthly interest rate
    count_of_periods = ceil(log(payment / (payment - i * principal), 1+i))
    overpayment = payment * count_of_periods - principal

    if count_of_periods < 12:
        print(f'You need {int(count_of_periods)} month to repay this credit!')
    elif count_of_periods == 12:
        print('You need 1 year to repay this credit!')
    elif count_of_periods % 12 == 0 and count_of_periods // 12 > 1:
        print(f'You need {count_of_periods // 12} years to repay this credit!')
    else:
        print(f'You need {int(count_of_periods // 12)} years and {int(count_of_periods % 12)} month to repay this credit!')
    print(f'Overpayment = {ceil(overpayment)}')


def choice(input_lst):
    count = 0
    for parameter in input_lst:
        if parameter is not None:
            count += 1

    if count != 4 or input_lst[2] not in ('diff', 'annuity'):
        return print('Incorrect parameters')

    if input_lst[2] == 'diff':
        differential_payment(principal, periods, interest)

    if input_lst[2] == 'annuity':
        if input_lst[3] is not None and input_lst[0] is not None:
            annuity_monthly_payment(principal, periods, interest)
        if input_lst[3] is not None and input_lst[4] is not None:
            principal_calc(payment, periods, interest)
        if input_lst[4] is not None and input_lst[0] is not None:
            count_of_month(principal, payment, interest)


choice(args_lst)
