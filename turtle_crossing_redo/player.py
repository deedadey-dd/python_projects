from turtle import Turtle

START_LINE = (0, -280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(START_LINE)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)

    def go_to_start(self):
        self.goto(START_LINE)



