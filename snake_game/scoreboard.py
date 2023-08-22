import turtle
from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.scores = 0
        self.penup()
        self.goto((0, 280))

    def reprint(self):
        self.clear()
        self.write(arg=f"SCORE: {self.scores}", move=False, align="center", font=("Arial", 14, "normal"))



