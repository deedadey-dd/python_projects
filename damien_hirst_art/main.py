# import colorgram
#
#
# colors = colorgram.extract("image.jpg", 20)
#
# # first_color = colors[0]
# # rgb = first_color.rgb
# new_rgb = []
# for c in colors:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     new_color = (r, g, b)
#
#     new_rgb.append(new_color )
# print(new_rgb)

from turtle import Turtle, Screen, colormode
import random

colormode(255)

colors = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99),
          (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244), (192, 87, 108), (11, 50, 64),
          (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77)]

timmy = Turtle()
timmy.hideturtle()
timmy.speed("fastest")


def start_position():
    timmy.speed("fastest")
    timmy.penup()
    timmy.forward(-200)
    timmy.setheading(270)
    timmy.forward(200)


def random_color():
    timmy.pencolor(random.choice(colors))


def draw_dot():
    timmy.pendown()
    timmy.dot(20)
    timmy.penup()
    timmy.setheading(0)
    timmy.forward(50)


def new_line():
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(0)
    timmy.forward(-500)


start_position()

for t in range (10):
    for _ in range (10):
        random_color()
        draw_dot()
    new_line()

screen = Screen()
screen.exitonclick()
