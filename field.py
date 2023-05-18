import ball
import score
import paddle
balloon = ball.ball()

class pongfiled():
    def __init__(self,level):
        self.width = 800
        self.height = 600
        self.level = level
        self.balloon = ball.ball()
        self.scoreright = score.score()
        self.scoreleft = score.score()
        self.paddleleft = paddle.paddle(20,1,-self.width/2)
        self.paddleright = paddle.paddle(20,1,+self.width/2)



        