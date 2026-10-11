from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen,Turtle
snake=Snake()
food=Food()
score=Scoreboard()
screen_2=Screen()
is_game_on=True
points=0
#screen setup
screen_2.setup(width=600,height=600)
screen_2.bgcolor("black")
screen_2.listen()
screen_2.tracer(0)
#wall creation
wall = Turtle()
wall.hideturtle()
wall.color("white")
wall.pensize(3)
wall.penup()
wall.goto(-280, -280)
wall.pendown()
for _ in range(2):
    wall.forward(560)  # Width of the box
    wall.left(90)
    wall.forward(520)  # Height of the box (leaves top space for score)
    wall.left(90)


screen_2.onkey(key="Up",fun=snake.upwards)
screen_2.onkey(key="Down",fun=snake.downwards)
screen_2.onkey(key="Left",fun=snake.leftwards)
screen_2.onkey(key="Right",fun=snake.rightwards)



def game_loop():
    global points
    snake.auto_move()
    # detecting food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        points+=1
        score.write_on_screen(points)
        snake.add_new_segment()
    screen_2.update()
    #wall collision check
    if snake.head.xcor()< -280:
        print("game over")
    screen_2.ontimer(fun=game_loop, t=100)
    return points



score.write_on_screen(points)


game_loop()








screen_2.exitonclick()