from turtle import Screen # https://docs.python.org/3/library/turtle.html
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Check Collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("y")
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.add_score("l")
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.add_score("r")
    # Check collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce("x")

screen.exitonclick()
