# Instances are what we call the objects created from a class.
# State is what we call the different attributes of each Instance

from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput(title="Make your bet.", prompt="Enter color of turtle:")
colors = ["red", "orange", "yellow", "blue", "green", "purple" ]
all_turtles = []

y_axis = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0,6):
    turt = Turtle(shape="turtle")
    turt.color(colors[turtle_index])
    turt.penup()
    turt.goto(x=-250, y=y_axis[turtle_index])
    all_turtles.append(turt)

if user_bet:
    is_race_on = True

while is_race_on:
    for turt in all_turtles:
        if turt.xcor() > 290:
            is_race_on = False
            winning_color = turt.pencolor()
            if winning_color == user_bet:
                print("You win.")
            else:
                print(f"You lose. {winning_color} won.")
        random_distance = random.randint(0,10)
        turt.forward(random_distance)

screen.exitonclick()
