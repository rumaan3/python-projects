import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
a = Turtle()

a.shape("turtle")
a.speed(0)
a.pensize(0)

def rand_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    c1 = (r, g, b)
    return c1

# b.shape("arrow")
# b.color("red")
i = 100
n = 10

while i:

    a.color(rand_color())
    a.circle(i)
    a.right(3)
    if a.heading() == 0.0:
        i = 0

    # i += 10

s = Screen()
s.exitonclick()

