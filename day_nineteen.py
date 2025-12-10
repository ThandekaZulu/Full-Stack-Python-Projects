from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="What turtle will win the race? Enter a colo: ")

colors = [
    "violet",
    "indigo",
    "blue",
    "green",
    "yellow",
    "orange",
    "red"
]

all_turtles = []
y_position = [-100, -70, -40, -10, 20, 50, 80]

for index in range(7):
  turtles = Turtle(shape="turtle")
  turtles.penup()
  turtles.color(colors[index])
  turtles.goto(x=-230, y=y_position[index])
  all_turtles.append(turtles)

if user_bet:
  is_race_on = True

while is_race_on:

  for turtle in all_turtles:
    if turtle.xcor() > 230:
      is_race_on = False
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"You've won! The {winning_color} turtle is the winner")
      else:
        print(f"You've lost! The {winning_color} turtle is the winner")

    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)
    


# 
# Drawing game
# def move_forwards():
#   tim.forward(10)

# def move_backwards():
#   tim.backward(10)

# def move_clockwise():
#   new_heading = tim.heading() + 10
#   tim.setheading(new_heading)
#   # tim.right(10)

# def move_anti_clockwise():
#   new_heading = tim.heading() - 10
#   tim.setheading(new_heading)
#   # tim.left(10) 

# def clear_drawing():
#   tim.clear()
#   tim.penup()
#   tim.home()
#   tim.pendown()
  

# screen.listen()

# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="d", fun=move_clockwise)
# screen.onkey(key="a", fun=move_anti_clockwise)
# screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()

# Example
# def add(n1,n2):
#   return n1 + n2

# def calculator(n1,n2,fun):
#   return fun(n1,n2)

# result = calculator(2,3,add) # higher order function
# print(result)
# 