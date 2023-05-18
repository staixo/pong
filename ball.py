from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed = 0.1
        self.direction = random.randint(-45,45)
        self.goto(0,0)
    def move(self):
        self.forward(self.speed)
        self.setheading(self.direction)
    def bounce(self):
        self.direction = self.direction * -1

    def bounce_back(self):
        self.direction = self.direction * -1 + 90
        self.direction = self.direction + random.randint(-5,5)

    def reset(self) -> None:
        return super().reset()
