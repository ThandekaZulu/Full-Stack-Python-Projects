# DAY 2
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12, 0r 15? "))
people = int(input("How many people to split the bill? "))

tip_amount = total_bill * (tip / 100)
total_with_tip = total_bill + tip_amount

payment_per_person = total_with_tip / people
             
print(f"Each person should pay: ${round(payment_per_person, 2)} ")

# 6+4/2-2
# 6+2-2
# 8-2
# 6
# a = int("5") / int(2.7)
# print(type(a))

# flooring number, removing decimal place
# bmi = 84 / 1.65 ** 2
# print(bmi) # decimal
# print(int(bmi)) # whole number
# print(round(bmi)) # rounded to the nearest decimal place
# print(round(bmi, 2))
# Implicit type casting
# print(type(6 / 2)) #even though these are int however python converts these to float
# print(6 // 3) # this removes decimal places
# priority PEMDAS === (), **, (*,or /)left calculate first, (+,or -)
# print(3 * 3 + 3 / 3 - 3) # 9+1-3
# print(3 * (3 + 3) / 3 - 3) #=3*6/3-3=18/3-3=6-3=3

# print("Number of letter in your name " + len(input("Enter your name")))
# name = input("Enter your name")
# length = len(name)
# print(f"Number of letter in your name {length}")
      
# substring
# print("hello"[-1])
# print(1_2 + 1_2)
# type casting/conversion
# print(len(str(abs(-1012))))
# print("Hi")
# print(12)
# print(12.0)
# print(True)