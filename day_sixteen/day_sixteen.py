# OOP paradigm = model real life objects - small pieces, (restarant)
# Python packages = code other developers have written
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokeman Name",["Picachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

# table.align["Pokeman Name"] = "l"
# table.align["Type"] = "l"
table.align = "l"
print(table)
# 
# import another_module
# print(another_module.another_variable)

# import turtle
# timmy = turtle.Turtle()

# Same as above
# from turtle import Turtle,Screen
# from turtle import *

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)


# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# waiter - has(attributes(variable attacked to a particular object)) * is_hoding_plate = True
#        -                 * tables_responsibility = [4,5,6]
#        - does(methods(function attached to an object))   * def take_ordr(table, order): -> takes orders to chef
#        -                 * def take_payment(): -> add money to retaurant
# 
# Class models a car - object
# car(object) =  CarBlueprint()(class)
# Turtle Graphics

