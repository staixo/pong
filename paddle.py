from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,size,speed,x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(size,1)
        self.penup()
        self.goto(x,0)
        self.speed = speed

    def up(self):
        new_y = self.ycor() + self.speed
        if new_y < 250:  
            self.sety(new_y)

    def down(self):
        new_y = self.ycor() - self.speed
        if new_y > -250:  
            self.sety(new_y)
    def getlattitude(self):
        return self.ycor()
    def changespeed(self,speed):
        self.speed = speed
