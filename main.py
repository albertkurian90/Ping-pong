import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

is_game_on = True
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()


def refresh():
    screen.update()


screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

while is_game_on:
    time.sleep(ball.movement_factor)
    ball.move()

    # ball bounce from wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    # ball bounce from paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or \
            (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.x_bounce()

    # ball out of bounds of right player
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.update_l_score()
    # ball out of bounds of left player
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.update_r_score()
    refresh()

screen.exitonclick()
