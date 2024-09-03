# Pong game breakdown :
# Need Scoreboard ( sep file)
# Need to be able to detect collision between players and the "ball"
# Need to have controls for up and down movement (remember to limit it to vertical movement!!)
# Files needed: Scoreboard, player file, ball file
from turtle import Screen, Turtle
from paddle import Paddle
from Ball import Ball
import time
from scoreboard import Scoreboard

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)
screen.title("Pong")

ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.go_up,"Up")
screen.onkeypress(right_paddle.go_down,"Down")
screen.onkeypress(left_paddle.go_up,"w")
screen.onkeypress(left_paddle.go_down,"s")

game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor()>= 300 or ball.ycor()<= -300:
       ball.bounce_y()


    #Detect collision with right paddle:
    if ball.distance(right_paddle) < 50 and ball.xcor()> 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detecting a "score"(left paddle):
    if ball.xcor()>380:
        score.l_point()
        ball.reset_position()

    #Detecting a "score"(right paddle):
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()





















screen.exitonclick()



