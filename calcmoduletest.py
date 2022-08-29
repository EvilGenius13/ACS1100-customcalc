from os import _exit


beginning_input = input('''
Hi, are you ready to calculate your overdraft interest?
We will need you to input your interest rate, amount owing, and days owing.
Press 1 to Start or 2 to Quit.
''')

if beginning_input == '1':
    interest_rate = float(input(f'Enter the interest rate: '))
    amount_owing = float(input(f'Enter the amount owing: '))
    days_owing = float(input(f'Enter the days owing: '))
    int_owed = interest_rate / 100 / 365 * amount_owing * days_owing
    print(f'Here is the calculation : {interest_rate} percent / 100 / 365 days * ${amount_owing} * {days_owing} days')
    print(f'You will owe {int_owed}')
elif beginning_input == '2':
    print(f'No problem, see you next time!')
    