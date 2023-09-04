from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-270, 270)

    def level_up(self):
        self.level += 1

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def gama_over(self):
        self.goto(-70, 0)
        self.write("GAME OVER", move=False, font=FONT)
