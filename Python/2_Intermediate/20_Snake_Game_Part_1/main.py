from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("No Step on Snek")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)

    snake.move()
