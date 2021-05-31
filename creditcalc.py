import argparse
import math
import sys


def calc_months(principal, m_payment, annual_interest):
    if principal < 0 or m_payment < 0 or annual_interest < 0:
        print('Incorrect parameters')
        return
    i = annual_interest / (12 * 100)
    x = (m_payment / (m_payment - i * principal))
    base = 1 + i
    n = math.ceil(math.log(x, base))
    y = n // 12
    m = n % 12
    overpayment = abs(m_payment * (y * 12 + m) - principal)
    if y == 0:
        print(f'It will take {m} months to repay this loan!\nOverpayment= {round(overpayment)}')
    elif m == 0:
        print(f'It will take {y} years to repay this loan!\nOverpayment= {round(overpayment)}')
    else:
        print(f'It will take {y} years and {m} months to repay this loan!\nOverpayment= {overpayment}')


def calc_annuity_payment(principal, periods, annual_interest):
    if principal < 0 or periods < 0 or annual_interest < 0:
        print('Incorrect parameters')
        return
    i = annual_interest / (12 * 100)
    m_payment = math.ceil(principal * i * (1 + i) ** periods / ((1 + i) ** periods - 1))
    overpayment = m_payment * periods - principal
    print(f'Your monthly payment = {m_payment}!\nOverpayment= {overpayment:.0f}')


def calc_loan_principal(payment, periods, annual_interest):
    if payment < 0 or periods < 0 or annual_interest < 0:
        print('Incorrect parameters')
        return
    i = annual_interest / (12 * 100)
    loan = math.floor(payment / (i * (1 + i) ** periods / ((1 + i) ** periods - 1)))
    print(f'Your loan principal = {loan}!')
    overpayment = (payment * periods) - loan
    print(f'Overpayment= {overpayment:.0f}')


def calc_diff_payments(principal, periods, annual_interest):
    if principal < 0 or periods < 0 or annual_interest < 0:
        print('Incorrect parameters')
        return
    total_amount_repaid = 0
    for current_month in range(1, periods + 1):
        mon_repayment = math.ceil(
            (principal / periods) + annual_interest / 1200 * (principal - (principal * (current_month - 1)) / periods))
        total_amount_repaid += mon_repayment
        print(f"Month {current_month}: payment is {mon_repayment}")
    overpayment = total_amount_repaid - principal

    print(f'\nOverpayment= {overpayment:.0f}')


parser = argparse.ArgumentParser()
parser.add_argument('--type',
                    type=str)
parser.add_argument('--payment',
                    type=float)
parser.add_argument('--principal',
                    type=float)
parser.add_argument('--periods',
                    type=int)
parser.add_argument('--interest',
                    type=float)
args = parser.parse_args()

if len(sys.argv) < 5:
    print('Incorrect parameters')
    exit()

if args.type == 'diff':
    if args.principal and args.periods and args.interest:
        calc_diff_payments(args.principal, args.periods, args.interest)
    else:
        print('Incorrect parameters')
        exit()

elif args.type == 'annuity':
    if args.principal and args.periods and args.interest:
        calc_annuity_payment(args.principal, args.periods, args.interest)
    elif args.principal and args.payment and args.interest:
        calc_months(args.principal, args.payment, args.interest)
    elif args.periods and args.payment and args.interest:
        calc_loan_principal(args.payment, args.periods, args.interest)
    else:
        print('Incorrect parameters')
        exit()
else:
    print('Incorrect parameters')
    exit()
