import json


def new_question(question, correct, answers):
    
    questions.append({
                'question': str(question),
                'correct' : str(correct),
                'answers': answers
                })





questions =[{
                'question': "Jaka jest stolica Polski?",
                'correct' : 'A',
                'answers': [
                    "A:Warszawa",
                    "B:Kraków",
                    "C:Lublin",
                    "D:Poznań",
                ]}
            ,
            {
                'question': "Jaka jest stolica Niemiec?",
                'correct': 'A',
                'answers': [
                    "A:Berlin",
                    "B:Monachium",
                    "C:Frankfurt",
                    "D:Hamburg"

                ]
            }]
            # Więcej pytań

new_question('Jaka dzispogoda?', 'C', ['A:gowno','B:gawa','C:gowadaw','D:pizda'])         

with open("questions.json", "w") as file:
    json.dump(questions, file)


removed_questions = questions.pop(0)
print(questions[1])

selected_answer = "B"

if selected_answer == questions[0]['correct']:
    print("Prawidłowa odpowiedź!")
else:
    print('błędna odpowiedź!')


