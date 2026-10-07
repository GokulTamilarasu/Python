from turtle import Turtle,Screen,colormode
import random
import colorgram
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

# angle_list=[0,90,180,270]
# turtle_1.pensize(10)
# color_list=['violet','indigo','blue','green','yellow','orange','red']
# no=0
# while no!=1000:
#     color = random.choice(color_list)
#     angle = random.choice(angle_list)
#     turtle_1.speed(100)
#     turtle_1.color(color)
#     turtle_1.forward(50)
#     turtle_1.setheading(angle)
#     no+=1
# def rand_colors():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     color=(r,g,b)
#     return color
#
# color_tuple=rand_colors()
# i=0
# turtle_1.speed(100)
# while i!=100:
#     turtle_1.color(color_tuple)
#     turtle_1.circle(100)
#     current = turtle_1.heading()
#     turtle_1.setheading(current +10)
#     i+=1
#
# colors=[]
# list_colors=colorgram.extract('image.jpeg',15)
# for color in list_colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     colors.append((r,g,b))
# print(colors)
colormode(255)
list_colors=[(198, 159, 116), (70, 92, 129), (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154)]
turtle_1.hideturtle()
white=(255,255,255)
turtle_1.setheading(225)
turtle_1.penup()
turtle_1.forward(400)
turtle_1.setheading(0)
number_dots=0
turtle_1.speed(100)
while number_dots!=100:
    color=random.choice(list_colors)
    turtle_1.color(color)
    turtle_1.dot(20)
    turtle_1.pendown()
    turtle_1.penup()
    turtle_1.forward(50)
    number_dots+=1
    if number_dots%10==0:
        turtle_1.setheading(90)
        turtle_1.forward(50)
        turtle_1.setheading(180)
        turtle_1.forward(500)
        turtle_1.setheading(0)
screen=Screen()
screen.exitonclick()
