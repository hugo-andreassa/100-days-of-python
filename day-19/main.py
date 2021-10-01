from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def mov_forward():
    tim.forward(10)


def mov_backward():
    tim.back(10)


def mov_clockwise():
    tim.right(10)


def mov_counter_clockwise():
    tim.left(10)


def clear():
    screen.reset()

screen.listen()
screen.onkey(key="w", fun=mov_forward)
screen.onkey(key="s", fun=mov_backward)
screen.onkey(key="a", fun=mov_counter_clockwise)
screen.onkey(key="d", fun=mov_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
