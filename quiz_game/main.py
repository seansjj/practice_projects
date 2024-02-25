from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question.get('text')
    question_answer = question.get('answer')

    quiz_questions = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(quiz_questions)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print('You completed the quiz!')
print(f'Your final score was {quiz.user_score}/{len(quiz.question_list)}.')
