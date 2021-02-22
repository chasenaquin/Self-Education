# RGB is going to be represtented by a tuple.
# my_tuple = (1, 2, 8)
# mytuple[0]
# Can not change the values of a tuple
# Can change to a list: list(my_tuple)

import turtle as t
import random

turt = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


directions = [1, 90, 180, 270]
turt.pensize(10)
turt.speed(0)

for _ in range(200):
    turt.color(random_color())
    turt.forward(25)
    turt.setheading(random.choice(directions))
