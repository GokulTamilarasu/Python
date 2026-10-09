from snake import Snake
from food import Food
snake=Snake()
food=Food()
is_game_on=True
snake.screen_2.setup(width=300,height=300)
snake.screen_2.bgcolor("black")
snake.screen_2.listen()
# segments_list=[]
# Initial_position=[0,20,40]
# for segment_index in range(3):
#     new_segment=Turtle()
#     new_segment.color("white")
#     new_segment.shape("circle")
#     new_segment.penup()
#     new_segment.setx(Initial_position[segment_index])
#     segments_list.append(new_segment)


snake.screen_2.onkey(key="Up",fun=snake.upwards)
snake.screen_2.onkey(key="Down",fun=snake.downwards)
snake.screen_2.onkey(key="Left",fun=snake.leftwards)
snake.screen_2.onkey(key="Right",fun=snake.rightwards)


#detecting food collision
def game_loop():
    snake.auto_move()
    if snake.head.distance(food) < 15:
        print("nom")
    snake.screen_2.ontimer(fun=game_loop, t=100)



game_loop()








snake.screen_2.exitonclick()