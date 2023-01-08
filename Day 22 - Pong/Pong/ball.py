from turtle import Turtle   # https://docs.python.org/3/library/turtle.html


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.move_speed_x = 10
        self.move_speed_y = 10

    def move(self):
        new_y = self.ycor() + self.move_speed_y
        new_x = self.xcor() + self.move_speed_x
        self.goto(new_x, new_y)

    def bounce(self, axis):
        if axis == "y":
            self.move_speed_y *= -1
        if axis == "x":
            self.move_speed_x *= -1
