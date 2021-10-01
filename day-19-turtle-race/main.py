from turtle import Turtle, Screen
import random


def setup_turtle(y: int, color: str, x=-230) -> Turtle:
    t = Turtle(shape="turtle")
    t.penup()
    t.goto(x=x, y=y)
    t.color(color)

    return t


turtles = []
colors = ["red", "blue", "orange", "yellow", "green", "purple"]
positions = [70, 40, 10, -20, -50, -80]
is_game_on = False

# Setup screen
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which Turtle will win the race? Enter a color: ").lower()

if user_bet:
    is_game_on = True

# Setup turtles
for i in range(0, 6):
    t = setup_turtle(positions[i], colors[i])
    turtles.append(t)

while is_game_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost. The {winning_color} turtle is the winner!")
            is_game_on = False
            break

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
