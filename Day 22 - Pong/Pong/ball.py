from turtle import Turtle   # https://docs.python.org/3/library/turtle.html


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):

        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce(self, axis):
        if axis == "y":
            self.y_move *= -1
        if axis == "x":
            if self.xcor() > 330:
                self.goto(329, self.ycor())  # move away from the paddle, dint get stuck in it
            if self.xcor() < -330:
                self.goto(-329, self.ycor())

            self.x_move *= -1
            self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce("x")
        self.move_speed = 0.1
