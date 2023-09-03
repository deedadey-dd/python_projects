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

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()

    # move player upon key press
    screen.listen()
    screen.onkey(fun=player.move_player, key="Up")
    screen.onkey(fun=player.reverse_player, key="Down")

    car.create_car()
    car.move_cars()

    for cars in car.all_cars:
        if player.distance(cars) < 20:
            game_is_on = False
            player.write("GAME OVER", move=False, font=("Courier", 25, "normal"))

screen.exitonclick()
