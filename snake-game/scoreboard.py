from turtle import Turtle

class Scoreboard:
    def __init__(self):
        self.scoreboard=Turtle()
        self.scoreboard.color("white")
        self.scoreboard.penup()
        self.scoreboard.goto(0,260)
        self.scoreboard.hideturtle()
        #game over turtle
        self.game_over = Turtle()
        self.game_over.color("white")
        self.game_over.penup()
        self.game_over.hideturtle()

    def write_on_screen(self,points):
        self.scoreboard.clear()
        self.scoreboard.write(f"Score = {points}",False,'left',font=("Arial",50,"bold"))


    def stop_game(self):
        self.scoreboard.goto(0, 0)
        self.scoreboard.write("Game Over",False)

