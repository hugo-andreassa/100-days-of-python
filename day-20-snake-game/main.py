from turtle import Turtle, Screen
import time
import random


def create_new_segment(x: float, y: float) -> Turtle:
    s = Turtle(shape="square")
    s.penup()
    s.color("white")
    s.goto(x, y)
    return s


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

snake_body = [create_new_segment(0, 0), create_new_segment(-20, 0), create_new_segment(-40, 0)]

screen.update()

is_game_on = True
while is_game_on:
    for seg in snake_body:
        seg.forward(20)

    time.sleep(1)
    screen.update()

screen.exitonclick()