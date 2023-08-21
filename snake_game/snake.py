from turtle import Turtle
STARTING_NUMBER = 3
MOVING_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()

    def create_snake(self):
        for num in range(STARTING_NUMBER):
            timmy = Turtle(shape="square")
            timmy.penup()
            timmy.color("white")
            timmy.goto(x=-20 * num, y=0)
            self.segment.append(timmy)

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()

            self.segment[seg].goto(new_x, new_y)
        self.segment[0].forward(20)

    def add_snake(self):
        new_x = self.segment[len(self.segment)-1].xcor()
        new_y = self.segment[len(self.segment) - 1].ycor()
        timmy = Turtle(shape="square")
        timmy.penup()
        timmy.color("white")
        timmy.goto(x=new_x, y=new_y)
        self.segment.append(timmy)

    def up(self):
        if self.segment[0].heading() == 0 or self.segment[0].heading() ==180:
            self.segment[0].setheading(90)

    def down(self):
        if self.segment[0].heading() == 0 or self.segment[0].heading() == 180:
            self.segment[0].setheading(270)

    def left(self):
        if self.segment[0].heading() == 90 or self.segment[0].heading() == 270:
            self.segment[0].setheading(180)

    def right(self):
        if self.segment[0].heading() == 90 or self.segment[0].heading() == 270:
            self.segment[0].setheading(0)
