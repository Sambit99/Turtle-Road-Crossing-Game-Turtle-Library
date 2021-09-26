from turtle import Turtle
from config import FONT,SCREEN_HEIGHT,SCREEN_WIDTH

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto((SCREEN_WIDTH//2*-1)+50,(SCREEN_HEIGHT//2)-50)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}",align='center',font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER',align='center',font=FONT)

     