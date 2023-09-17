from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_paddle = 0
        self.r_paddle = 0
        self.update()

    def update(self):
        self.goto(-100, 200)
        self.write(self.l_paddle, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_paddle, align="center", font=("Courier", 80, "normal"))
    def l_score(self):
        self.l_paddle += 1
        self.clear()
        self.update()

    def r_score(self):
        self.r_paddle += 1
        self.clear()
        self.update()
