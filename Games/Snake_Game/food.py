from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rx = random.randint(-250, 250)
        ry = random.randint(-250, 250)
        self.teleport(rx, ry)

