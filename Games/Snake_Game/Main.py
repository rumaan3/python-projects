from turtle import Screen, Turtle
from snake_oops import Snake
import time
from food import Food
from score import Score


s = Screen()
f = Food()
scor = Score()

s.setup(height=600, width=600)
s.bgcolor("black")
s.title("Welcome to snake game")
s.tracer(0)

snake = Snake()

s.listen()
s.onkey(snake.up, "w")
s.onkey(snake.down, "a")
s.onkey(snake.left, "s")
s.onkey(snake.right, "d")

flag = True

while flag:
    s.update()
    time.sleep(.1)
    snake.move()


    #collision with food

    if snake.head.distance(f) < 15:
        f.refresh()
        snake.extend()
        scor.add_score()

    #collision with tail
    for i in snake.sneks:
        if i == snake.head:
            pass
        elif snake.head.distance(i) < 10 :
            flag = False
            scor.gameover()

    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scor.gameover()
        flag = False

s.exitonclick()