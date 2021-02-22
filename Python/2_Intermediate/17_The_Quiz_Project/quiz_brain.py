# Asking Questions
# Checking if answer was correct
# Checking if it is the end of the quiz

class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0


    def still_has_questions(self):
        return len(self.question_list) > self.question_number


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}. {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("This is correct!")
        else:
            print("Incorrect.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score} / {self.question_number}")
        print("\n")


