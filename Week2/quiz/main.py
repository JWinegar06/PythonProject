from question_model import Question
from data import question_data
from da_quiz import Quiz

question_bank = []

for q in question_data:
    question = Question(q["question"], q["correct_answer"])
    question_bank.append(question)

quiz = Quiz(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Quiz complete!")
print(f"Final score: {quiz.score}/{quiz.question_number}")
