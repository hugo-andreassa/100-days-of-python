import pandas as pd
import turtle

states_data = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
# Load image
image = "blank_states_img.gif"
screen.addshape(image)
# Use image
turtle.shape(image)

print(states_data)

is_game_on = True
while is_game_on:
    answer_state = screen.textinput("Guess the State", "What's another state's name?")
    state = states_data[states_data["state"] == answer_state.title()]
    if not state.empty:
        print(state)
    else:
        is_game_on = False

screen.exitonclick()
