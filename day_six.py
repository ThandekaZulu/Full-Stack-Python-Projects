# Code Block
# Functions
# Maize
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
 
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
# 
# Hurdle 4
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
 
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
# 
# Hurdle 3
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal():
#     if front_is_clear():
#         move()
#     else:
#         turn_left()
#         move()
#         turn_right()
#         move()
#         turn_right()
#         move()
#         turn_left()
# Reeborg's World (While loop is good for when you want to achieve a certain goal not really caring about each iteration)
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def turn():    
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# step = 0
# while step != 6:
#     turn()
#     step += 1
# # Same as above
# step = 6
# while step > 0:
#     turn()
#     step -= 1
# # using at_goal() function
# while at_goal() != True: # or not at_goal()
#     turn() 
# 
# Reeborg's World (For loop is good for when you want to utilise each item as you iterate through the loop )
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def turn():    
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# for t in range(6):
#     turn()
# 
# Draw a square
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# # Draw Square
# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()
