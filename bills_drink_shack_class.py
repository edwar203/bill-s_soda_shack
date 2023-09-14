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
        pass

    def calculate(self, num_of_drinks):
        #TODO: Calculate cost of drinks purchased
        self.num_of_drinks = num_of_drinks
        self.total_sale = num_of_drinks * COST_DRINKS

