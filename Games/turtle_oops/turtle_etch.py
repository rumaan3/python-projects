import random
import turtle
from turtle import Turtle, Screen

a = Turtle()
s = Screen()

def move_forward():
    a.forward(10)
def backwards():
    a.backward(10)

def left():
    a.left(10)

def right():
    a.right(10)

def clear():
    a.clear()
    a.penup()
    a.home()
    a.pendown()

s.listen()

s.onkey( move_forward, "w")
s.onkey( backwards, "s")
s.onkey( left, "a")
s.onkey( right, "d")
s.onkey( clear, "c")

s.exitonclick()

