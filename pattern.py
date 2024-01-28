# This code will create a pattern of stars increasing from one to five
# and decreasing back to one.

stars = ""

# The for loop covers each of the 9 lines in the pattern of stars.
for i in range(0, 10):
    # This if statement adds a star to each of the first 5 iterations
    if i <= 4:
        stars += "*"
        print(stars)
    # The else statement removes a star from the last 5 iterations    
    else:
        stars = stars.replace("*", "", 1)
        print(stars)
        