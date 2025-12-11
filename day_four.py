# LISTS = mutable,can be mixed data types
import random

# game_images = [rock, paper, scissors]

your_choice = int(input("What do you choose?\n"
               " Type 0 for Rock, 1 for Paper"
               "or 2 for Scissors: "))
# if your_choice >= 0 and your_choice <= 2:
  # print(game_images[your_choice])

computer_choice = random.randint(0, 2)
# print(game_images[your_choice])

if your_choice >= 3 or your_choice < 0:
  print("Invalid number")
  print(f"You choice: {your_choice} -- Computer choice: {computer_choice}")
elif your_choice == 0 and computer_choice == 2:
  print(f"You choice: {your_choice} -- Computer choice: {computer_choice}")
  print("You Wins!")
elif your_choice == 2 and computer_choice == 0:
  print(f"You choice: {your_choice} -- Computer choice: {computer_choice}")
  print("You lose!")
elif computer_choice > your_choice:
  print(f"You choice: {your_choice} -- Computer choice: {computer_choice}")
  print("You loose!")
elif your_choice > computer_choice:
  print(f"You choice: {your_choice} -- Computer choice: {computer_choice}")
  print("You Win!")
elif your_choice == computer_choice:
  print(f"You choice: {your_choice} -- Computer choice: {computer_choice}")
  print("It a draw!")



# 
# friends = ["Alice","Bob","Charlie","David","Emmanuel"]
# #  option 1
# print(random.choice(friends))

# # option 2
# random_index = random.randint(0, 4)
# print(friends[random_index])
# 
# Randomisation Khan Academy
# import random
# determiner_number = random.randint(0, 1)
# if determiner_number == 0:
#   print(f"Heads, Number is {determiner_number}")
# else:
#   print(f"Tails, Number is {determiner_number}")
# 
# random_number_0_to_one = random.random() * 10
# print(random_number_0_to_one)

# random_float = random.uniform(1,10)
# print(random_float)
# 
# import my_module

# random_integer = random.randint(1, 10) 
# print(random_integer)

# print(my_module.my_favourite_number)