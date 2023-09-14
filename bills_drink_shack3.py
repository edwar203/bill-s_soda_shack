"""
 Filename: bills_drink_shack3.py
 Author: Bill Edwards
 Created: 09/03/2023
 Purpose: POS program OOP
"""
#cost of drinks for the customer
COST_DRINKS = 2.50


class BillsDrinks:
    def __init__(self):
        self.get_input()
        self.calculate()
        self.display()

    def get_input(self):
        #TODO get int for drinks sold
        self.num_of_drinks_sold = int(input("How number of drinks: "))

    def calculate(self):
        #TODO: Calculate cost of drinks purchased
        self.total_sale = self.num_of_drinks_sold * COST_DRINKS

    def display(self):
        #TODO: display total cost for customer
        print(f"Your total today is ${self.total_sale:,.2f}")

bills_drinks = BillsDrinks()