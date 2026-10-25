from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard():
    def __init__(self):
        self.scoreboard=Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.penup()
        self.scoreboard.goto(x=-260,y=270)
        self.level_no=1
        self.scoreboard.write(f"Level {self.level_no}:",False,"left",FONT)

    def game_over(self):
        game=Turtle()
        game.hideturtle()
        game.write("Game Over",False,"center",FONT)
    def increase_level(self):
        self.level_no+=1