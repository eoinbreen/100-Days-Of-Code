from tkinter import *  # https://docs.python.org/3/library/tkinter.html#    http://tcl.tk/man/tcl8.6/TkCmd/entry.htm

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()  # Creates Label in the middle of the screen


# Button
def button_clicked():
    my_label["text"] = my_input.get()


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
my_input = Entry(width=10)
my_input.pack()


window.mainloop()  # Keeps window open - must be last line in code


