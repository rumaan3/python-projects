from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

bank1 = []
x = 1

for i in question_data:
    text = i["text"]
    ans = i["answer"]
    q = Question(text, ans)
    bank1.append(q)

a = QuizBrain(bank1)


while QuizBrain.more_questions(a):
    a.next_question()



