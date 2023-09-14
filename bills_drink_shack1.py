"""
 Filename: bills_drink_shack1.py
 Author: Bill Edwards
 Created: 09/03/2023
 Purpose: POS program top down
"""
#cost of drinks for the customer
COST_DRINKS = 2.50

#TODO get int for drinks sold
num_of_drinks_sold = int(input("How number of drinks: "))

#TODO: Calculate cost of drinks purchased
total_sale = num_of_drinks_sold * COST_DRINKS

#TODO: display total cost for customer
print(f"Your total today is ${total_sale:,.2f}")