from turtle import Turtle, Screen
import random


def draw_shape(sides: int):
    angle = 360 / sides
    for _ in range(1, sides + 1):
        t.forward(100)
        t.right(angle)


def random_walk(walks: int):
    directions = [0, 90, 180, 270]

    for _ in range(walks):
        t.setheading(random.choice(directions))
        t.forward(20)


# Challenge
t = Turtle()
t.shape("arrow")
t.speed(15)

# Challenge 1 - Square
for i in range(1, 5):
    # t.forward(100)
    # t.right(90)
    pass

# Challenge 2 - Dashed line
t.left(90)
for _ in range(1, 11):
    # t.forward(5)
    # t.penup()
    # t.forward(5)
    # t.pendown()
    pass

# Challenge 3 - Drawing complex shapes
# t.right(90)
# draw_shape(3)
# draw_shape(4)
# draw_shape(5)
# draw_shape(6)
# draw_shape(7)
# draw_shape(8)

# Challenge 4 - Random Walk
# random_walk(100)

# Challenge 5 - Draw Circles
t.left(90)
space = 1
for i in range(int(360/space)):
    current_heading = t.heading()
    t.circle(500)
    t.setheading(current_heading + space)


screen = Screen()
screen.exitonclick()
