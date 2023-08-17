from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.speed("fastest")


def move_forward():
    timmy.forward(10)


def move_up():
    timmy.setheading(90)
    move_forward()


def move_left():
    timmy.left(10)
    move_forward()


def move_right():
    timmy.right(10)
    move_forward()


def move_down():
    timmy.setheading(270)
    move_forward()


def clear_screen():
    # screen.clearscreen()
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.onkey(key="space", fun=move_forward)
screen.onkey(key="w", fun=move_up)
screen.onkey(key="s", fun=move_down)
screen.onkey(fun=move_right, key="d")
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clear_screen)


screen.listen()
screen.exitonclick()
