from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.goto(-100,200)
        self.write(self.lscore, align="center", font=("Courier", 70, "normal"))
        self.goto(100,200)
        self.write(self.rscore, align="center",font = ("Courier", 70, "normal"))

    def l_point(self):
        self.lscore += 1
        self.update()

    def r_point(self):
        self.rscore += 1
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Courier", 70, "normal"))
