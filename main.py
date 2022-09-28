#TODO: Create the screen

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping pong")
screen.listen()
screen.tracer(0)


#TODO: Create and move a paddle

game_is_on = True

paddle = Paddle()
paddle_2 = Paddle()
paddle_2.goto(x=350, y=0)
yellow_ball = Ball()
scoreboard = Scoreboard()

time_spent = 0.08

while game_is_on:

    time.sleep(time_spent)
    screen.update()
    screen.onkey(paddle.up, "w")
    screen.onkey(paddle.down, "s")

#TODO: Create another paddle

    screen.onkey(paddle_2.up, "Up")
    screen.onkey(paddle_2.down, "Down")


#TODO: Create the ball and make it move

    yellow_ball.start()

    if yellow_ball.ycor() > 280 or yellow_ball.ycor() < -280:
        yellow_ball.rebote()

#TODO: Detect collision with wall and bouce

    if yellow_ball.distance(paddle_2) < 50 and yellow_ball.xcor() > 320:
        yellow_ball.rebote_x()
        if time_spent >= 0.01:
            time_spent *= 0.9

    elif yellow_ball.distance(paddle) < 50 and yellow_ball.xcor() < -320:
        yellow_ball.rebote_x()
        if time_spent >= 0.01:
            time_spent *= 0.9

#TODO: Detect collision with paddle

    if yellow_ball.xcor() > 380:
        yellow_ball.restart()
        scoreboard.l_point()
        time_spent = 0.075

    if yellow_ball.xcor() < -380:
        yellow_ball.restart()
        scoreboard.r_point()
        time_spent = 0.075


#TODO: Detect when paddle misses

#TODO: Keep Score

screen.exitonclick()