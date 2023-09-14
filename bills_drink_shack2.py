"""
 Filename: bills_drink_shack2.py
 Author: Bill Edwards
 Created: 09/03/2023
 Purpose: POS program functional
"""
#cost of drinks for the customer
COST_DRINKS = 2.50


def main():
    num_of_drinks_sold = get_input()
    total_sale = calculate(num_of_drinks_sold)
    display(total_sale)

def get_input():
    #TODO get int for drinks sold
    num_of_drinks_sold = int(input("How number of drinks: "))
    return num_of_drinks_sold

def calculate(num_of_drinks_sold):
    #TODO: Calculate cost of drinks purchased
    total_sale = num_of_drinks_sold * COST_DRINKS
    return total_sale

def display(total_sale):
    #TODO: display total cost for customer
    print(f"Your total today is ${total_sale:,.2f}")

if __name__ == '__main__':
    main()