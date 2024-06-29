from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mnu = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()
flag = True


while flag:
    inp = input(f"select your drink {mnu.get_items()}")

    if inp == "report":
        mm.report()
        cm.report()
    elif inp == "off":
        flag = False
    else:
        item = mnu.find_drink(inp)
        if cm.is_resource_sufficient(item):
            if mm.make_payment(item.cost):
                cm.make_coffee(item)








