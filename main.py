
import turtle
from paddle import Paddle
from ball import Ball
from score import Score

sizefiled=[800,600]

humanpaddle = Paddle(5,0.3,sizefiled[0]/2-50)
computerpaddle = Paddle(5,0.3,-sizefiled[0]/2+50)

ball = Ball()
score = Score()


my_screen = turtle.Screen()
my_screen.setup(sizefiled[0],sizefiled[1])
my_screen.bgcolor("black")
my_screen.title("pong game")
my_screen.listen()
my_screen.onkey(humanpaddle.up(), "z")
my_screen.onkey(humanpaddle.down(), "s")
my_screen.tracer(0)

while True:
    
    score.update_score()
    ball.move()
    if(ball.ycor() > sizefiled[1]/2-20 or ball.ycor() < -sizefiled[1]/2+20):
        ball.bounce()
    if(ball.xcor() > sizefiled[0]/2-20):
        ball.reset()
        score.addrscore
        my_screen.update()
    if(ball.xcor() < -sizefiled[0]/2+20):
        ball.reset()
        score.addlscore
        my_screen.update()
    if(ball.distance(computerpaddle)<50 and ball.xcor()>-sizefiled[0]/2+50):
        ball.bounce_back()
    if(ball.distance(humanpaddle)<50 and ball.xcor()<-sizefiled[0]/2+50):
        ball.bounce_back()
    if(score.getmax()>3):
        break
my_screen.exitonclick()


