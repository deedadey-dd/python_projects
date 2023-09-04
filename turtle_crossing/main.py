import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

# Create Turtle Player
player = Player()

car = CarManager()

score = Scoreboard()

game_is_on = True


while game_is_on:
    score.update_score()
    time.sleep(0.04)
    screen.update()

    # move player upon key press
    screen.listen()
    screen.onkey(fun=player.move_player, key="Up")
    screen.onkey(fun=player.reverse_player, key="Down")

    car.create_car()
    car.move_cars()
    car.hideturtle()

    for cars in car.all_cars:
        if player.distance(cars) < 20:
            game_is_on = False
            score.gama_over()

    if player.ycor() > 280:
        player.goto(0, -280)
        car.increase_speed()
        score.level_up()
        score.update_score()


screen.exitonclick()
