import caesar_art

print(caesar_art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text,shift_amount,direction):
    if direction == "decode":
        shift_amount *= -1

    decode_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            decode_text += alphabet[shifted_position]
        else:
            decode_text += letter  # Keep symbols, numbers, punctuation

    print(f"Here is the {direction}d result: {decode_text}")

# Run the function
# caesar()

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    original_text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))

    caesar(original_text,shift_amount,direction)

    restart = input("Type 'yes' if you want to go again.Otherwise type 'no': ").lower()

    if restart == "no":
        should_continue = False
        print("GOODBYE")
# 
# # Exercise
# def calculate_love_score(name_one,name_two):
#   combined_names = (name_one + " " + name_two).lower()
  
#   name_checkers_one = "true"
#   name_checkers_two = "love"
#   count_name_checkers_one = 0
#   count_name_checkers_two = 0

#   for i in name_checkers_one:
#     count_one = combined_names.count(i)
#     print(f"{i} occurs {count_one} times")
#     count_name_checkers_one += count_one
#   print(f"Total: {count_name_checkers_one}")
  
#   for i in name_checkers_two:
#     count_two = combined_names.count(i)
#     print(f"{i} occurs {count_two} times")
#     count_name_checkers_two += count_two
#   print(f"Total: {count_name_checkers_two}")
#   print(f"Love scrore is: {count_name_checkers_one}{count_name_checkers_two}")
    

# # calculate_love_score("Angela Yu", "Jack Bauer")
# # calculate_love_score("Thandeka", "Zulu")
# calculate_love_score("Kanye West", "Kim Kardashian")

# #  
# # def greet(location, name):
# #   print(f"Hi {name}!")
# #   print("How are you?")
# #   print("Im good and how are you?")
# #   print(f"Are you in {location}?")

# # greet(location = "Durban", name = "Thandeka")