from turtle import Turtle
import random

import paddle
from paddle import Paddle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.ANGLES = [45, 315, 135, 225]
        self.angle = random.choice(self.ANGLES)

    def move_ball(self):
        self.setheading(self.angle)
        self.forward(20)

    def ball_position(self):
        new_ball_position = self.pos()
        return new_ball_position

    def wall_bounce(self):
        if self.ycor() > 310:
            if self.angle > 89:
                self.angle += 90
            else:
                self.angle = 360 - self.angle

        elif self.ycor() < -310:
            if self.angle > 269:
                self.angle = 360 - self.angle
            else:
                self.angle -= 90

    def paddle_bounce(self):
        if self.angle < 90:
            self.angle += 90
        elif self.angle < 180:
            self.angle -= 90
        elif self.angle < 270:
            self.angle += 90
        else:
            self.angle -= 90

    def reset_to_left(self):
        l_angles = random.choice(self.ANGLES[2:])
        self.goto(0, 0)
        self.angle = l_angles

    def reset_to_right(self):
        r_angles = random.choice(self.ANGLES[:2])
        self.goto(0, 0)
        self.angle = r_angles

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("Courier", 20, "normal"))
