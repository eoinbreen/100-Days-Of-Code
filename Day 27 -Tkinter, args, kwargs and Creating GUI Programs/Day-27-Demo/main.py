import tkinter  # https://docs.python.org/3/library/tkinter.html#

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="left")  # Creates Label in the middle of the screen

window.mainloop()  # Keeps window open - must be last line in code


