from turtle import Turtle   # https://docs.python.org/3/library/turtle.html

STARTING_POSITION = (-350, 0)  # Starting position of the Paddles
MOVE_DISTANCE = 20



class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.speed("fastest")
        self.goto(STARTING_POSITION)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

