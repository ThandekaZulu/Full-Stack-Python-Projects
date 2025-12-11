import random
import art_guessing_game 

print("Welcome to the number guessing game!\n"
      "I'm thinking of a number between 1 and 100\n"
      "")
game_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
# print(game_choice)

# print(random.randrange(1,101))
def choice(game_choice):
  print(art_guessing_game.guessing_game)
  easy_random = random.randint(1,100)
  attempts = 10 if game_choice == "easy" else 5

  while attempts > 0:
    print(f"{easy_random}")
    print(f"You have {attempts} attempts to guess the number.")
    guess_number = int(input("Make a guess: "))

    if guess_number > easy_random:
      print(f"Too high.\nGuess again.")
    elif guess_number < easy_random:
      print(f"Too low.")
    else:
      print("YOU WON CONGRATS")
      return
      
    attempts -= 1
  print("Ran out of attempts")

choice(game_choice)
# 
# Scope
# There is no scope block in Python
# Global enemies
# count = 1

# def counting(num):
#   return num + 1

# print(counting(count))
# 
# enemies = 1

# def increase_enemies():
#   global enemies
#   enemies += 1
#   print(f"Enemies inside function: {enemies}")

# increase_enemies()


