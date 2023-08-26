from turtle import Screen
from paddle import Paddle
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=700)
screen.tracer(0)

# Create and move the paddles
paddle = Paddle()
left_paddle = paddle.create_paddle("left")
right_paddle = paddle.create_paddle("right")
screen.update()


# Move the paddles
screen.listen()
screen.update()
time.sleep(0.1)
screen.onkey(fun=paddle.move("right"), key="Up")




screen.exitonclick()
