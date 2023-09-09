from turtle import Turtle
import random

COLORS = ["green", "blue", "red", "purple", "brown", "yellow", "black"]
MOVEMENT_FACTOR = 10
INCREMENT = 5


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.new_speed = MOVEMENT_FACTOR

    def create_car(self):
        repeat = random.randint(0, 3)
        if repeat == 3:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-13, 13)
            new_car.color(random.choice(COLORS))
            new_car.goto(270, random_y * 20)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.new_speed)

    def level_up_speed(self):
        self.new_speed += INCREMENT
