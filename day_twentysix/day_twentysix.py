import pandas
# Dictionary comprehension
# Pandas dictionary
student_dict = {
  "student": ["Angela","James","Lily"],
  "score": [56,76,98]
}

# looping through dictionary
# for key,value in student_dict.items():
  # print(value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# loop through dataframe
# for (key,value) in student_data_frame.items():
#   print(key)
#   print(value)

# Loop through rows of a data frame
for(index, row) in student_data_frame.iterrows():
  # print(index)
  # print(row)
  # print(row.student)
  # print(row.score)
  if row.student == "Angela":
    print(row.score)


# Testing
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}
# print(result)
# .....
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
# import random

# names = ["Abongwe","Liwayo","Jade","Pears"]
# students_scores = {new_key:new_value for item in names}
# students_scores = {student:random.randint(1, 100) for student in names}
# print(students_scores)

# passed_students = {ps for ps in students_scores.items() if students_scores.items() >= 60}
# passed_students = {name: score for name, score in students_scores.items() if score >= 60}
# print(passed_students) 
# 
# Conditional list comprehension
# names = ["Abongwe","Liwayo","Jade","Pears"]
# new_list = [name.upper() for name in names if len(name) >= 5]
# print(new_list)
# 
# List comprehension
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)
# range
# double_numbers = [dn * 2 for dn in range(1,5)]
# print(double_numbers)

# strings
# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)
# 
# it when you create a list from another list
# numbers = [1,2,3]
# new_list = []
# for n in numbers:
#   add_1 = n + 1
# new_list.append(add_1)

# # Another way
# # new_list = [n + 1 for n in numbers]

# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)