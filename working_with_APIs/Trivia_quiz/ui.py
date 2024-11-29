from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
Score = 0


def check_answer(self, a:bool):
    global Score
    q_ans = self.quiz.check_answer(a)
    if q_ans:
        self.canvas.itemconfig(bg="green")
    else:
        self.canvas.itemconfig(bg="red")

    Score = self.quiz.score

class QuizInterface:

    def __init__(self, quiz_question: QuizBrain):
        self.quiz = quiz_question
        self.window = Tk()
        self.window.title("Quizzels")

        self.window.minsize(width=500, height=700)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score = {Score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=400, height=450, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.question = self.canvas.create_text(200, 225, text="", font=("Arial", 20, "italic"), fill="black" , width=380)

        # ------------- BUTTONS ---------

        correct_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")

        self.correct_button = Button(image=correct_image, highlightthickness=0)
        self.correct_button.grid(row=2, column=1)

        self.wrong_button = Button(image=wrong_image, highlightthickness=0)
        self.wrong_button.grid(row=2, column=0)

        self.correct_button.config(command=check_answer(self,True))
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)


