import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
#player
turtle_player=Player()
screen.onkey(fun=turtle_player.move,key='Up')
#cars
car=CarManager()
#scoreboard
level=Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.move_car()
    for cars in car.car_list:
        if turtle_player.distance(cars)<20:
            level.game_over()
            game_is_on=False
    if turtle_player.ycor()>280:
        turtle_player.next_level()
        screen.update()
        level.increase_level()
        car.increase_speed()



screen.exitonclick()
