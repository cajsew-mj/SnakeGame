from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score_b
import time
screen = Screen()
screen.bgcolor("blue")
screen.setup(width=800, height=600)
screen.title("pong_game")
screen.tracer(0)

paddle1 = Paddle((-350, 0))
paddle2 = Paddle((350, 0))
ball = Ball()
scores = Score_b()
screen.onkey(paddle1.go_up, "w")
screen.onkey(paddle1.go_down, "s")
screen.onkey(paddle2.go_up, "Up")
screen.onkey(paddle2.go_down, "Down")


screen.listen()


game_is_on = True
scores.update_score_b()
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.jump()
    if ball.distance(paddle2) < 50 and ball.xcor() > 320 or ball.distance(paddle1) < 50 and ball.xcor() < -320:
        ball.reflect()
    if ball.xcor() > 380:
        ball.reset_position()
        scores.point1()
        ball.move_speed = 0.1
    if ball.xcor() < -380:
        ball.reset_position()
        scores.point2()
        ball.move_speed = 0.1
    if scores.score1 == 5 or scores.score2 == 5:
        game_is_on = False

screen.exitonclick()
