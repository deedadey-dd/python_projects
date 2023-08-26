from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


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
        self.write(arg=f"SCORE: {self.scores}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
