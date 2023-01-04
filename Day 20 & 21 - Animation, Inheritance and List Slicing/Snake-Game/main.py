from turtle import Screen, Turtle  # https://docs.python.org/3/library/turtle.html
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake")

segments = []


def move_snake():
    for seg_num in range(len(segments) - 1, 0, -1):  # range(start, stop, step)
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y) # Make segment move to the position of the segment in front of it
    segments[0].forward(20)


for n in range(3):
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    position_x = 0 - (n * 20)
    new_segment.goto(position_x, 0)
    segments.append(new_segment)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    move_snake()


screen.exitonclick()
