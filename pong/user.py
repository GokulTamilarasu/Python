from turtle import Turtle


class User(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.setheading(90)
        self.penup()

    def user_up(self):
        self.forward(10)
    def user_down(self):
        self.backward(10)

