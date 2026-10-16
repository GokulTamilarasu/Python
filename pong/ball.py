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
        self.x_move=20
        self.y_move=20

    def ball_move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
    def y_change(self):
        self.y_move*=-1
    def x_change(self):
        self.x_move*=-1

    def reset_position(self):
        self.goto(0, 0)
        self.x_change()


