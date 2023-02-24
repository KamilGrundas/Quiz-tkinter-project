import json



class Questions():

    def __init__(self):

        with open("questions.json") as self.file:
            self.questions = json.load(self.file)

        # for i in self.questions['active_questions']:
        #     print(i['question'])

        # print(self.questions['questions'][0]['answers'][0])

        # self.save_question("Jaka jutro4 pogoda", "B4", ["faj4na", "słaba", "średnia", "dobra"])

    def delete_question(self, questions, index):
        
        removed=self.questions[questions].pop(index)

        with open("questions.json", "w") as file:
            json.dump(self.questions, file)

    def save_question(self,questions, question, correct, answers):
        

        self.questions[questions].append(
                    
                    {
                    'question': str(question),
                    'correct' : str(correct),
                    'answers': answers
                    })

        with open("questions.json", "w") as file:
            json.dump(self.questions, file)

    def move_question(self, moved, i):

        if i == 1:

            self.questions['active_questions'].append(moved)

        elif i == 2:

            self.questions['no_active_questions'].append(moved)

        with open("questions.json", "w") as file:
            json.dump(self.questions, file)



    # questions =[{
    #                 'question': "Jaka jest stolica Polski?",
    #                 'correct' : 'A',
    #                 'answers': [
    #                     "A:Warszawa",
    #                     "B:Kraków",
    #                     "C:Lublin",
    #                     "D:Poznań",
    #                 ]}
    #             ,
    #             {
    #                 'question': "Jaka jest stolica Niemiec?",
    #                 'correct': 'A',
    #                 'answers': [
    #                     "A:Berlin",
    #                     "B:Monachium",
    #                     "C:Frankfurt",
    #                     "D:Hamburg"

    #                 ]
    #             }]
    #             # Więcej pytań

    # new_question('Jaka dzispogoda?', 'C', ['A:gowno','B:gawa','C:gowadaw','D:pizda'])         




    # removed_questions = questions.pop(0)
    # print(questions[1])

    # selected_answer = "B"

    # if selected_answer == questions[0]['correct']:
    #     print("Prawidłowa odpowiedź!")
    # else:
    #     print('błędna odpowiedź!')
