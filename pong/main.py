#pong game
#two users user class
#ball class needed
#scoreboard class
#x=450,y=1000
import time
from turtle import Turtle,Screen
from user import User
from scorecard import Scorecard
from ball import Ball
#initial screen setup
pong_screen=Screen()
pong_screen.bgcolor("black")
pong_screen.tracer(0)
#middle intersection
border_length=0
border=Turtle()
border.color("white")
border.shape("square")
border.penup()
border.hideturtle()
border.goto(x=0,y=450)
border.setheading(-90)
border.pensize(15)
border.pendown()
while border_length !=-320:
    border.pendown()
    border.forward(10)
    border.penup()
    border.forward(20)
    border_length-=10
#controls
user_1=User()
user_1.goto(x=450,y=0)
user_2=User()
user_2.goto(x=-450,y=0)
pong_screen.listen()
pong_screen.onkey(key="Up",fun=user_1.user_up)
pong_screen.onkey(key="Down",fun=user_1.user_down)
pong_screen.onkey(key="w",fun=user_2.user_up)
pong_screen.onkey(key="s",fun=user_2.user_down)
#scorecard
score_1=Scorecard()
score_2=Scorecard()
#game loop
is_game_on=True
ball=Ball()
#scoreboard
points_1 = 0
points_2 = 1
score_1.goto(-200, 470)
score_2.goto(200, 470)
score_1.score_display(points=points_1)
score_2.score_display(points=points_2)
while is_game_on:
    ball.ball_move()
    time.sleep(0.5)
    if ball.ycor() >=-450 or ball.ycor() >=450:
        ball.y_change()
    elif ball.distance(user_1) <5 :
        ball.x_change()
        ball.y_change()
    elif ball.distance(user_2) <5:
        ball.x_change()
        ball.y_change()
    pong_screen.update()

pong_screen.exitonclick()