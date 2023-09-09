from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.scores = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())

    def reprint(self):
        self.clear()
        self.goto(0, 280)
        self.write(arg=f"SCORE: {self.scores}   Highscore: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        # if self.scores > self.highscore:
        #     with open("data.txt", mode="w") as file:
        #         file.write(f"{self.scores}")
        # self.reprint()
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def update_high_score(self):
        if self.scores > self.highscore:
            with open("data.txt", mode="w") as file:
                file.write(f"{self.scores}")
        self.reprint()
