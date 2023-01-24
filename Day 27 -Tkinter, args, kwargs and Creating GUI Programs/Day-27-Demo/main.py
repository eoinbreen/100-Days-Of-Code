from tkinter import *  # https://docs.python.org/3/library/tkinter.html#    http://tcl.tk/man/tcl8.6/TkCmd/entry.htm

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.place(x=100, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


# Button
def button_clicked():
    my_label["text"] = my_input.get()


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Click Me Too", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
my_input = Entry(width=10)
my_input.grid(column=3, row=2)


window.mainloop()  # Keeps window open - must be last line in code


