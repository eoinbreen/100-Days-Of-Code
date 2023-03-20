from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


def report():
    coffee_maker.report()
    money_machine.report()

on = True
while on:
    user_choice = input(f"What would you like? {menu.get_items()} type report for a list of resources : ").lower()
    if user_choice == "off":
        on = False
    elif user_choice == "report":
        report()
    else:
        drink = menu.find_drink(user_choice)

        while drink is None:
            user_choice = input("Please choose one of the above drinks : ").lower()
            drink = menu.find_drink(user_choice)

        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
