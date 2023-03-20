from turtle import Turtle   # https://docs.python.org/3/library/turtle.html

ALIGNMENT = "center"
FONT = ("Consolas", 80, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def add_score(self, paddle):
        if paddle == "l":
            self.l_score += 1
        if paddle == "r":
            self.r_score += 1
        self.update_scoreboard()
