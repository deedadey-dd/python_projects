import time
from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Score

screen = Screen()
screen.title("Turtle Crossing")
screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0)

player = Player()
score = Score()
car = Car()
car.hideturtle()
game_is_on = True

while game_is_on:

    score.update_score()
    car.create_car()
    car.move_car()
    time.sleep(0.1)
    screen.update()

    screen.listen()
    screen.onkey(fun=player.move_up, key="Up")
    screen.onkey(fun=player.move_down, key="Down")

    for any_car in car.all_cars:
        if player.distance(any_car) < 15:
            game_is_on = False
            score.game_over()

    if player.ycor() > 270:
        player.go_to_start()
        car.level_up_speed()
        score.level_up()
        score.update_score()

    screen.update()

screen.exitonclick()
