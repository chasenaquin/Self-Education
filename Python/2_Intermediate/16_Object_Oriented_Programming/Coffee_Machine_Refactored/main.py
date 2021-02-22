from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 1. Print Report
# TODO 2. Check Resouces Sufficient
# TODO 3. Process Coins
# TODO 4. Check Transaction Successful
# TODO 5. Make Coffee

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What coffee would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice in options:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)
