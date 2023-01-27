from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
# x = 0
for item in question_data:
    current_question = Question(item["question"], item["correct_answer"])
    question_bank.append(current_question)

# for item in question_bank:
#     print(item)

# print(question_bank)
# print(question_bank[11])

# print(len(question_bank))
# print(f"{question_bank[5].text}\n{question_bank[11].answer}")
quiz_ques = QuizBrain(question_bank)

while quiz_ques.still_has_questions():
    quiz_ques.next_question()

print(f"You have completed the quiz.")
print(f"Your final score was: {quiz_ques.score}/{quiz_ques.question_number}")
