from questions_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# # Testing
# for i in range(0, len(question_bank)):
#     print(f"{question_bank[i].text} - {question_bank[i].answer}")

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quizz")
print(f"Your final score is: {quiz.score} / {quiz.question_number}")