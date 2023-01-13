import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.up, "Up")

game_is_on = True
car_timer = 6
while game_is_on:
    time.sleep(0.1)
    screen.update()

