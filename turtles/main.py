from turtle import Turtle,Screen
import random
turtle_1=Turtle()
# turtle_1.shape("turtle")
# turtle_1.color("green")
# turtle_1.forward(100)
# turtle_1.right(90)
# turtle_1.forward(100)
# turtle_1.right(90)
# turtle_1.forward(100)
# turtle_1.right(90)
# turtle_1.forward(100)
# turtle_1.right(90)
# for i in range(49):
#     turtle_1.forward(10)
#     turtle_1.pendown()
#     turtle_1.forward(10)
#     turtle_1.penup()
# size=4
# color_list=['violet','indigo','blue','green','yellow','orange','red']
# while size!=11:
#     angle=360
#     color = random.choice(color_list)
#     for i in range (size):
#         turtle_1.color(color)
#         turtle_1.forward(100)
#         turtle_1.right(angle/size)
#     size+=1

angle_list=[0,90,180,270]
turtle_1.pensize(10)
color_list=['violet','indigo','blue','green','yellow','orange','red']
no=0
while no!=1000:
    color = random.choice(color_list)
    angle = random.choice(angle_list)
    turtle_1.speed(100)
    turtle_1.color(color)
    turtle_1.forward(50)
    turtle_1.setheading(angle)
    no+=1
screen=Screen()
screen.exitonclick()