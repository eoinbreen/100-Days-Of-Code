import turtle   # https://docs.python.org/3/library/turtle.html


# Setting up the screen
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


correct = 0
while correct < 51:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")


screen.exitonclick()
