# Hangman
import random
import my_list
from hangman_art import hangman

# Step 1
# TODO-1 Randomly choose a word from the word_list
# word_list = ["aardvark","baboon","camel"]

# chosen_word = random.choice(word_list)
chosen_word = random.choice(my_list.word_list)

# Create blanks for each letter
display = ["_"] * len(chosen_word)
print(chosen_word)
print("".join(display))

# Keep prompting until all blanks are filled
lives = 6

while "_" in display and lives > 0:
  guess = input("Guess a letter: ").lower()
  correct = False

  for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
      display[i] = guess
      print(hangman[0])
      correct = True
    if guess in display[i]:
      print(f"You have guessed {guess} letter already!")

  if not correct:
    lives -= 1
    print(f"You guessed {guess}. You loose a life.")
    print(f"******* {lives}/6 LIVES LEFT*******")
    print(f'The correct word is "{chosen_word}"')
    print(hangman[6 - lives])
  print("".join(display))

if "_" not in display:
  print("CONGRATULATIONS YOU WON!!!")
else:
  print("SORRY You lose!!")

