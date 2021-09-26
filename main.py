import time
from turtle import Screen
from config import SCREEN_WIDTH,SCREEN_HEIGHT
from player import Player
from border import Border
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.tracer(0)
player = Player()
border = Border()
border.zebra_crossing()
car_manager = CarManager()
car_manager.create_car()

scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move,'Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_starting_pos()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()