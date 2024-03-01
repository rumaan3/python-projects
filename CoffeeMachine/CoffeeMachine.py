import random


#DATA coding
#make a dictionary of resources
#make a dictionary of menu items with ingredient amounts

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

profit = 0
is_on = True


def generate_report():
    """Prints the available resources"""
    print(resources)
    print(profit)


def check_ing(stock, menu_item, menu):
    a = menu[menu_item]['ingredients']
    for i in a:
        if a[i] > stock[i]:
            print(f"sorry {i} is not available ")
            return False
    return True


def check_input(item, menu1):
    """Checks the Input"""
    if item == "report":
        generate_report()
        return True
    elif item == "off":
        print("machine is Turned OFF")
        return False
    elif item in menu1:
        return True


def collect_money():
    print("please insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction(a, b):
    if b >= a:
        change = round(b - a, 2)
        print(f"here is the {change}.")
        global profit
        profit += a
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_item(item1, c):
    """makes the item of choice"""
    for i in c:
        resources[i] -= c[i]
    print(f"Here is your {item1} Drink")


while is_on:
    choice = input(" What would you like to have? (espresso/latte/cappuccino) :  ")
    if check_input(choice, MENU):
        if check_ing(resources, choice, MENU):
            payment = collect_money()
            if transaction(MENU[choice]['cost'], payment):
                make_item(choice, MENU[choice]['ingredients'])
        else:
            is_on = False
    else:
        is_on = False







