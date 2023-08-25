from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(x_cor, y_cor)


    def go_up(self):
        new_y_coordinate = self.ycor() + 20
        self.goto(self.xcor(), new_y_coordinate)


    def go_down(self):
        new_y_coordinate = self.ycor() - 20
        self.goto(self.xcor(), new_y_coordinate)