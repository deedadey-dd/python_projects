from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1190, height=650)
screen.title("PONG")
screen.tracer(0)
# don't forget to update the screen else no display of elements

# create paddles
left_paddle = Paddle(pos="left")
right_paddle = Paddle(pos="right")

# TODO Create ball
ball = Ball()


# Start the game
game_is_on = True

while game_is_on:
    screen.update()
# move the ball

    ball.move_ball(angle=27)

# listen for key presses and move paddles accordingly
    screen.listen()
    screen.onkey(fun=right_paddle.move_up, key="Up")
    screen.onkey(fun=right_paddle.move_down, key="Down")
    screen.onkey(fun=left_paddle.move_up, key="w")
    screen.onkey(fun=left_paddle.move_down, key="s")

    # detect collision with walls
    # detect collision with paddles
    if ball.xcor() == 580 and ball.distance(right_paddle) < 10:
        ball.setheading(120)

    # keep scores

screen.exitonclick()
