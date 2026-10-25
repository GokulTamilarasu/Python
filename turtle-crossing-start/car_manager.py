import random
from  turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    def __init__(self):
        self.car_list=[]
        self.car_speed=STARTING_MOVE_DISTANCE



    def create(self):
        chance=random.randint(1,6)
        if chance==1:
            new_car=Turtle()
            new_car.shape("square")
            new_car.turtlesize(stretch_wid=2, stretch_len=4)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(x=300, y=random.randint(-250, 260))
            self.car_list.append(new_car)

    def move_car(self):
         for car in self.car_list:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed+=MOVE_INCREMENT