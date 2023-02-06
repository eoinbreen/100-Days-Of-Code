from tkinter import *  # https://docs.python.org/3/library/tkinter.html#    http://tcl.tk/man/tcl8.6/TkCmd/entry.htm
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
words_to_learn = data.to_dict(orient="records")


def next_card():
    word = random.choice(words_to_learn)["French"]
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(word_text, text=f"{word}")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)

window.mainloop()
