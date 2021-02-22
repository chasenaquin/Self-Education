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

turt.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turt.color(random_color())
        turt.circle(100)
        current_heading = turt.heading()
        turt.setheading(turt.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
