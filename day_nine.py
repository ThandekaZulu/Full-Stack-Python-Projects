# DICTIONARY = MUTTABLE
# Nesting
# Auction Program
print("Welcome to the secret auction program.")
reapeat = False
bidders = {}

def find_highest_bidder(bidders):
  big_amount = 0
  winner = ""
  for bidder,amount in bidders.items():
    if amount > big_amount:
      big_amount = amount
      winner = bidder
  print(f"The winner is {winner} with {amount} amount of bid")

while not reapeat:
  name = input("What is your name?:\n")
  bid = int(input("What is your bid?:\n"))
  any_other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  bidders[name] = bid

  if any_other_bidders == 'yes':
    reapeat
  else:
    reapeat = True
    find_highest_bidder(bidders)

# 
# Nested Dictionary
# travel_log = {
#   "France": {
#     "cities_visited": ["Paris", "Lille", "Dijon"],
#     "total_visits": 12
#   },
#   "Germany": {
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#     "total_visits":5
#   }
# }
# print(travel_log["Germany"]["cities_visited"][2])
# 
# Nested list
# nested_list = ["A","B",["C","D"]]
# print(nested_list[2][1])
# print(nested_list[2][0])
# 
# capitals = {
#   "France": "Paris",
#   "Germany": "Berlin",
# }

# #  nested list in Dictionary
# travel_log = {
#   "France": ["Paris","Lille", "Dijon"],
#   "Germany": ["Stuttgart", "Berlin"],
# }

# print(travel_log["France"][1])
# 
# Grading program
# student_scrores = {"Bono": 50,
#                    "Dineo": 70,
#                    "Sbu": 80,
#                    "Koe": 90,
#                    "Cebo": 100}
# student_grades ={}

# for key in student_scrores:
#   if student_scrores[key] >= 91 or student_scrores[key] == 100:
#     student_grades[key] = "Outstanding"
#   elif student_scrores[key] >= 81 or student_scrores[key] == 90:
#     student_grades[key] = "Exceeds Expectations"
#   elif student_scrores[key] >= 71 or student_scrores[key] == 80:
#     student_grades[key] = "Acceptable"
#   else:
#     student_grades[key] = "Fail"

# print(student_scrores)
# print(student_grades)
# 
# programming_dictionary = {
#   "Bug": "An error",
#   "Function": "A piece ",
# }
# programming_dictionary["Loop"] = "The action"
# # print(programming_dictionary)

# # wipe dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# # edit an item in a dictionary
# programming_dictionary["Bug"] = "No explanation here"
# # print(programming_dictionary)

# # Looping through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])