
import data
#b = len(data.question_data)
#print(b)
#print(data.question_data)
#hello
score=0
question=1
for a in data.question_data:
    print(type(a))
    print(a)
    answer=input(f"{a['text']}  (True/False): ").capitalize()
    if answer==a['answer']:
        score +=1
        print(score)
        print("You got it right!")
        print(f"The correct answer was: {a['answer']}.")
        print(f"Your current score is: {score}/{question}")
    elif answer!=a['answer']:
        print("That's wrong.")
        print(f"The correct answer was: {a['answer']}.")
        print(f"Your current score is: {score}/{question}")
    question+=question
    
  