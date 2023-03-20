from question_model import Question
from data import questions
from quiz_brain import QuizBrain
import random

question_bank = []
question_data = random.choice(questions)
print(f"You are doing the {question_data['title']} Quiz")

for data in question_data["questions"]:
    text = data["question"]
    answer = data["correct_answer"]
    question = Question(text, answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz")
print(f"Your final score was {quiz.score} / {quiz.question_number}")
