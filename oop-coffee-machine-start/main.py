from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu_methods=Menu()
total=0
is_on=True
while is_on:
    list_of_drinks=menu_methods.get_items()
    order=input(f"What would You like to have?({list_of_drinks}):  ")
    if order=='off':
        is_on=False
    elif order=='report':
        print(coffee_maker.report())
    else:
        drink = menu_methods.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



