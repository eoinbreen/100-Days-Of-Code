from tkinter import *  # https://docs.python.org/3/library/tkinter.html#    http://tcl.tk/man/tcl8.6/TkCmd/entry.htm

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ("Consolas", 35, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"

reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label["text"] = "Break"
        title_label["fg"] = RED
        checkmark_label["text"] = ""
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label["text"] = "Break"
        title_label["fg"] = PINK
    else:
        count_down(WORK_MIN * 60)
        title_label["text"] = "Work"
        title_label["fg"] = GREEN
        checkmark_label["text"] += CHECKMARK

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = int(count/60)
    count_secs = count % 60

    if count_secs < 10:
        count_secs = f"0{count_secs}"  # Add a 0 in front of single digit number to make it look like a timer

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_secs}")
    if count > 0:
        window.after(1, count_down, count - 1)  # 1000 for timer
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", font=FONT, bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=FONT)
canvas.grid(column=1, row=1)


def start():
    start_timer()


start_button = Button(text="Start", command=start)
start_button.grid(column=0, row=2)


def reset():
    pass


reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=2, row=2)


checkmark_label = Label(text="", bg=YELLOW, fg=GREEN)
checkmark_label.grid(column=1, row=3)

window.mainloop()
