from turtle import Screen, Turtle
import random

def random_pace():
    i = 0
    i = random.randint(1,10)
    return i

def random_turtle(turtles):
    random_turtle = random.choice(turtles)
    return random_turtle

def race():
    flag = True
    while flag:
        x = random_turtle(turtles)
        p = random_pace()
        x.forward(p)

        if x.xcor() > 200.0:
            flag = False
            print (x.color())
    return x.color()

a = Turtle()
b = Turtle()
c = Turtle()
d = Turtle()
e = Turtle()
s = Screen()

colors = ["red","blue","green","yellow","orange"]
turtles = [a, b, c, d, e]

b = 40
for i in turtles:
    i.teleport(x=-300, y=b)
    b -= 20

a=0
for i in turtles:
    i.color(colors[a])
    a += 1

w = race()

print (f"the winner is {w}")


s.listen()
s.onkey(race,"space")

s.exitonclick()

