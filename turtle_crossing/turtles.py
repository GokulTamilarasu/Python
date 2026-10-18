from turtle import Turtle
class Player(Turtle):
    def __int__(self):
        super().__init__()


    def create_player(self):
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0,-200)

    def move_forward(self):
        self.forward(20)

    def move_down(self):
        self.hideturtle()
        self.setheading(-90)
        self.forward(20)
        self.setheading(90)
        self.showturtle()

    def move_left(self):
        x=self.xcor() - 20
        y=self.ycor()
        self.penup()
        self.goto(x,y)

    def move_right(self):
        x = self.xcor() + 20
        y = self.ycor()
        self.penup()
        self.goto(x, y)

