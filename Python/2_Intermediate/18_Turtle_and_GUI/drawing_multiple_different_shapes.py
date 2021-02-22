# Alias for import module
# import turtle as t
from turtle import Turtle, Screen
import random

turt = Turtle()

turt.color("blue")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turt.forward(100)
        turt.right(angle)


for i in range(3,11):
    turt.color(random.choice(colors))
    draw_shape(i)

screen = Screen()
