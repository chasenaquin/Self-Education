from turtle import Turtle, Screen
import random

turt = Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [1, 90, 180, 270]
turt.pensize(10)
turt.speed(0)

for _ in range(200):
    turt.color(random.choice(colors))
    turt.forward(25)
    turt.setheading(random.choice(directions))
