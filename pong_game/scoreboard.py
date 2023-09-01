from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 250)
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", move=False, align="center", font=("Courier", 30, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scores()

    def r_point(self):
        self.r_score += 1
        self.update_scores()
