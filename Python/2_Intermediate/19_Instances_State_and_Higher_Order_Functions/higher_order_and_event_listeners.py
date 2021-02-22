from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()

def move_forward():
    turt.forward(10)


screen.listen()

#High Order Function
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()
