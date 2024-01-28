# This program asks the user to repeatedly enter a number until they enter -1.
# When they enter -1, it calculates the average of all their previous attempts.

num = int(input("Enter a number: "))

# This variable stores the sum of the numbers entered.
total = 0

#This variable stores the number of attempts they have made.
attempts = 0

while num != int(-1):
    total += num
    attempts +=1
    num = int(input("Try again: "))

if num == int(-1):
    average = total/attempts
    print("The mean average of your attempts is " + str(average))
