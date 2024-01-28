'''
This program will find the total value of the stock from a cafe menu
by multiplying then number of each item by the price of the item,
using lists and dictionaries to store the information.
'''

# A list storing the name of each item on the menu
menu = ["Matcha Latte", "Cappuccino", "Hot Chocolate", "Coffee Cake",
         "Brownie", "Cinnamon Bun"]

# A dictionary storing the number of each menu item currently in stock
stock = {"Matcha Latte": 5,
         "Cappuccino": 2,
         "Hot Chocolate": 9,
         "Coffee Cake": 6,
         "Brownie": 3,
         "Cinnamon Bun": 8
        }

# A dictionary storing the price of each single menu item
price = {"Matcha Latte": 3.50,
         "Cappuccino": 2.90,
         "Hot Chocolate": 2.75,
         "Coffee Cake": 4.00,
         "Brownie": 3.20,
         "Cinnamon Bun": 3.00
        }

# This variable will store the total stock value once the number in
# stock is multiplied by the price
total_value = 0

'''
This for loop iterates through each item in the cafe menu.
When the item matches the key in each of the dictionaries, it will
take the equivalent dictionary value and multiply them,
then add the total to the total stock value.
'''
for x in menu:
    total_value += (stock[x])*(price[x])

# This prints the final total
print(f"Your total stock value is £{total_value}.")