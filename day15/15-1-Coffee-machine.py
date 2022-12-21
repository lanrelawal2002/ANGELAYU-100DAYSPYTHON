# my first version of the coffee machine project
# I fixed the dollar top up problem by altering the content of the "resources" dictionary.

def show_resources():
    water_left = resources["water"]
    milk_left = resources["milk"]
    coffee_left = resources["coffee"]
    money_left = resources["balance"]

    print(f"Water: {water_left}ml\nMilk: {milk_left}ml\nCoffee: {coffee_left}g\nMoney: ${money_left}")


def check_resources(current_dict, resources_dict, drink_selected):
    if resources_dict["water"] < current_dict["ingredients"]["water"]:
        return f"Sorry there is not enough water"
    elif resources_dict["coffee"] < current_dict["ingredients"]["coffee"]:
        return f"Sorry there is not enough coffee"

    if drink_selected == "latte" or drink_selected == "cappuccino":
        if resources_dict["milk"] < current_dict["ingredients"]["milk"]:
            return f"Sorry there is not enough milk"

    return f"get coins"


def coin_amount():
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = float(((0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)))

    return total


def coin_process(total_money, working_dict):
    if total_money < working_dict["cost"]:
        return 0
    elif total_money == working_dict["cost"]:
        return total_money
    elif total_money > working_dict["cost"]:
        change = total_money - working_dict["cost"]
        change_rounded = round(change, 2)
        return change_rounded


def adjust_resources(drink_selected, resources_dict, working_dict):
    resources_dict["water"] = resources_dict["water"] - working_dict["ingredients"]["water"]
    resources_dict["coffee"] = resources_dict["coffee"] - working_dict["ingredients"]["coffee"]
    resources_dict["balance"] = resources_dict["balance"] + working_dict["cost"]

    if drink_selected == "latte" or drink_selected == "cappuccino":
        resources_dict["milk"] = resources_dict["milk"] - working_dict["ingredients"]["milk"]


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "balance": 0
}

game_run_outer = True

while game_run_outer:
    user_request = input("What would you like? (espresso/latte/cappuccino): ")
    if user_request == "off":
        game_run_outer = False
    elif user_request == "report":
        show_resources()
    elif user_request == "espresso" or user_request == "latte" or user_request == "cappuccino":
        drink_dict = MENU[user_request]
        resource_verdict = check_resources(drink_dict, resources, user_request)
        if resource_verdict == "get coins":
            total_amount = coin_amount()
            money_returned = coin_process(total_amount, drink_dict)
            if money_returned == 0:
                print(f"Sorry that's not enough money. Money refunded.")
            elif total_amount == money_returned:
                print(f"Here is your {user_request}. Enjoy!!!")
                adjust_resources(user_request, resources, drink_dict)
            elif total_amount > money_returned:
                print(f"Here is ${money_returned} in change.")
                print(f"Here is your {user_request}. Enjoy!!!")
                adjust_resources(user_request, resources, drink_dict)
        else:
            print(resource_verdict)
    else:
        print(f"enter either 'espresso' 'latte' 'cappuccino' 'report' or 'off'")
