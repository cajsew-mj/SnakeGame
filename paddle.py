from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.setheading(90)
        self.penup()
        self.shapesize = self.shapesize(1, 5)
        self.goto(position)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)


