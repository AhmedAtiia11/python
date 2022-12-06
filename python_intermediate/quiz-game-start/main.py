from question_model import questionmodel
from quiz_brain import quizbrain
from data import question_data
from random import choice

#Initial  values
points=0
cont=True
number=1


while cont:
    choosen_question =choice(question_data)
    quest=questionmodel(choosen_question["text"],choosen_question["answer"])
    print(f"q.{number}:{choosen_question['text']}")
    print(f'The answer is (for development):{ choosen_question["answer"] }')
    answer=quest.user_answer.lower()
    user_answer=input("true or false : ")
    check=quizbrain(answer,user_answer,points,number)
    
    #to save values from the last turn
    points=check.user_points
    cont=check.cont
    number=check.question_number