# Function()
# year = 2400
# leap_year = True

# def leap_year_or_not(year):
#   """
#   Take year then determines whether it a 
#   leap year or not.
#   """
#   if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     return leap_year
#   else:
#     return not leap_year
# output = leap_year_or_not(2400)
# print(output)
# 
# def format_name(f_name, l_name):
#   if f_name == "" or l_name == "":
#     return "NO first and last name inserted"
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()

#   return f"{formated_f_name} {formated_l_name}"
 
# print(format_name(input("What is your first name?\n"), 
#       input("What is your last name?\n")))

# output = format_name("thanDEKa", "zulu")
# 
# def function_1(text):
#   return text + text

# def function_2(text):
#   return text.title()

# print(function_2(function_1("hello")))
# 
# def format_name(f_name, l_name):
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()

#   return f"{formated_f_name} {formated_l_name}"
#   # return f_name.title() +" "+ l_name.title()
#   # return (f_name).capitalize() + " " + (l_name).capitalize()

# # output = format_name()
# output = format_name("thanDEKa", "zulu")
# print(output)
# 
# def my_function():
#   return 3*1

# output = my_function()
# print(output)
# 
# CALCULATOR = MY VERSION
# 
# END = CALCULATOR = MY VERSION
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# operations["*"] = multiply
# print(multiply(4,8))
#           or
# print(operations["*"](4,8))

def calculator():
  repeat = True
  n1 = float(input("What is your first number?:\n"))

  while repeat:
      for symbol in operations:
        print(symbol)
      symbol = input("Pick an operation:\n")
      n2 = float(input("What is your second number?:\n"))

      if symbol in operations:
        output = operations[symbol](n1,n2)
        print(f"{n1} {symbol} {n2} = {output}")

      continue_not = input(f"Type 'yes' to continue with {output}, or 'no' to exit:\n").lower()
      if continue_not == 'yes':
          n1 = output  # reuse the previous result
      else:
          repeat = False
          print("\n" * 20)
          calculator()

calculator()