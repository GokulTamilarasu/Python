# from turtles import Player
from turtle import Screen,Turtle
from obstacles import Obstacles
import random
from turtles import Player
from turtle_crossing.turtles import Player

#variables
is_game_on=True
#screen
turtle_screen=Screen()
turtle_screen.listen()
#player
player= Player()
player.create_player()
#controls
turtle_screen.onkey(fun=player.move_forward,key='Up' )
turtle_screen.onkey(fun=player.move_left,key='Left')
turtle_screen.onkey(fun=player.move_right,key='Right')
turtle_screen.onkey(fun=player.move_down,key='Down')

#obstacles
while is_game_on:
    obstacle = Obstacles()
    obstacle.random_position()
    obstacle.speed(random.randint(10,20))
    f/home/gokul_04/Downloads/turtle-crossing-start
    obstacle.forward(20)


turtle_screen.exitonclick()
