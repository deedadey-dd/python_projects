from turtle import Turtle


class Paddle:
    def __init__(self):
        self.left_segment = []
        self.right_segment = []

# Create Paddle. Use the position to specify if it is left or right
    def create_paddle(self, position):
        pos = 1
        segment = self.right_segment

        if position.lower() == "left":
            pos = -1
            segment = self.left_segment
        elif position.lower == "right":
            pos = 1

        for _ in range(3):
            timmy = Turtle()
            timmy.shape("square")
            timmy.penup()
            timmy.setheading(90)
            timmy.color("white")
            timmy.goto(pos * 570, 20 * _)
            segment.append(timmy)

    def move(self, position):
        segment = self.right_segment

        if position.lower() == "left":
            segment = self.left_segment
        elif position.lower() == "right":
            segment = self.right_segment

        for seg in range(len(segment) - 1, 0, -1):
            new_x = segment[seg - 1].xcor()
            new_y = segment[seg - 1].ycor()

            segment[seg].goto(new_x, new_y)
        segment[0].forward(20)
        print(segment)
