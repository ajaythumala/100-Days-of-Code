
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(choice_ingredients):
    for ingredient in choice_ingredients:
        if resources[ingredient] < choice_ingredients[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            return False
    return True

def process_coins():
    total = int(input("How many quarters? "))
    total += int(input("How many dimes? "))
    total += int(input("How many nickels? "))
    total += int(input("How many pennies? "))
    return total

def is_transaction_successful(received_amount, order_cost):
    if received_amount > order_cost:
        print(f"Here is {round(received_amount - order_cost)} in change.")
        global profit
        profit += order_cost
        return True
    else :
        print(f"Sorry, you are short of {order_cost - received_amount}, your amount has been refunded.")
        return False

def make_coffee(Choice, order_ingredients):
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"And here is your {Choice} :)")

#main
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])