from turtle import Turtle, Screen
import time
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic("pong_bg.gif")
screen.title("The Pong Game")
screen.tracer(0)
paddles = []

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

# key binding
screen.listen()
screen.onkey(r_paddle.up, key="Up")
screen.onkey(r_paddle.down, key="Down")
screen.onkey(l_paddle.up, key="w")
screen.onkey(l_paddle.down, key="s")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with the upper and lower x, y axis
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # when ball go outside of the surface
    # l_paddle
    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_point()
    # r_paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


screen.exitonclick()
