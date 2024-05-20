from turtle import Turtle


class Score_b(Turtle):
    def __init__(self):
        super().__init__()
        self.color("brown")
        self.penup()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0

    def update_score_b(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score1, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score2, align="center", font=("Courier", 80, "normal"))

    def point1(self):
        self.score1 += 1
        self.update_score_b()

    def point2(self):
        self.score2 += 1
        self.update_score_b()
