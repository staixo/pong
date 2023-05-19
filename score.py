from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Courier", 80, "normal"))
        self.goto(0, 150)
        self.write("highest score is : " + str(self.get_highscore())+ " - 3", align="center", font=("Courier", 20, "normal"))

    def addlscore(self):
        self.lscore += 1
        self.update_score()
        if(self.lscore >= self.get_highscore()):
            self.update_highscore(self.lscore)

    def addrscore(self):
        self.rscore += 1
        self.update_score()
    def getmax(self):
        return self.rscore
    
    def get_highscore(self):
        with open("pong\score.txt") as f:
            return int(f.read())

    def update_highscore(self, score):
        with open("pong\score.txt", "w") as f:
            f.write(str(score))
        self.update_score()