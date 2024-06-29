MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
machineON = True


def report():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ${money}")


def check_resources(drink, menu, resources):
    ingredients = menu[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return round(quarters + dimes + nickles + pennies, 2)


def process_order(drink):
    global money
    if check_resources(drink, MENU, resources):
        cost = MENU[drink]["cost"]
        payment = process_coins()
        if payment >= cost:
            change = round(payment - cost, 2)
            money += cost
            for item in MENU[drink]["ingredients"]:
                resources[item] -= MENU[drink]["ingredients"][item]
            print(f"Here is your {drink}. Enjoy!")
            if change > 0:
                print(f"Here is ${change} in change.")
        else:
            print("Sorry, that's not enough money. Money refunded.")


while machineON:
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee == "off":
        machineON = False
    elif coffee == "report":
        report()
    elif coffee in MENU:
        process_order(coffee)
    else:
        print(
            "Invalid selection. Please choose espresso, latte, or cappuccino.")
