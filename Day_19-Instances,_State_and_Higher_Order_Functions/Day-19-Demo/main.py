from turtle import Turtle, Screen
# https://docs.python.org/3/library/turtle.html
timmy = Turtle()
screen = Screen()
screen.colormode(255)

timmy.shape("turtle")
timmy.color("green")
timmy.speed("fastest")


def move_forwards():
    timmy.forward(10)


screen.listen()
screen.onkeypress(key="space", fun=move_forwards)

screen.exitonclick()
