#TODO: asking the question
#TODO: checking if the answer given is right
#TODO: cheking if we are at the end of the quiz.

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0



    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        your_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/ False)? ").lower()
        self.question_number += 1
        self.check_answer(your_answer, current_question.answer)

    def check_answer(self, your_answer, correct_answer):
        if your_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wong.")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
