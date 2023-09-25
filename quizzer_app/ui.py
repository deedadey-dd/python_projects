from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Trivia Quiz!!!")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20, width=300, height=250)
        self.score_label = Label(text=f"Score: {quiz_brain.score}/{quiz_brain.question_number}", bg=THEME_COLOR, foreground="white", font=("Ariel", 14, "normal"))
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(bg="white", highlightthickness=0)
        self.q_text = self.canvas.create_text(190, 125, fill=THEME_COLOR,
                                         text="Questions here. This is the day that the Lord has made; we will "
                                              "rejoice and be glad in it", font=("Arial", 20, "italic"), width=350)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0,
                                  borderwidth=0, pady=20, padx=20, bg=THEME_COLOR, command=self.answer_true)
        self.true_button.grid(row=3, column=0)
        self.false_button = Button(image=false_image, highlightthickness=0,
                                   borderwidth=0 ,padx=20, pady=20, command=self.answer_false)
        self.false_button.grid(row=3, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.progress:
            quest_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=quest_text)
        else:
            self.true_button.configure(state="disabled")
            self.false_button.configure(state="disabled")

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.update_scores()
        self.give_feedback(is_right)
        # self.get_next_question()

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.update_scores()
        self.give_feedback(is_right)
        # self.get_next_question()

    def update_scores(self):
        self.score_label.configure(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.canvas.after(1000, self.get_next_question)

    def white_canvas(self):
        self.canvas.configure(bg="white")
