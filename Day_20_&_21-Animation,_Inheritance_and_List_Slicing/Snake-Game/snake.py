from turtle import Turtle   # https://docs.python.org/3/library/turtle.html

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Starting positions of the first segments
MOVE_DISTANCE = 20
UP = 90  # Headings
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.body = self.segments[1:]  # List Slicing - takes all but first entry in list

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.hideturtle()
        new_segment.color("white")
        new_segment.speed("fastest")
        new_segment.goto(position)
        self.segments.append(new_segment)
        new_segment.showturtle()

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)  # Make all segments leave the screen

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.body = self.segments[1:]  # List Slicing - takes all but first entry in list

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # range(start, stop, step)
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y) # Make segment move to the position of the segment in front of it
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  # Make sure snake cant reverse
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

