from turtle import Turtle   # https://docs.python.org/3/library/turtle.html

FONT = ("Consolas", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)




