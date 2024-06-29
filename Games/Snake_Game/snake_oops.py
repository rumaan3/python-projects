from turtle import Turtle

POS = [(0, 0), (-20, 0), (-40, 0)]
SPID = 20
class Snake:

    def __init__(self):
        self.sneks = []
        self.make_sneks()
        self.head = self.sneks[0]

    def make_sneks(self):
        for i in POS:
            self.add_snek(i)

    def add_snek(self, i):
        snek = Turtle("square")
        snek.color("white")
        snek.penup()
        snek.goto(i)
        self.sneks.append(snek)

    def extend(self):
        self.add_snek(self.sneks[-1].pos())

    def move(self):

        for i in range(len(self.sneks) - 1, 0, -1):
            newx = self.sneks[i - 1].xcor()
            newy = self.sneks[i - 1].ycor()
            self.sneks[i].goto(newx, newy)


        self.head.forward(SPID)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def left(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

