from turtle import Turtle
from config import SCREEN_WIDTH,BORDER_POSITIONS



class Border(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('black')
        self.penup()
        self.pensize(1)

    def zebra_crossing(self):
        for items in BORDER_POSITIONS:
            self.goto(SCREEN_WIDTH//2,items)
            self.setheading(180)
            self.pendown()
            while(self.xcor()>(SCREEN_WIDTH//2*-1)):
                self.color('black')
                self.forward(5)
                self.color('white')
                self.forward(5)
            self.penup()
