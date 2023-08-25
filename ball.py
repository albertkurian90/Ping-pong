from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        # self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.x_indent = 10
        self.y_indent = 10
        self.movement_factor = 0.1

    def move(self):
        x_cor = self.xcor() + self.x_indent
        y_cor = self.ycor() + self.y_indent
        self.goto(x_cor, y_cor)

    def y_bounce(self):
        self.y_indent *= -1

    def x_bounce(self):
        self.movement_factor *= 0.9
        self.x_indent *= -1

    def reset_position(self):
        self.home()
        self.x_bounce()
        self.movement_factor = 0.1

