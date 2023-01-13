from turtle import Turtle   # https://docs.python.org/3/library/turtle.html
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
POSITION = (305, 0)
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.setheading(180)
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        rand_y = random.randint(-250, 250)
        new_car.goto(305, rand_y)
        new_car.color(random.choice(COLORS))
        self.cars.append(new_car)
