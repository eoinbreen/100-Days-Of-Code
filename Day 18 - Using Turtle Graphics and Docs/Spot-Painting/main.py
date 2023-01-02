from turtle import Turtle, Screen
import random

# import colorgram
# https://pypi.org/project/colorgram.py/
# Getting the colors - only needed to run module once to get list below
# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

colors = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]
timmy = Turtle()
screen = Screen()
screen.colormode(255)

timmy.shape("turtle")
timmy.color("green")
timmy.speed("fastest")

timmy_x_pos = -600
timmy_y_pos = -500
timmy.penup()

for col in range(10):
    timmy.goto(timmy_x_pos, timmy_y_pos)

    for row in range(10):
        random_color = random.choice(colors)
        timmy.dot(20, random_color)
        timmy.forward(50)

    timmy_y_pos += 50
timmy.hideturtle()

screen.exitonclick()


