# Range
# Password Exercise
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
           ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("Welclome to the PyPassword Generator!")
nr_letters = int(input("Letters you want in your password?\n"))
nr_symbols = int(input("Symbols you want in your password?\n"))
nr_numbers = int(input("Numbers you want in your password?\n"))

password = []

for _ in range(nr_letters):
  password.append(random.choice(letters))

for _ in range(nr_symbols):
  password.append(random.choice(symbols))


for _ in range(nr_numbers):
  password.append(random.choice(numbers))
  
random.shuffle(password)
print(password)
password = ''.join(password)
print(password)
# print("Here is your password")
# 
# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")   
#   else:  
#     print(number)
# 
# for number in range(1, 10):
# sum = 0

# for number in range(1, 101):
#   sum += number
# print(sum)
# 
# for loop
# student_scores = [900, 500, 700, 100,3100]
# # print(max(student_scores))

# max = student_scores[0]

# for score in student_scores:
#   if score > max:
#     max = score
# print(max)
# print(score)
# 
# total_score = sum(student_scores)
# print(total_score)
# sum_score = 0

# for score in student_scores:
#   sum_score += score
# print(sum_score)
# 
# fruits = ["Apple","Peach", "Pear"]
# for fruit in fruits:
#   print(fruit)