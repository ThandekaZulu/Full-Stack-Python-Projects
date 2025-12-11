from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
  # question_text = item["text"]
  # question_answer = item["answer"]
  question_text = item["question"]
  question_answer = item["correct_answer"]
  question_object = Question(question_text,question_answer)
  question_bank.append(question_object)

quiz = QuizBrain(question_bank) 
while quiz.still_has_questions():
  quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")