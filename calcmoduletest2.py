def calculate(): 
    choice =input('''
We will be calcuating overdraft interest:
We will need your interest rate, amount owing, and days owed.
Press 1 to start
Press 2 to quit
''')

    int_rate = int(input('Enter your interest rate: '))
    amount_owing = int(input('Enter your amount owing: '))
    days_owing = int(input('Enter your days owed: '))

# Addition
    if choice == "1":
        print(f'Here is the calculation : {int_rate} / 100 / 365 days * ${amount_owing} * {days_owing}')
        print(f" Your total owing is : ")
        print(int_rate / 100 / 365 * amount_owing * days_owing)
# Subtraction
    elif choice == "2":
        print('Okay, have a great day!')
      
    else:
        print('Enter a valid operator, please run the program again.')
# Add again() function to calculate() function
    again()


def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

# Add again() function to calculate() function
    if calc_again.upper() == 'Y' :
        calculate()
    elif calc_again.upper() == 'N' :
        print('Okay, have a great day!')
    else:
        again()

#Call calculate () outside of the function
calculate()