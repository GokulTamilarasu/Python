from readline import set_completer
from turtle import *
import random
# def move_forward():
#     tim.forward(10)
# def move_backwards():
#     tim.back(10)
# def clear_drawing():
#     screen_1.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
# def clockwise():
#     tim.right(10)
# def anti_clockwise():
#     tim.left(10)
# tim=Turtle()
# screen_1.listen()
# screen_1.onkey(key='w',fun=move_forward)
# screen_1.onkey(key='s',fun=move_backwards)
# screen_1.onkey(key='a',fun=anti_clockwise)
# screen_1.onkey(key='d',fun=clockwise)
# screen_1.onkey(key='c',fun=clear_drawing)

# def create():
#     turtles={}
#     for participant in range (4):
#         turtles[participant]=Turtle()
#     return turtles
screen_1=Screen()
screen_1.bgcolor("black")
screen_1.setup(width=500,height=400)
bet=screen_1.textinput(title="make your bet",prompt="which will reach the end first ? : ")
turtle_list=[]
is_race_on=False
color_list=["violet","yellow","blue","green","red"]
ycor=[-100,-50,0,50,100]
for turtle_index in range(5):
    new_turtle=Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color_list[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=ycor[turtle_index])
    turtle_list.append(new_turtle)

if bet:
    is_race_on=True
while is_race_on:
    for turtle in turtle_list:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() > 230:
            is_race_on=False
            if turtle.pencolor() == bet:
                print("you won")
            else:
                print(f"you lose, {turtle.pencolor()} won")

screen_1.exitonclick()