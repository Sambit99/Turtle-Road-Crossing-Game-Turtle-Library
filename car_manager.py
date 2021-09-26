from turtle import Turtle, width
from config import COLOURS,CARS_MOVING_SPEED, SCREEN_WIDTH,SPEED_INCREMENT,BORDER_POSITIONS
import random

class CarManager:
    def __init__(self) -> None:
        self.all_cars = []
        self.car_speed = CARS_MOVING_SPEED

    def create_car(self):
        frequency = random.randint(1,6)
        if frequency == 1:
            new_car = Turtle(shape='square')
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            # new_car.setheading(180)
            new_car.color(random.choice(COLOURS))
            new_car.goto(SCREEN_WIDTH//2,random.choice(BORDER_POSITIONS)+10)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        
    def level_up(self):
        self.car_speed += SPEED_INCREMENT

