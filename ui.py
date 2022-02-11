from tkinter import *
# from main import question_bank
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # score
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 14, "normal"))
        self.score.grid(column=1, row=0)
        # canvas
        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.canvas.grid(column=0, columnspan=2, row=1, padx=20, pady=20)
        self.question_text = self.canvas.create_text(150, 125, width=260,
                                                     text="Some question Text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        # Buttons
        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.true_answer)
        self.right_button.grid(column=0, row=2)
        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.false_answer)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz\nYour final score was: "
                                                            f"{self.quiz.score}/{self.quiz.question_number}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_answer(self):
        user_answer = "True"
        self.give_feedback(self.quiz.check_answer(user_answer))

    def false_answer(self):
        user_answer = "False"
        self.give_feedback(self.quiz.check_answer(user_answer))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, func=self.get_next_question)
