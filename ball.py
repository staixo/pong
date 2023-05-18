from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed = 10
        self.direction = random.randint(-45, 45)
        self.goto(0, 0)

    def add_speed(self):
        self.speed += 1
    def move(self):
        self.setheading(self.direction)
        self.forward(self.speed)

    def bounce(self):
        self.direction *= -1

    def bounce_back(self):
        self.direction = (self.direction * -1) + 180
        self.direction += random.randint(-5, 5)
    def getlattitude(self):
        return self.ycor()
    def reset(self):
        self.goto(0, 0)
        self.direction = random.randint(-45, 45)
        self.speed = 10
