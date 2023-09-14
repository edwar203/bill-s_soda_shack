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

    def get_num_drinks(self):
        #validation
        if self._num_of_drinks > 0:
            return self._num_of_drinks
        else:
            return "You must order at least one drink!"
    
    def get_total_sale(self):
        return self._total_sale

    def calculate(self, num_of_drinks):
        #TODO: Calculate cost of drinks purchased
        self._num_of_drinks = num_of_drinks
        self._total_sale = self._num_of_drinks * COST_DRINKS

