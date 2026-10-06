from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank=[]
for item in question_data:
    question=Question(item['text'],item['answer'])
    question_bank.append(question)
print(question_bank)


if question_number > len(question_list):
    return False
return True 