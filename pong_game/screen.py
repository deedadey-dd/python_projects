from turtle import Screen


class Screened:
    def __init__(self):
        self.screen = Screen()


def create_screen():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=1200, height=700)
    screen.tracer(0)
