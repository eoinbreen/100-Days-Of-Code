from turtle import Turtle   # https://docs.python.org/3/library/turtle.html
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
POSITION = (305, 0)
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def move_cars(self):
        for car in self.cars:
            car.backward(self.move_distance)
            if car.xcor() < -305:  # If car goes off the screen
                self.cars.remove(car)

    def create_car(self):
        random_chance = random.randint(1, 5)  # Called every update function, random chance to slow down number of cars
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            rand_y = random.randint(-250, 250)
            new_car.goto(305, rand_y)
            new_car.color(random.choice(COLORS))
            self.cars.append(new_car)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
