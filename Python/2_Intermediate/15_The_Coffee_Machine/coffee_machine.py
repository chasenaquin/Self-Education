# Program Requirements
# TODO 1. Prompt user by asking "Drink order (Espresso, Latte, or Cappuccino):
#           A. Check users input and decide how to process it.
#           B. Show prompt everytime an action has completed.
# TODO 2. Turn off the Coffee Machine by entering "Off" to the prompt.
# TODO 3. Print Report.
#           A. Water, Milk, Coffee, Money.
# TODO 4. Check if resources are sufficient.
#           A. When user makes a request, program should check available resources.
#           B. If not enough available resources print ("Sorry there is not enough {resource).
# TODO 5. Process coins.
#           A. If sufficient resources, prompt the user to insert coins.
#           B. Calculate monetary value of the coins.
# TODO 6. Check if the transaction is successful.
#           A. Check to see if the user has inserted enough money.
#           B. If sufficient funds, the cost of the drink gets added to the machine resources.
#           C. If user inserts more money than required, issue a refund.
# TODO 7. Make Coffee
#           A. If transaction is successful and there are sufficient resources, then deduct resources from pool.
#           B. Once resources have been deducted print ("Here is your {drink_order}")

from os import system

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
profit = 0.00

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def machine_prompt():
    user_selection = input("Drink order: (Espresso, Latte, or Cappuccino?): ").lower()
    if user_selection in ("espresso", "latte", "cappuccino", "report", "off"):
        return user_selection
    else:
        machine_prompt()


def generate_resource_report():
    for resource in resources:
        print(f"{resource} : {resources[resource]}")
    print(f"Money : ${profit}")


def turn_machine_off():
    print("Shutting the coffee machine down...")
    exit()


def check_sufficient_resources(coffee_selection):
    for resource in resources:
        if MENU[coffee_selection]['ingredients'][resource] < resources[resource]:
            return True
        else:
            print(f"Unavailable resource: {resource}")
            return False


def payment(coffee_selection):
    coffee_selection_cost = MENU[coffee_selection]['cost']
    tender_values = {
        "penny": 0.01,
        "nickle": 0.05,
        "dime": 0.10,
        "quarter": 0.25,
    }

    payment_attempts = 2
    while payment_attempts > 0:
        pennies = int(input("Pennies: "))
        nickels = int(input("Nickles: "))
        dimes = int(input("Dimes: "))
        quarters = int(input("Quarters: "))
        total_payment = (pennies * tender_values["penny"]) + (nickels * tender_values["nickle"]) + \
                        (dimes * tender_values["dime"]) + (quarters * tender_values["quarter"])
        if total_payment >= coffee_selection_cost:
            global profit
            profit += coffee_selection_cost
            if total_payment > coffee_selection_cost:
                refund = total_payment - coffee_selection_cost
                print(f"You have paid: ${round(total_payment, 2)}. Your refund is: ${round(refund, 2)}")
                return True
        else:
            system('clear')
            print(f"You have paid: ${round(total_payment, 2)}. Insufficient funds.")
            print(f"You need: ${round(coffee_selection_cost - total_payment, 2)}")
            print(f"Payment attempts remaining: {payment_attempts}")
            payment_attempts -= 1


def make_coffee(coffee_selection):
    if coffee_selection == 'espresso':
        resources['water'] -= MENU[coffee_selection]['ingredients']['water']
        resources['coffee'] -= MENU[coffee_selection]['ingredients']['coffee']
    else:
        resources['water'] -= MENU[coffee_selection]['ingredients']['water']
        resources['coffee'] -= MENU[coffee_selection]['ingredients']['coffee']
        resources['milk'] -= MENU[coffee_selection]['ingredients']['milk']


def coffee_machine_operations():
    user_prompt_selection = machine_prompt()
    if user_prompt_selection == "report":
        generate_resource_report()
    elif user_prompt_selection == "off":
        turn_machine_off()
    elif user_prompt_selection in ("espresso", "latte", "cappuccino"):
        selected_coffee = user_prompt_selection
        available_resources = check_sufficient_resources(coffee_selection=selected_coffee)
        if available_resources:
            make_coffee(coffee_selection=selected_coffee)
            payment(coffee_selection=selected_coffee)


while True:
    coffee_machine_operations()

# # Angela's Code
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
#
# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True
#
#
# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total
#
#
# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#
#
# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")
#
#
# is_on = True
#
# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])
