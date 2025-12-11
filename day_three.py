# DAY 3
# LOGICAL OPERATORS = and, or, not
# print("Welcome to Treasure Island. " 
#       "Your mission is to find the treasure")
# left_or_right = input("You have arrived in an Island, " 
#                       "will you take Left or Right? ").lower()
# if left_or_right == "right":
#   print("Game Over!!!")
# elif left_or_right == "Left" or left_or_right == "left":
#   swim_or_wait = input("There is a sea before you. " 
#                         "Do you want to Swim or Wait? ").lower()
#   if swim_or_wait == "swim":
#     print("Crocodile ate you.Game Over!!")
#   else:
#     door = input("There is a Red, Blue and Yellow door. " 
#                  "Choose one: ").lower()
#     if door == "yellow":
#       print("You Win!!!!!!!")
#     else:
#       print("Game over!!")
# else:
#   print("Game over!!")

# 
# print("Welcome to the Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# bill = 0

# if size == "S":
#   bill = 15
#   if pepperoni == "Y":
#     bill += 2
# elif size == "M":
#   bill = 20
#   if pepperoni == "Y":
#     bill += 3
# else:
#   bill = 25
#   if pepperoni == "Y":
#     bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}")

# Modulo
# number = int(input("Enter a number. "))
# if number % 2 == 0:
#   print("The number is even.")
# else:
#   print("The number is odd.")
# 
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#   print("You can ride the rollercoaster")
#   age = int(input("What is your age? "))
#   if age < 12:
#     bill = 5
#     print("Child tickets $5.")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets $7.")
#   elif 45 <= age <=55:
#     print("ZERO bill")
#   else:
#     bill = 12
#     print("Adult ticket is $12")

#   wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.") 
#   if wants_photo == "y":
#     #  Add to their bill
#     bill += 3
#   print(f"You final bill is {bill}")
# else:
#   print("Sorry you have to grow taller before you can ride.")

# comparison operator >,<, >=, <=, !=, ==