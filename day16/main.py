from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    all_drinks = menu.get_items()
    choice = input(f"What would you like? {all_drinks}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink_selected = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink_selected):
            if money_machine.make_payment(drink_selected.cost):
                coffee_maker.make_coffee(drink_selected)
