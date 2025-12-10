# # DAY 15
# SOUTH AFRICAN VERSION
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 15.0,  # Rands
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 25.0,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 30.0,
    }
}

profit = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# South African coin values in Rands
COIN_VALUES = {
    "R5": 5.00,
    "R2": 2.00,
    "R1": 1.00,
    "50c": 0.50,
    "20c": 0.20,
    "10c": 0.10,
}

def is_resources_sufficient(order_ingredients):
    """Returns true when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from the coins inserted"""
    print("Please insert coins (in Rands).")
    total = 0
    for coin, value in COIN_VALUES.items():
        count = int(input(f"How many {coin} coins? "))
        total += count * value
    return round(total, 2)

def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is R{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️ Enjoy!")

# Main loop
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        print("Turning off the coffee machine. Goodbye!")
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: R{profit}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid selection. Please choose espresso, latte, or cappuccino.")