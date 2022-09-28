from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1, 1)
        self.color("white")
        self.speed("fast")
        self.x_move = 10
        self.y_move = 10


    def start(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def rebote(self):
        self.y_move *= -1

    def rebote_x(self):
        self.x_move *= -1

    def restart(self):
        self.goto(0, 0)
        self.rebote_x()


