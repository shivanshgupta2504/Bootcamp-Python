from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
# is_on = True
#
# while is_on:
#     options = menu.get_items()
#     choice = input(f"What would you like? ({options}): ")
#     if choice == 'off':
#         is_on = False
#     elif choice == 'report':
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
#         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
#             coffee_maker.make_coffee(drink)


def coffee_machine():
    """Initialises the coffee machine"""
    print("Welcome to to Coffee-Machine")
    print("We serve the Best Coffee here...")
    off = False
    while not off:
        choice = input(f"What would you like? ({menu.get_items()}): ")
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                coffee_maker.report()
                money_machine.report()
            else:
                print("Order Again!")
                continue
        else:
            print("Sorry for the inconvenience.")
            if input("Do you want to close the coffee machine? (y/n):") == 'y':
                coffee_maker.report()
                money_machine.report()
                off = True
            else:
                continue


coffee_machine()





