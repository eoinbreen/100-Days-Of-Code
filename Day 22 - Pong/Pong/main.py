from turtle import Screen # https://docs.python.org/3/library/turtle.html
from paddle import Paddle
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

user_paddle = Paddle()

screen.listen()
screen.onkeypress(user_paddle.up, "Up")
screen.onkeypress(user_paddle.down, "Down")

game_on = True
while game_on:
    screen.update()

screen.exitonclick()
