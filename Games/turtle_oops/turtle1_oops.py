from turtle import Turtle, Screen
import random

a = Turtle()
b = Turtle()

a.shape("turtle")
a.color("blue")
a.speed(5)
a.pensize(10)
color = ["red", "blue", "green", "yellow", "orange"]
# b.shape("arrow")
# b.color("red")
i = 30

direction = [0, 90, 180, 360]
# print (c)
while i:
    d = random.choice(color)
    e = random.choice(direction)
    a.color(d)
    a.forward(i)
    a.setheading(e)


    # i += 10

s = Screen()
s.exitonclick()

