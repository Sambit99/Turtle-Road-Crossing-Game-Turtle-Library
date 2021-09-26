from turtle import Turtle
from config import PLAYER_STARTING_POSITION,PLAYER_FINISHING_POSITION


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('green')
        self.go_to_starting_pos()
        self.setheading(90)
    
    def move(self):
        self.forward(10)

    def is_at_finish_line(self):

        if self.ycor()>=PLAYER_FINISHING_POSITION:
            return True

        return False

    def go_to_starting_pos(self):
        self.goto(PLAYER_STARTING_POSITION)