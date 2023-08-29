from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        #self.ball = Turtle(shape="circle")
        self.shape("circle")
        self.penup()
        self.color("white")
        self.angle = 0

    def move_ball(self, angle):
        self.setheading(angle)
        self.forward(1)

    def ball_position(self):
        new_ball_position = self.ball.pos()
        return new_ball_position
