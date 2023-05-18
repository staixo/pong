
import turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time


sizefiled=[800,600]

humanpaddle = Paddle(5,20,sizefiled[0]/2-50)
computerpaddle = Paddle(5,20,-sizefiled[0]/2+50)

ball = Ball()
score = Score()


my_screen = turtle.Screen()
my_screen.setup(sizefiled[0],sizefiled[1])
my_screen.bgcolor("black")
my_screen.title("pong game")
my_screen.listen()
my_screen.onkey(humanpaddle.up, "z")
my_screen.onkey(humanpaddle.down, "s")
my_screen.tracer(0)

while True:
    my_screen.update()
    ball.move()
    if(ball.ycor() > sizefiled[1]/2-20 or ball.ycor() < -sizefiled[1]/2+20):
        ball.bounce()
    elif(ball.distance(computerpaddle)<50 and ball.xcor()< -sizefiled[0]/2+100):  # computer paddle is on the left
        ball.add_speed()
        ball.bounce_back()
    elif(ball.distance(humanpaddle)<50 and ball.xcor()> sizefiled[0]/2-100):  # human paddle is on the right
        ball.add_speed()
        ball.bounce_back()
    elif(ball.xcor() > sizefiled[0]/2-20):
        ball.reset()
        score.addrscore()  # score for the right paddle
        my_screen.update()
    elif(ball.xcor() < -sizefiled[0]/2+20):
        ball.reset()
        score.addlscore()  # score for the left paddle
        my_screen.update()
    if(score.getmax()>=3):
        break
    if(ball.ycor()>(computerpaddle.ycor()+50)):
        computerpaddle.up()
    if(ball.ycor()<(computerpaddle.ycor()-50)):
        computerpaddle.down()
    time.sleep(0.1)
my_screen.exitonclick()




