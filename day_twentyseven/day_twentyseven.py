# TKinter = GUI
from tkinter import *

window  = Tk()
window.title("My first GUI Program")
window.minsize(width=500,height=300)

# label
my_label = Label(text="Im not a label",font=("Arial",24,"bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
def button_clicked():
  # my_label["text"] = "I got clicked"
  new_text = input.get()
  my_label.config(text=new_text)
  # print("I got clicked")

  

button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry()
input.pack()
input.get()

# ............
# Advanced python arguments
# Unlimited arguments
# def add(n1, n2):
#   return n1 + n2


# add(n1=5, n2=3)





window.mainloop() # keep window on the screen