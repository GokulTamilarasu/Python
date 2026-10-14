from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.turtlesize(1)
        self.color("white")
        self.start=random.randint(0,450)
        self.goto(y=self.start,x=0)



