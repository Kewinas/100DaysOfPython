from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


def report():
    coffee_maker.report()
    money_machine.report()


def process_order(order_name):
    drink = menu.find_drink(order_name)
    if drink:
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


machineON = True
while machineON:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee == "off":
        machineON = False
    elif coffee == "report":
        report()
    elif coffee in [item.name for item in menu.menu]:
        process_order(coffee)
    else:
        print(
            "Invalid selection. Please choose espresso, latte, or cappuccino.")

print("Coffee machine turned off.")
