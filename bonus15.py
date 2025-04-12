"""Creating a quiz app. First decide the data structure.
We choose dictionary as data type for the quiz app"""

import json

with open ("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)


for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index+1, "-", alternative)
    user_choice = int(input("Enter your answer choice: "))
    question["user_choice"] = user_choice #adds user choice to the dictionary.

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
    message = (f'{index+1} - Your answer: {question["user_choice"]},'
               f'Correct answer: {question["correct_answer"]}')
    print(message)

#print(data)
print(score, "/", len(data))



