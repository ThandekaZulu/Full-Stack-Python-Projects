#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
import os

with open("./Input/Names/invited_names.txt", "r") as names_file:
  names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
  letter = letter_file.read()
  for name in names:
    clean_name = name.strip()
    personalised_letter = letter.replace("[name]", clean_name)
    with open(f"./Output/ReadyToSend/letter_for_{clean_name}.docx", "w") as output_file:
      output_file.write(personalised_letter)
  