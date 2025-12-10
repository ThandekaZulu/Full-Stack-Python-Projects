# Spirograph with turtle
from turtle import Turtle,Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.speed(0)

screen = Screen()
screen.colormode(255)

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r,g,b)

def draw_spirograph(size_of_gap):
  for _ in range(int(360 / size_of_gap)):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(1)
screen.exitonclick()

# ============
# Tuple = Immutable - cannot be changed
# my_tuple = (1, 3, 8)
# print(my_tuple)
# my_tuple[0] = 12
# ========
# import heroes
# import villains

# print(heroes.gen())
# 
# import turtle as t # t = alias name
# tim = t.Turtle()
# ================
# from turtle import Turtle, Screen
# # from turtle import *
# import random

# tim = Turtle()
# tim.speed(0)
# screen = Screen()
# screen.colormode(255)
# # color_t = ()

# # colors = ["red", "blue", "green", "yellow", "orange",
# #           "purple", "pink", "brown", "black", "cyan"]

# def random_color():
#   r = random.randint(0, 255)
#   g = random.randint(0, 255)
#   b = random.randint(0, 255)
#   return (r,g,b)

# directions = [0,90,180,270]
# tim.pensize(15)

# def random_walk(steps):
#   for _ in range(steps):
#     tim.forward(10)
#     tim.setheading(random.choice(directions))
#     tim.color(random_color())

# random_walk(200)

# ============
# num_sides = 10
# colors = ["red", "blue", "green", "yellow", "orange",
#           "purple", "pink", "brown", "black", "cyan"]

# def draw_shape(num_sides):
#   angle = 360 / num_sides 
#   for _ in range(num_sides):
#     tim.forward(100)
#     tim.right(angle)

# for sides in range(3,11):
#   tim.color(random.choice(colors))
#   draw_shape(sides)

# for _ in range(15):
#   tim.forward(10)
#   tim.penup()
#   tim.forward(10)
#   tim.pendown()



# 
# tim.shape("square")
# tim.color("green")

# for _ in range(4):
#   tim.forward(100)
#   tim.right(90)

# screen.exitonclick()