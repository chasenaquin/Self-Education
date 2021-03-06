from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_number in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_number -1].xcor()
            new_y = self.segments[seg_number -1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.segments[0].forward(20)