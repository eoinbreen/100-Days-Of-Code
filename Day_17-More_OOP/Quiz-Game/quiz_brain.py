class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text}. (True/False)? ")
        while not user_answer == "True" and not user_answer == "False":
            user_answer = input("That is not a valid answer, please choose True or False: ")

        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print(f"You got it right, the answer was {correct_answer}. ")
            self.score += 1
            print(f"Your current score is {self.score} / {self.question_number}")
        else:
            print(f"You got it wrong, the answer was {correct_answer}. ")
            print(f"Your current score is {self.score} / {self.question_number}")

        print("\n")
