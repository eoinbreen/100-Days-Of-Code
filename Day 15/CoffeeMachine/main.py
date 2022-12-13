from data import resources
from data import coins
from data import MENU


def print_resources():
    """Prints a report of what resources the user has"""
    for key in resources:
        print(f"{key} - {resources[key]}")


def take_resources(drink):
    resources["money"] -= MENU[drink]["cost"]
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]


def check_resources(drink):
    if resources["money"] < MENU[drink]["cost"]:
        print("That's not enough money. Money refunded.")
        resources["money"] = 0
        return False
    elif resources["water"] < MENU[drink]["ingredients"]["water"]:
        return False
    elif resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        return False
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        return False
    else:
        print(f"Here is your {drink}, enjoy!")
        take_resources(drink)
        return True


def calculate_money(num_pennies, num_nickles, num_dimes, num_quarters):
    """Calculates the amount of money the user has after they have inputted their coins"""
    pennies = coins["penny"] * num_pennies
    nickles = coins["nickle"] * num_nickles
    dimes = coins["dime"] * num_dimes
    quarters = coins["quarter"] * num_quarters
    total_money = pennies + nickles + dimes + quarters

    return total_money


available_drinks = []
for key in MENU:
    available_drinks.append(key)

print(available_drinks)
# TODO: Ask the user what they would like

# TODO: Ask the user to input money into the machine

# TODO: Turn off the machine


resources["money"] = calculate_money(12, 12, 12, 12)
check_resources("latte")
print_resources()
