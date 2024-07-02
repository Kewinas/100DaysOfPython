from turtle import Turtle, Screen

tim = Turtle()


def triangle():
    tim.color("green")
    for a in range(3):
        tim.forward(100)
        tim.left(120)


def square():
    tim.color("red")
    for a in range(4):
        tim.forward(100)
        tim.left(90)


def pentagon():
    tim.color("blue")
    for a in range(5):
        tim.forward(100)
        tim.left(72)


def hexagon():
    tim.color("black")
    for a in range(6):
        tim.forward(100)
        tim.left(60)


def heptagon():
    tim.color("brown")
    for a in range(7):
        tim.forward(100)
        tim.left(360/7)


def octagon():
    tim.color("grey")
    for a in range(8):
        tim.forward(100)
        tim.left(45)


def nonagon():
    tim.color("yellow")
    for a in range(9):
        tim.forward(100)
        tim.left(40)


def decagon():
    tim.color("pink")
    for a in range(10):
        tim.forward(100)
        tim.left(36)


triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()
screen = Screen()
screen.exitonclick()
