import random
from turtle import Turtle, Screen
# https://docs.python.org/3/library/turtle.html
screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

starting_y = 125  # Starting Y position of first Turtle
turtles = []
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    y_position = starting_y - (50 * turtle_index)  # Space out each turtle
    new_turtle.goto(x=-230, y=y_position)
    turtles.append(new_turtle)

user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:  # if turtle has passed the finish line
            winning_color = turtle.pencolor()
            is_race_on = False
            if user_bet.lower() == winning_color:
                print(f"You win, the {winning_color} turtle won!!")
            else:
                print(f"You lose, the {winning_color} turtle won")


screen.exitonclick()
