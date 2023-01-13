import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

CAR_TIMER = 6  # Cooldown on creating cars, decreases with each update

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.up, "Up")


game_is_on = True
car_timer = CAR_TIMER
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_timer -= 1
    if car_timer == 0:
        car_manager.create_car()
        car_timer = CAR_TIMER
    car_manager.move_cars()
    if player.ycor() > 260:
        scoreboard.increase_level()
        player.reset_position()
