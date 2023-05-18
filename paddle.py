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
        self.sety(self.ycor() + self.speed)
    def down(self):
        self.sety(self.ycor() - self.speed)
    def changespeed(self,speed):
        self.speed = speed
