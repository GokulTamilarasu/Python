from turtle import Turtle

class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
    def score_display(self,points):
        self.clear()
        self.write(f"Score:{points}",False,"center",("Roboto",300,'bold'))
