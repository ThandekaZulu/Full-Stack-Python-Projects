#  **kwargs: Many Keyworded Arguments
def calculate(n, **kwargs): # unlimited key words arguments
  # print(kwargs)
  # for key, value in kwargs.items():
  #   print(key)
  #   print(value)
  # print(kwargs["add"])
  n += kwargs["add"]
  # print(n)
  n *= kwargs["multiply"]
  # print(n)

calculate(n=2,add=3, multiply=5)
#  ..........
class Car:
  def  __init__(self,**kw):
    self.make = kw.get("make")
    self.model = kw.get("model")
    self.color = kw.get("color")
    self.seat = kw.get("seat")
    # or the above option is better since 
    # if one argument is not provided the program does not crash
    # self.make = kw["make"]
    # self.model = kw["model"]
my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)
# ........
# Unlimited positional arguments
# def add(*args):
#   print(sum(args))

# or
# def add(*args):
#   print(args[2])
#   sum = 0
#   for n in args:
#     sum += n
#   return sum

# print(add(3,5,6))