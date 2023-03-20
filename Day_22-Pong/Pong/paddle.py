from turtle import Turtle   # https://docs.python.org/3/library/turtle.html

MOVE_DISTANCE = 20



class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.speed("fastest")
        self.goto(position)

    def up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

