from turtle import Turtle, Screen
import random

y_position = [-70, -40, -10, 20, 50, 80]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(500, 400)
all_turtles = []
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will "
                                                          "win the "
                                                          "race? Enter a "
                                                          "color: ")
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! {winning_color} is the winner!")
            else:
                print(f"You lost! {winning_color} is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
