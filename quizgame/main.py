
import data
#b = len(data.question_data)
#print(b)
for a in data.question_data:
    answer=input(f"{a} (True/False): ").capitalize()
    print(f"{answer}")
    print(data.question_data.value(a)[1])
    break
  