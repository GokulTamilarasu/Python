from turtle import Turtle
import random
class Obstacles(Turtle):
    def __int__(self):
        super().__init__()


    def random_position(self):
        new_y=random.randint(-100,100)
        self.hideturtle()
        self.shape("square")
        self.color("black")
        self.penup()
        self.turtlesize(stretch_len=2)
        self.goto(100,new_y)
        self.setheading(180)
        self.showturtle()


    def obstacle_move(self):
        self.forward(20)

