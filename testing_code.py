# DAY 24
f = open("testing.txt", "r")
replace_with_name = f.replace("[name]", "invited")
print(f.readlines())

# # DAY 15
# MENU = {
#     "espresso": {
#         "ingredients": {"water": 50, "coffee": 18},
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {"water": 200, "milk": 150, "coffee": 24},
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {"water": 250, "milk": 100, "coffee": 24},
#         "cost": 3.0,
#     }
# }

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
#     "money": 0.0,
# }

# COIN_VALUES = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}


# def is_resource_sufficient(order_ingredients):
#     for item in order_ingredients:
#         if resources[item] < order_ingredients[item]:
#             print(f"Sorry there is not enough {item}.")
#             return False
#     return True


# def process_coins():
#     print("Please insert coins.")
#     total = 0
#     for coin in COIN_VALUES:
#         count = int(input(f"How many {coin}? "))
#         total += count * COIN_VALUES[coin]
#     return round(total, 2)


# def is_transaction_successful(money_received, drink_cost):
#     if money_received < drink_cost:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#     change = round(money_received - drink_cost, 2)
#     if change > 0:
#         print(f"Here is ${change} dollars in change.")
#     resources["money"] += drink_cost
#     return True


# def make_coffee(drink_name, order_ingredients):
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name}. Enjoy!")


# def print_report():
#     print(f"Water: {resources['water']}ml")
#     print(f"Milk: {resources['milk']}ml")
#     print(f"Coffee: {resources['coffee']}g")
#     print(f"Money: ${resources['money']}")


# def coffee_machine():
#     while True:
#         choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
#         if choice == "off":
#             print("Turning off the coffee machine. Goodbye!")
#             break
#         elif choice == "report":
#             print_report()
#         elif choice in MENU:
#             drink = MENU[choice]
#             if is_resource_sufficient(drink["ingredients"]):
#                 payment = process_coins()
#                 if is_transaction_successful(payment, drink["cost"]):
#                     make_coffee(choice, drink["ingredients"])
#         else:
#             print("Invalid selection. Please choose espresso, latte, or cappuccino.")


# # Start the machine
# coffee_machine()

# # END DAY 15
# # DAY 14
# # import art
# # import random
# # import game_data

# # def format_celebrity(celeb):
# #     """Returns a formatted string for a celebrity dictionary."""
# #     return f"{celeb['name']}, {celeb['description']}, from {celeb['country']}"

# # def game_loop():
# #     """Main game loop for Higher-Lower comparison."""
# #     print(art.higher_lower_game)
# #     score = 0
# #     compare_a = random.choice(game_data.data)
# #     compare_b = random.choice(game_data.data)
    
# #     while compare_b == compare_a:
# #         compare_b = random.choice(game_data.data)

# #     while True:
# #         print(f"\nCompare A: {format_celebrity(compare_a)}")
# #         print(f"Compare B: {format_celebrity(compare_b)}")
        
# #         guess = input("Who has more followers? Type 'A' or 'B': ").lower()
# #         a_followers = compare_a["follower_count"]
# #         b_followers = compare_b["follower_count"]
# #         correct = "a" if a_followers > b_followers else "b"
        
# #         if guess == correct:
# #             score += 1
# #             print(f"✅ Correct! Current score: {score}")
# #             compare_a = compare_a if correct == "a" else compare_b
# #             compare_b = random.choice(game_data.data)
# #             while compare_b == compare_a:
# #                 compare_b = random.choice(game_data.data)
# #         else:
# #             print(f"❌ Wrong! Final score: {score}")
# #             break

# # # Run the game
# # game_loop()

# # DAY 10
# # def calculator(first_number, symbol, second_number):
# #     if symbol == "+":
# #         return first_number + second_number
# #     elif symbol == "-":
# #         return first_number - second_number
# #     elif symbol == "*":
# #         return first_number * second_number
# #     elif symbol == "/":
# #         return first_number / second_number
# #     else:
# #         print("Invalid operation.")
# #         return first_number

# # repeat = True
# # first_number = int(input("What is your first number?:\n"))

# # while repeat:
# #     symbol = input("Pick your operation:\n +\n -\n *\n /\n")
# #     second_number = int(input("What is your second number?:\n"))

# #     output = calculator(first_number, symbol, second_number)
# #     print(f"Result: {output}")

# #     continue_not = input(f"Type 'yes' to continue with {output}, or 'no' to exit:\n").lower()
# #     if continue_not == 'yes':
# #         first_number = output  # reuse the previous result
# #     else:
# #         repeat = False
# # 
# # DAY 8
# # import caesar_art

# # print(caesar_art.logo)

# # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
# #             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# # def caesar(original_text,shift_amount,direction):
# #     # direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# #     # original_text = input("Type your message:\n").lower()
# #     # shift_amount = int(input("Type the shift number:\n"))

# #     # Flip shift once, outside the loop
# #     if direction == "decode":
# #         shift_amount *= -1

# #     decode_text = ""
# #     for letter in original_text:
# #         if letter in alphabet:
# #             shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
# #             decode_text += alphabet[shifted_position]
# #         else:
# #             decode_text += letter  # Keep symbols, numbers, punctuation

# #     print(f"Here is the {direction}d result: {decode_text}")

# # # Run the function
# # # caesar()

# # should_continue = True
# # while should_continue:
# #     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# #     original_text = input("Type your message:\n").lower()
# #     shift_amount = int(input("Type the shift number:\n"))

# #     caesar(original_text,shift_amount,direction)

# #     restart = input("Type 'yes' if you want to go again.Otherwise type 'no': ").lower()

# #     if restart == "no":
# #         should_continue = False
# #         print("GOODBYE")