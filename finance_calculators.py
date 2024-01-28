#This program can calculate interest earned from an investment, or amount payable
#per month on a home loan, based on user input

import math

print("investment \t - to calculate the amount of interest that you'll earn on your investment")
print("bond \t\t - to calculate the amount you'll have to pay on the home loan")
print()
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

#This prints an error message if the user emters an invalid input from the investment
# menu and asks them to re-enter their choice until they enter a valid answer
while choice.lower() != "investment" and choice.lower() != "bond":
    print("That is not a valid entry, please try again.")
    choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

#This section calculates interest on investments
if choice.lower() == "investment":
    deposit = float(input("Enter how much money you will deposit: "))
    interest_rate = float(input("Enter the interest rate not including the percentage symbol: "))
    percentage = interest_rate/100
    years = int(input("Enter how many years you will invest for: "))
    interest = input("Will the interest be [simple] or [compound]: ")

    #This code works out the total value with simple interest and prints to 2 decimal places
    if interest.lower() == "simple":
        answer = round(deposit*(1+percentage*years))
        print("The total amount including interest will be £" + str(answer))
    #This code works out the total value with compound interest and prints to 2 decimal places    
    elif interest.lower() == "compound":
        answer = round(deposit*math.pow((1+percentage),years),2)
        print("The total amount including interest will be £" + str(answer))

#This section calculates interest on home loans
elif choice.lower() == "bond":
    house_value = float(input("Enter the current value of the house: "))
    interest_rate = float(input("Enter the interest rate not including the percentage symbol: "))
    monthly_percentage = (interest_rate/100)/12
    months = int(input("Enter the number of months you will take to repay the loan: "))
    repayment = round((monthly_percentage*house_value)/(1-(1+monthly_percentage)**(-months)),2)
    print("The amount you will have to pay each month is £" + str(repayment))
