from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-260, 260)
        rand_y = random.randint(-260, 200)
        self.goto(rand_x, rand_y)

