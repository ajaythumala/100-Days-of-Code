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

def print_menu():
    print("----MENU----")
    for coffee_type in MENU:
        print(coffee_type,f"-> ${MENU[coffee_type]['cost']}")
    print("------------")

def calculate_total():
    q = int(input("How many quarters? : "))
    d = int(input("How many dimes? : "))
    n = int(input("How many nickels? : "))
    p = int(input("How many pennies? : "))
    return (0.25 * q) + (0.1 * d) + (0.05 * n) + (0.01 * p)

def deplete_resouces(Choice):
    for ing in MENU[Choice]['ingredients']:
        resources[ing] -= MENU[Choice]['ingredients'][ing]
    print(f"and here's your {choice}, enjoy! :)\n")

def is_available(ingredients):
    for ing in ingredients:
        if resources[ing] < ingredients[ing]:
            return False
    return True
  
def is_sufficient(tot_input, cost):
    if tot_input < cost:
        print("Sorry that isn't enough money. Amount refunded.")
        return False
    elif tot_input > cost:
        print(f"Here's your change -> ${round(tot_input - cost, 2)}")
        return True

ended = False
other = ""
while not ended:
    print_menu()
    choice = input(f"What {other}would you like to order? : ").lower().strip()
    if choice == '0':
        ended = True
    elif choice == 'report':
        print("water -", resources["water"])
        print("coffee -", resources["coffee"])
        print("milk -", resources["milk"])
    else:
        drink = MENU[choice]
        if is_available(drink['ingredients']):
            print("Please insert coins.")
            tot_input = calculate_total()
            if is_sufficient(tot_input, drink['cost']):
                deplete_resouces(choice)
                other = "else "
    
    
    