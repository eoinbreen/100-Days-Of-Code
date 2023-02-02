from tkinter import *  # https://docs.python.org/3/library/tkinter.html#    http://tcl.tk/man/tcl8.6/TkCmd/entry.htm
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    num_letters = random.randint(8, 10)
    num_symbols = random.randint(2, 4)
    num_numbers = random.randint(2, 4)

    char_list = [random.choice(letters) for n in range(num_letters)]
    symbol_list = [random.choice(symbols) for n in range(num_symbols)]
    number_list = [random.choice(numbers) for n in range(num_numbers)]
    password_list = char_list + symbol_list + number_list

    random.shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(username) ==0 or len(password) == 0:
        messagebox.showwarning(title="Empty Fields!!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="Adding Password", message=f"These are the details entered:\nEmail: {username}"
                                                                        f" \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:  # Use try if you think an exception may be raised by the code
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)  # Reading old data
            except FileNotFoundError:  # Catch any exception that may happen with previous code, can have multiple
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)  # Create the file if an exception is called
            else:  # Runs if no exception has happened
                data.update(new_data)  # Updating old data with new data
                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)  # Saving updated data
            finally:  # Always runs
                website_input.delete(0, END)
                password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry()
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")  # Sticky sticks widget to east and west edges of column
website_input.focus()

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_input = Entry()
username_input.grid(column=1, row=2, columnspan=2, sticky="EW")
username_input.insert(0, "e.breen185@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry()
password_input.grid(column=1, row=3, sticky="EW")

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

save_password_button = Button(text="Add", command=add)
save_password_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
