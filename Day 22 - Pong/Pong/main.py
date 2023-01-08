from turtle import Screen # https://docs.python.org/3/library/turtle.html
from paddle import Paddle
from ball import Ball
import time

STARTING_POSITION = [(-350, 0), (350, 0)]  # Starting position of the Paddles

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(STARTING_POSITION[0])
r_paddle = Paddle(STARTING_POSITION[1])
ball = Ball()

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Check Collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("y")
    # Check collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce("x")
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce("x")
screen.exitonclick()
