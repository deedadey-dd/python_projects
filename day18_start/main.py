import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
timmy = Turtle()

# timmy.shape("turtle")
# timmy.color("green")

# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for _ in range (10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

colors = ["wheat", "blue", "red", "yellow", "green", "deep sky blue", "indigo", "rosy brown", "orange", "maroon", "gray", "aquamarine"]
move = [0, 90, 180, 270]


sides = 3
# angle = 360/sides
# while sides < 11:
#     angle = 360/sides
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)
#     sides += 1

# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360/num_sides
#         timmy.forward(100)
#         timmy.right(angle)
#
def change_color():
    # color = random.choice(colors)
    # while color != random.choice(colors):
    #     timmy.color(color)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    timmy.color(new_color)

#
# for shape in range(3, 11):
#     draw_shape(shape)
#     change_color()
#
# timmy.pensize(10)
# timmy.speed("fastest")
# while sides < 100:
#     timmy.forward(30)
#     timmy.setheading(random.choice(move))
#     change_color()
#     sides += 1


timmy.pensize(2)
angle = 5
timmy.speed("fastest")
for _ in range(int(360/angle)):
    change_color()
    timmy.circle(100)
    timmy.setheading(angle)
    angle += 5


screen = Screen()
screen.exitonclick()
