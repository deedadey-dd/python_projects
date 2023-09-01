from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from turtle import Turtle


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

score = Turtle()

# Start the game
game_is_on = True
#angle = 45

while game_is_on:
    screen.update()
# move the ball
    time.sleep(0.04)

    ball.move_ball()

# listen for key presses and move paddles accordingly
    screen.listen()
    screen.onkey(fun=right_paddle.move_up, key="Up")
    screen.onkey(fun=right_paddle.move_down, key="Down")
    screen.onkey(fun=left_paddle.move_up, key="w")
    screen.onkey(fun=left_paddle.move_down, key="s")

    # detect collision with walls
    ball.wall_bounce()

    # detect collision with paddles
    if ball.xcor() < -560 and ball.distance(left_paddle) < 20:
        ball.paddle_bounce()
    elif ball.xcor() > 560 and ball.distance(right_paddle) < 20:
        ball.paddle_bounce()


# detect escape and game over
    if ball.xcor() < -650 and ball.distance(left_paddle) > 50:
        game_is_on = False
        ball.game_over()

    if ball.xcor() > 600 and ball.distance(right_paddle) < 50:
        game_is_on = False
        ball.game_over()

screen.exitonclick()
