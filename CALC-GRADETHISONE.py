# I am pretty happy with how this turned out! - but also happy for feedback
# MY CALCULATOR TEST - This is to calculate overdraft interest 

print("We will now calculate the overdraft interest you owe.\nPlease input your interest rate, amount owing, and days owing")
# This is the annual interest rate which gets converted to a number automatically
# ex - 5% will become 0.05
interest_rate = input("Enter the interest rate as a number : ")
interest_rate = float(interest_rate)
interest_rate = interest_rate / 100

# This is the amount owing in dollars
amount_owing = input("Enter the amount owing in dollars (no cents): ")
amount_owing = int(amount_owing)

#This is the amount of days owing
days_owing = input("Enter the amount of days you will borrow money for : ")
days_owing = int(days_owing)

# The calculation should be as follows (with example) :
# interest rate (0.05) / 365 (days in a year) = 0.00013698630137
# * amount owing (10,000) = 1.36986301369863 (this would be interest per day)
# * amount of days owing (30) = 41.095890410958901
def daily_interest_calc(interest_rate_input, amount_input, days_owing_input):
    total_owing = interest_rate_input / 365 * amount_input * days_owing_input
    print(f" Here is the calculation {interest_rate_input} / 365 * ${amount_input} * {days_owing_input} = ")
    return total_owing
    
final_calc = daily_interest_calc
print(final_calc(interest_rate, amount_owing, days_owing))
# this is to explain the rate as a percentage again when it's printed
interest_rate_reconverted = interest_rate * 100

print(f"That is the total amount of interest you will pay on ${amount_owing} after {days_owing} days at {interest_rate_reconverted} percent")
