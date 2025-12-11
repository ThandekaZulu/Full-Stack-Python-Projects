import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states =[]

while len(guessed_states) < 50:
  answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                  prompt="What is another states name?").title()
  print(answer_state)
  if answer_state == "Exit":
    missing_state = []
    for state in all_states:
      if state not in guessed_states:
        missing_state.append(state)
    new_data = pandas.DataFrame(missing_state)
    new_data.to_csv("Missing States.csv")
    break
  if answer_state in all_states:
    guessed_states.append(answer_state)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x.item()), int(state_data.y.item()))
    t.write(state_data.state.item())

# state_to_learn.csv

# screen.exitonclick()

# turtle.shape(image)

# def get_mouse_click_coor(x, y):
#   print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()