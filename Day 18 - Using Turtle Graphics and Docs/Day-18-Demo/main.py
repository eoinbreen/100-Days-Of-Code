from turtle import Turtle, Screen
import random
# https://docs.python.org/3/library/turtle.html

timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.shape("turtle")
timmy.color("magenta")
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.pencolor(r, g, b)


def shapes():
    """Ask Timmy to draw multiple shapes"""
    for sides in range(3, 11):
        random_color()
        angle = 360 / sides
        for n in range(sides):
            timmy.forward(100)
            timmy.right(angle)


def dashed_line():
    """Ask Timmy to draw a dashed line"""
    for n in range(15):
        timmy.pendown()
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)


def random_walk():
    """Bring Timmy for a walk, changing to a random direction every so often"""
    timmy.pensize(15)
    directions = [0, 90, 180, 270]
    for n in range(100):
        random_color()
        direction = random.choice(directions)
        timmy.setheading(direction)
        timmy.forward(30)


def spinograph(times):
    """Ask Timmy to draw a spinograph"""
    tilt = 360 / times
    for n in range(times):
        random_color()
        timmy.circle(100)
        timmy.right(tilt)


spinograph(100)

screen.exitonclick()
