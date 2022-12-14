from data import resources
from data import coins
from data import MENU


def print_resources():
    """Prints a report of what resources the user has"""
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${format(resources['money'], '.2f')} ")


def take_resources(drink):
    resources["money"] -= MENU[drink]["cost"]
    resources["money"] = round(resources["money"], 2)
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]


def check_resources(drink):
    if resources["money"] < MENU[drink]["cost"]:
        print("That's not enough money. Money refunded.")
        resources["money"] = 0
        return False
    elif resources["water"] < MENU[drink]["ingredients"]["water"]:
        print(f"You do not have enough Water to make a {drink}")
    elif resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        print(f"You do not have enough Milk to make a {drink}")
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print(f"You do not have enough Coffee to make a {drink}")
    else:
        take_resources(drink)
        print(f"Here is your {drink}, enjoy!")
        print(f"you have ${format(resources['money'], '.2f')} change left")


def calculate_money(num_pennies, num_nickles, num_dimes, num_quarters):
    """Calculates the amount of money the user has after they have inputted their coins"""
    pennies = coins["penny"] * num_pennies
    nickles = coins["nickle"] * num_nickles
    dimes = coins["dime"] * num_dimes
    quarters = coins["quarter"] * num_quarters
    total_coins = pennies + nickles + dimes + quarters
    resources['money'] += total_coins


def add_money():
    """Takes in coins then adds their combined value to the users money"""
    print("Please insert some coins")
    pennies = int(input("How many pennies would you like to insert? "))
    nickles = int(input("How many nickles would you like to insert? "))
    dimes = int(input("How many dimes would you like to insert? "))
    quarters = int(input("How many quarters would you like to insert? "))
    calculate_money(pennies, nickles, dimes, quarters)


valid_choices = ["report", "off", "add"]
for key in MENU:
    valid_choices.append(key)

on = True
while on:
    user_choice = input("What would you like? (espresso, latte, cappuccino) Type report for a list of resources. : ").lower()
    while user_choice not in valid_choices:
        user_choice = input("That is not a valid choice, please choose one of the above drinks or report : ").lower()
    if user_choice == "off":
        on = False
    elif user_choice == "report":
        print_resources()
    else:
        add_money()
        check_resources(user_choice)


print("turning off machine")

