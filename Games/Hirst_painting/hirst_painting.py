import colorgram
from turtle import Turtle, Screen
import random
import turtle


def extract():
    colors = colorgram.extract("image.jpg", 20)
    hirst_colors = []

    for i in colors:
        r = i.rgb.r
        g = i.rgb.g
        b = i.rgb.b
        rgb_tuple = (r, g, b)
        hirst_colors.append(rgb_tuple)

    return hirst_colors


def paint_it(colors):

    turtle.colormode(255)
    a = Turtle()
    a.shape("arrow")
    a.speed(5)
    a.pensize(20)

    x = -300
    y = -300
    p = 50
    i = 1

    a.teleport(x, y)

    for z in range(1, 100):
        b = random.choice(colors)
        a.dot(20, b)
        a.penup()
        a.forward(50)
        a.pendown()
        if z % 10 == 0:
            d = y + (i*p)
            a.teleport(x, d)
            i += 1

    s = Screen()
    s.exitonclick()


a = extract()
paint_it(a)


