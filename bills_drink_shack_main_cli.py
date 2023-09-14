"""
"""
import bills_drink_shack_class as drink

def get_input():
        #TODO get int for drinks sold
        num_of_drinks = int(input("How many drinks: "))
        return num_of_drinks


def display():
#TODO: display total cost for customer
        num_of_drinks = bills_drinks.num_of_drinks
        total_sale = bills_drinks.total_sale
        print(f"Number of drinks: {num_of_drinks}")
        print(f"Your total today is ${total_sale:,.2f}")

bills_drinks = drink.BillsDrinks()

num_of_drinks = get_input()

bills_drinks.calculate(num_of_drinks)

display()

