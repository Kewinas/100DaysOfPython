import turtle
import random
from turtle import Turtle, Screen

tim = Turtle()

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


tim.speed(0)

for a in range(36):
    tim.color(random_color())
    tim.circle(100)
    tim.left(10)

screen = Screen()
screen.exitonclick()
