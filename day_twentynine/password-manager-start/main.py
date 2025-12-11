from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  # nr_letters = random.randint(8, 10)
  # nr_symbols = random.randint(2, 4)
  # nr_numbers = random.randint(2, 4)

  password_list = (
      [choice(letters) for _ in range(randint(8, 10))] +
      [choice(symbols) for _ in range(randint(2, 4))] +
      [choice(numbers) for _ in range(randint(2, 4))]
  )

  # password_list = []

  # for char in range(nr_letters):
  #   password_list.append(random.choice(letters)) 

  # for char in range(nr_symbols):
  #   password_list += random.choice(symbols)

  # for char in range(nr_numbers):
  #   password_list += random.choice(numbers)

  shuffle(password_list)

  password = "".join(password_list)
  password_entry.insert(0,password)
  pyperclip.copy(password)
  # password = ""
  # for char in password_list:
  #   password += char

  # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
          messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
      is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                            f"\nPassword: {password} \nIs it ok to save?")
      
      if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            # Clear fields after saving
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1,row=0)

# website label
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

# website_entry
website_entry = Entry(width=38)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

# email/username label
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0,row=2)

# email_username_entry
email_username_entry = Entry(width=38)
email_username_entry.grid(column=1,row=2,columnspan=2)
email_username_entry.insert(0,"tsazulu@gmail.com")

# password label
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

# password_entry
password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

# generate password button
generate_password_button = Button(text="Generate Password", 
                      command=generate_password,              
                      highlightthickness=0)
generate_password_button.grid(column=2, row=3)

# add button
add_button = Button(text="Add", width=36,
                      highlightthickness=0,
                      command=save_data)
add_button.grid(column=1, row=4,columnspan=2)

window.mainloop()