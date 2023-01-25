from tkinter import *  # https://docs.python.org/3/library/tkinter.html#    http://tcl.tk/man/tcl8.6/TkCmd/entry.htm

window = Tk()
window.title("Miles to Km")
window.minsize(width=250, height=150)
window.config(padx=100, pady=50)

my_input = Entry(width=10)
my_input.insert(END, string=0)
my_input.grid(column=1, row=0)


def input_drop_changed(event):
    if menu.get() == "Miles":
        km_label["text"] = "Kilometers"
    elif menu.get() == "Kilometers":
        km_label["text"] = "Miles"


# Set the Menu initially
menu = StringVar()
menu.set("Miles")
# Create a dropdown Menu
input_drop = OptionMenu(window, menu, "Miles", "Kilometers", command=input_drop_changed)
input_drop.grid(column=2, row=0)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)
result_label.config

km_label = Label(text="Kilometers")
km_label.grid(column=2, row=1)


def calculate():
    if menu.get() == "Miles":
        miles = float(my_input.get())
        km = miles * 1.609344
        result_label["text"] = str(round(km, 2))
    elif menu.get() == "Kilometers":
        km = float(my_input.get())
        miles = km / 1.609344
        result_label["text"] = str(round(miles, 2))


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
