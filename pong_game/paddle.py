from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        #self.paddle = Turtle()
        self.create_paddle(position=pos)

    def create_paddle(self, position):
        if position == "left":
            y_pos = -580
        else:
            y_pos = 580

        self.color("white")
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(y_pos, 0)

    def move_up(self):
        if self.ycor() != 280:
            self.forward(20)

    def move_down(self):
        if self.ycor() != -280:
            self.backward(20)

    def paddle_position(self):
        new_paddle_position = self.pos()
        return new_paddle_position
