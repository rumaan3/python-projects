from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.update_Score()

    def update_Score(self):
        self.write(f"score: {self.score}", align='center', font=('Arial', 20, 'normal'))
    def add_score(self):
        self.clear()
        self.score += 1
        self.update_Score()

    def gameover(self):
        self.home()
        self.write("GAME OVER!!", align='center', font=('Arial', 20, 'normal'))