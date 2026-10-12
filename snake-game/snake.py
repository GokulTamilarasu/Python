from turtle import Turtle

INITIAL_POSITIONS=[0,-20,-40]
class Snake:
    def __init__(self):
        self.segments_list=[]
        self.create_snake()
        self.head=self.segments_list[0]
        self.tail=self.segments_list[-1]




    def create_snake(self):
        for segment_index in range(3):
            new_segment = Turtle()
            new_segment.color("white")
            new_segment.shape("circle")
            new_segment.penup()
            new_segment.setx(INITIAL_POSITIONS[segment_index])
            self.segments_list.append(new_segment)

    def upwards(self):
        segment =self.segments_list[0]
        if self.head.heading() != 270:
            segment.setheading(90)

    def downwards(self):
        segment = self.segments_list[0]
        if self.head.heading() != 90:
            segment.setheading(270)

    def leftwards(self):
        segment = self.segments_list[0]
        if self.head.heading() != 0:
            segment.setheading(180)

    def rightwards(self):
        segment = self.segments_list[0]
        if self.head.heading() != 180:
            segment.setheading(0)

    def auto_move(self):
        for seg_index in range(len(self.segments_list) - 1, 0, -1):
            new_xcor =self.segments_list[seg_index - 1].xcor()
            new_ycor =self.segments_list[seg_index - 1].ycor()
            self.segments_list[seg_index].goto(x=new_xcor, y=new_ycor)
        self.head.forward(20)

    def add_new_segment(self):
        new_segment = Turtle()
        new_segment.hideturtle()
        new_segment.shape("circle")
        new_segment.color("white")
        new_segment.penup()
        new_pos=self.segments_list[-1].position()
        new_segment.goto(new_pos)
        self.segments_list.append(new_segment)
        new_segment.showturtle()
        self.tail=self.segments_list[-1]

    def hide_snake(self):
        for segment in self.segments_list:
            segment.hideturtle()
