
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


def diff(total, item_cost):
    if total < item_cost:
        balance_amount = item_cost - total
        print(f"You have to pay extra ${round(balance_amount, 2)} to get the drink")
    elif total > item_cost:
        change = total - item_cost
        print(f"Enjoy your drink and here is your change ${round(change, 2)}")
    else:
        print("Enjoy your drink")


def coins():
    penny = int(input("How many Pennys: "))
    nickel = int(input("How many Nickel: "))
    dime = int(input("How many Dime: "))
    quarter = int(input("How many Quarter: "))
    total = penny * 0.01 + nickel * 0.05 + dime * 0.10 + quarter * 0.25
    print(f"Total amount is ${round(total, 2)}")
    return round(total, 2)


def drink_input(drink):
    item_cost = MENU[drink]["cost"]
    print(f"Total cost of Latte is ${item_cost}")
    print("Please insert the coins")
    total = coins()
    diff(total, item_cost)


cost = 0


def update_resources(drink):
    drink_ingredients = MENU[drink]["ingredients"]
    for i in drink_ingredients:
        menu_key = drink_ingredients[i]
        if resources[i] >= menu_key:
            # resources_key -= menu_key
            resources[i] -= menu_key

                # resources[i] = resources_key
        elif resources_key < menu_key:
            print(f"Not Enough {resources[key]} ")
    global cost
    cost += int(MENU[drink]["cost"])

    return resources


coffe_machine = True
while coffe_machine:
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input == 'report':
        for key, values in resources.items():
            print(key, values)
        print(f"Money: ${cost}")

    elif user_input == 'stop':
        coffe_machine = False

    else:
        drink_input(user_input)
        update_resources(user_input)

