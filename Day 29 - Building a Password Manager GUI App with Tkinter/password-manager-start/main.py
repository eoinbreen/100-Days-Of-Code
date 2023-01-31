from tkinter import *  # https://docs.python.org/3/library/tkinter.html#    http://tcl.tk/man/tcl8.6/TkCmd/entry.htm
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    if len(website) == 0 or len(username) ==0 or len(password) == 0:
        messagebox.showwarning(title="Empty Fields!!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="Adding Password", message=f"These are the details entered:\nEmail: {username}"
                                                                        f" \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{website} | {username} | {password}\n")
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
