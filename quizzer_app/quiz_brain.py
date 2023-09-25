from data import NUM_OF_QS


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.progress = True
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        if self.question_number < NUM_OF_QS:
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            # self.progress = True
            return f"Q.{self.question_number}: {self.current_question.text} (True/False): "
        else:
            self.progress = False
            return f"End of the Quiz\nYour Score is {self.score}/{NUM_OF_QS}"

            # user_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")
            # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if self.progress:
            if user_answer.lower() == correct_answer.lower():
                self.score += 1
                print("You got it right!")
                return True
            else:
                print("That's wrong.")
                return False

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
