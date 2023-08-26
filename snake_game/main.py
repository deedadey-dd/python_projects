import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)


# segment = []
# # color = ["green", "blue", "white", "yellow", "purple", "gray"]
#
# def snake(number):
#     timmy = Turtle(shape="square")
#     timmy.penup()
#     timmy.color("white")
#     timmy.goto(x=-20 * number, y=0)
#     return timmy
#
#
# for num in range(0, 3):
#     segment.append(snake(num))
#
# game_is_on = True
#
#
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#
#     for seg in range(len(segment) - 1, 0, -1):
#         new_x = segment[seg-1].xcor()
#         new_y = segment[seg-1].ycor()
#
#         segment[seg].goto(new_x, new_y)
#     segment[0].forward(20)

snakey = Snake()
food = Food()
score = Score()
food.change_location()


screen.listen()
screen.onkey(snakey.up, "Up")
screen.onkey(snakey.down, "Down")
screen.onkey(snakey.left, "Left")
screen.onkey(snakey.right, "Right")

score.reprint()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snakey.move()

    # Collision Detection
    if snakey.segment[0].distance(food) < 15:
        # print("yes!!!!!!")
        food.change_location()
        snakey.add_snake()
        score.scores += 1
        score.reprint()

    # Detect Wall Collision
    if snakey.head.xcor() > 290 or snakey.head.xcor() < -290 or snakey.head.ycor() > 290 or snakey.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    for body in snakey.segment[1:]:
        # if body == snakey.segment[0]:
        #     pass
        if snakey.head.distance(body) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
