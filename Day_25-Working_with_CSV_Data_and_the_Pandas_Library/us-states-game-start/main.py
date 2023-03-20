import turtle   # https://docs.python.org/3/library/turtle.html
import pandas  # https://pandas.pydata.org/docs/

# Setting up the screen
screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(height=491, width=725)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

timmy = turtle.Turtle()
timmy.hideturtle()
timmy.penup()

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

guessed_states = []
answer_state = ""
while len(guessed_states) < 50 and answer_state != "Exit":
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state in states and answer_state not in guessed_states:
        state = data[data.state == answer_state]
        timmy.goto(int(state.x), int(state.y))
        timmy.write(answer_state, align="center", font=("Consolas", 8, "bold"))
        guessed_states.append(answer_state)

# find the states you missed and put them into a CSV file to learn for the next time you play
forgotten_states = [state for state in states if state not in guessed_states]  # List Comprehension
states_to_learn = pandas.DataFrame(forgotten_states)
states_to_learn.to_csv("states_to_learn.csv")
