from turtle import Turtle

class Scoreboard:
    def __init__(self):
        self.scoreboard=Turtle()
        self.scoreboard.color("white")
        self.scoreboard.penup()
        self.scoreboard.goto(0,110)
        self.scoreboard.hideturtle()

    def write_on_screen(self,points):
        self.scoreboard.clear()
        self.scoreboard.write(f"Score = {points}",False,'left',font=("Arial",50,"normal"))
