from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question.get("question")
    question_answer = question.get("correct_answer")
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)


# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# If your data is trapped in a list nested in a dictionary, use get.
# https://stackoverflow.com/questions/34818782/iterate-through-nested-json-object-and-get-values-with-python
# is a good example of the issue.
