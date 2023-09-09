from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(-350, 270)
        self.level = 1
        self.hideturtle()
        self.penup()

    def level_up(self):
        self.level += 1

    def update_score(self):
        self.clear()
        self.penup()
        self.write(f"LEVEL: {self.level}", move=False, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("Courier", 28, "bold"))