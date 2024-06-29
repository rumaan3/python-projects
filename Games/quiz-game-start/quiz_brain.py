class QuizBrain:

    def __init__(self, bank):
        self.question_number = 0
        self.question_list = bank
        self.score = 0

    def more_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ans1 = input(f"Q.{self.question_number}: {current_question.text} (True/False)\n")
        if ans1 == "f":
            ans1 = "False"
        elif ans1 == "t":
            ans1 = "True"
        # print(f"Q.{self.question_number}: {current_question.text} (True/False)")
        ans1 = ans1.capitalize()
        self.check_ans(ans1, current_question.ans)

    def check_ans(self, ans, q_ans):
        if ans == q_ans:
            print("You're Right!!!")
            self.score += 1
        else:
            print("you're Wrong....")

        print(f"your total score is {self.score}/{self.question_number}\n")






