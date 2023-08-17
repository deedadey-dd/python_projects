from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
#screen.bgcolor("blue")

t_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
t_position = [125, 75, 25, -25, -75, -125]

all_turtles = []
#
# a = str(random.choice(t_colors))
# t_colors.remove(a)
# b = str(random.choice(t_colors))
# t_colors.remove(b)
# c = str(random.choice(t_colors))
# t_colors.remove(c)
# d = str(random.choice(t_colors))
# t_colors.remove(d)
# e = str(random.choice(t_colors))
# t_colors.remove(e)
# f = str(random.choice(t_colors))
#
# timmy = Turtle(shape="turtle")
# timmy.color(a)
# timmy.penup()
# timmy.goto(-230, 125)
#
# tommy = Turtle(shape="turtle")
# tommy.color(b)
# tommy.penup()
# tommy.goto(-230, 75)
#
#
# tobby = Turtle(shape="turtle")
# tobby.color(c)
# tobby.penup()
# tobby.goto(-230, 25)
#
#
# tonny = Turtle(shape="turtle")
# tonny.color(d)
# tonny.penup()
# tonny.goto(-230, -25)
#
#
# toffy = Turtle(shape="turtle")
# toffy.color(e)
# toffy.penup()
# toffy.goto(-230, -75)
#
# totty = Turtle(shape="turtle")
# totty.color(f)
# totty.penup()
# totty.goto(-230, -125)

for turtle_index in range(0, len(t_position)):
    tim = Turtle(shape="turtle")
    tim.color(t_colors[turtle_index])
    tim.penup()
    tim.goto(-230, t_position[turtle_index])
    all_turtles.append(tim)

user_bet = screen.textinput("Which Turtle will Win?", "Red, Orange, Yellow, Green, Blue, Purple").lower()

race_is_on = True

while race_is_on:

    for all_tims in all_turtles:
        all_tims.forward(random.randint(0, 10))

        if all_tims.xcor() > 220:
            winning_color = all_tims.pencolor()
            race_is_on = False

            if user_bet == winning_color:
                print(f"You've won, the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost, the {winning_color} turtle is the winner!")


screen.exitonclick()
