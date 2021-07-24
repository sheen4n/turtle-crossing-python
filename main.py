import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()
car_manager.create_car()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if randint(0, 6) == 0:
        car_manager.create_car()

    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.level_up()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    car_manager.move_cars()

screen.exitonclick()
