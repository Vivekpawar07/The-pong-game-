from turtle import Turtle
import random

AUTO_MOVES = [-20, 20]


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        if self.ycor() <= 200:
            y_pos = self.ycor() + 20
            self.goto(self.xcor(), y_pos)

    def down(self):
        if self.ycor() >= -200:
            y_pos = self.ycor() - 20
            self.goto(self.xcor(), y_pos)



