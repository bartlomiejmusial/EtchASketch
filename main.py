from turtle import Turtle, Screen
from random import choice


tim_turtle = Turtle()
tim_turtle.color('red')
screen = Screen()


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


def move_forward():
    tim_turtle.forward(10)


def move_backward():
    tim_turtle.backward(10)


def turn_left():
    tim_turtle.color(choice(colors))
    tim_turtle.left(10)


def turn_right():
    tim_turtle.color(choice(colors))
    tim_turtle.right(10)


def clear_drawing():
    tim_turtle.speed(50)
    while tim_turtle.pos() != (0, 0):
        tim_turtle.undo()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)


screen.listen()
screen.exitonclick()
