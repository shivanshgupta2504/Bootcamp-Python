from machine_data import MENU, resources

coin_value = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

machine_profit = 0.0
# initial_water = resources['water']
# initial_milk = resources['milk']
# initial_coffee = resources['coffee']


def which_coffe():
    coffee = input("What would you like? (Espresso/Latte/Cappuccino): ")
    return coffee.lower()


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${machine_profit}")


def is_resources_sufficient(coffee_chosen):
    milk = resources['milk']
    water = resources['water']
    coffee = resources['coffee']
    if milk < MENU[coffee_chosen]['ingredients']['milk']:
        print("Sorry there is not enough milk.")
        return False
    if water < MENU[coffee_chosen]['ingredients']['water']:
        print("Sorry there is not enough water.")
        return False
    if coffee < MENU[coffee_chosen]['ingredients']['coffee']:
        print("Sorry there is not enough coffee.")
        return False

    return True


def process_payment(quarters, dimes, nickles, pennies):
    total_amount = (quarters * coin_value["quarters"] + dimes * coin_value["dimes"] +
                    nickles * coin_value["nickles"] + pennies * coin_value["pennies"])
    return total_amount


def is_transaction_successful(coffee_chosen, quarters, dimes, nickles, pennies):
    global machine_profit
    received_amount = process_payment(quarters, dimes, nickles, pennies)
    actual_coffe_cost = MENU[coffee_chosen]['cost']

    if received_amount < actual_coffe_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

    if received_amount == actual_coffe_cost:
        machine_profit += received_amount
        return True

    else:
        change = received_amount - actual_coffe_cost
        machine_profit += actual_coffe_cost
        print(f"Here is ${round(change, 2)} dollars in change.")
        return True


def deduct_resources(coffee_chosen):
    resources['milk'] -= MENU[coffee_chosen]['ingredients']['milk']
    resources['water'] -= MENU[coffee_chosen]['ingredients']['water']
    resources['coffee'] -= MENU[coffee_chosen]['ingredients']['coffee']


def make_coffee():
    coffee = which_coffe()
    print_report()
    resource_sufficient = is_resources_sufficient(coffee)
    if resource_sufficient:
        print(f"The cost of {coffee} is {MENU[coffee]['cost']}")
        print("Pay the amount in Quarters/Dimes/Nickles/Pennies")
        quarters = int(input("Quarters: "))
        dimes = int(input("Dimes: "))
        nickles = int(input("Nickles: "))
        pennies = int(input("Pennies: "))
        transaction_successful = is_transaction_successful(coffee, quarters, dimes, nickles, pennies)
        if transaction_successful:
            deduct_resources(coffee)
            print_report()
            print(f"Here is your {coffee.title()}. Enjoy!☕️")
            return "successful"
    else:
        print_report()
        print("Sorry for the inconvenience.")
        return "unsuccessful"


# make_coffee()
def coffee_machine():
    print("Welcome to to Coffee-Machine")
    print("We serve the Best Coffee here...")
    off = False
    while not off:
        is_successful = make_coffee()
        if is_successful == "successful":
            continue
        else:
            if input("Do you want to close the coffee machine? (y/n):") == 'y':
                print_report()
                off = True
            else:
                continue


coffee_machine()






