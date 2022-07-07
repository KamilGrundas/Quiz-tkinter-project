import random
import linecache
from tkinter import *
root = Tk()
root.title("Quiz")
root.geometry("1200x700")
root.config(background='#de9518')

user_score = 0
steps = 0

            #Draw questions
random_question1 = random.randrange(0,35,6)
random_question2 = random.randrange(0,35,6)
random_question3 = random.randrange(0,35,6)

while random_question2 == random_question1:
    random_question2 = random.randrange(0,35,6)
while random_question3 == random_question1 or random_question3 == random_question2:
    random_question3 = random.randrange(0,35,6)



def questions_place():
    global random_question
    global good_answer
    global quest_label
    global steps
    global questions

    if steps == 0:
        questions = str('easy_questions.txt')
    if steps == 3:
        questions = str('medium_questions.txt')
    if steps == 6:
        questions = str('hard_questions.txt')


    if steps == 0 or steps == 3 or steps == 6:
        random_question = random_question1
    if steps == 1 or steps == 4 or steps == 7:
        random_question = random_question2
    if steps == 2 or steps == 5 or steps ==8:
        random_question = random_question3
    
    quest = linecache.getline(questions, random_question + 1)
    quest_label = Label(root, 
                    text = quest,
                    font = ('Gill Sans Ultra Bold',15,'bold'),
                    fg='#5cfcff',
                    bg='black',
                    relief = SUNKEN,
                    pady = 10,
                    width=50)

    quest_label.place(x=600,y=150, anchor=CENTER)
    
    good_answer = linecache.getline(questions, random_question + 6)
def next_exit_buttons():

    global button_nq
    global button_exit

    button_nq = Button(root,
                        text = "Następne pytanie",
                        font=('Gill Sans Ultra Bold',15,'bold'),
                        background='white',
                        padx=10,
                        pady=10,
                        disabledforeground='black',
                        command=next_question,
                        state = DISABLED)
    button_exit = Button(root,
                        text = "Zakończ",
                        font=('Gill Sans Ultra Bold',15,'bold'),
                        background='white',
                        padx=10,
                        pady=10,
                        disabledforeground='black',
                        command=exit,
                        state = DISABLED)

    button_nq.place(x=600,y=600, anchor=CENTER)

def answers_place():
    global button_A
    global button_B
    global button_C
    global button_D
    global button_nq
    global questions
    global button_exit
    ans1 = linecache.getline(questions, random_question + 2)
    ans2 = linecache.getline(questions, random_question + 3)
    ans3 = linecache.getline(questions, random_question + 4)
    ans4 = linecache.getline(questions, random_question + 5)
    button_A = Button(root,
                        text = ans1,
                        font=('Gill Sans Ultra Bold',15,'bold'),
                        background='white',
                        padx=10,
                        pady=10,
                        disabledforeground='black',
                        command=lambda: check_answer(1))
    button_B = Button(root,
                        text = ans2,
                        font=('Gill Sans Ultra Bold',15,'bold'),
                        background='white',
                        padx=10,
                        pady=10,
                        disabledforeground='black',
                        command=lambda: check_answer(2))
    button_C = Button(root,
                        text = ans3,
                        font=('Gill Sans Ultra Bold',15,'bold'),
                        background='white',
                        padx=10,
                        pady=10,
                        disabledforeground='black',
                        command=lambda: check_answer(3))
    button_D = Button(root,
                        text = ans4,
                        font=('Gill Sans Ultra Bold',15,'bold'),
                        background='white',
                        padx=10,
                        pady=10,
                        disabledforeground='black',
                        command=lambda: check_answer(4))


    button_A.place(x=300, y=300,anchor=CENTER)
    button_B.place(x=900, y=300,anchor=CENTER)
    button_C.place(x=300, y=450,anchor=CENTER)
    button_D.place(x=900, y=450,anchor=CENTER)
    button_nq.config(state=DISABLED)


def check_answer(ans):
    button_A.config(background='red',state=DISABLED)
    button_B.config(background='red',state=DISABLED)
    button_C.config(background='red',state=DISABLED)
    button_D.config(background='red',state=DISABLED)
    global user_score
    if int(good_answer) == 1:
        button_A.config(background='green')
    if int(good_answer) == 2:
        button_B.config(background='green')
    if int(good_answer) == 3:
        button_C.config(background='green')
    if int(good_answer) == 4:
        button_D.config(background='green')
    if int(good_answer) == ans:
        user_score += 10
    


    if steps == 8:
        button_exit.config(state=ACTIVE)
    else:
        button_nq.config(state=ACTIVE)




def next_question():
    global random_question1
    global random_question2
    global random_question3
    global steps
    steps += 1
    quest_label.destroy()
    button_A.destroy()
    button_B.destroy()
    button_C.destroy()
    button_D.destroy()
    if steps == 3:
            #Draw questions
        random_question1 = random.randrange(0,35,6)
        random_question2 = random.randrange(0,35,6)
        random_question3 = random.randrange(0,35,6)

        while random_question2 == random_question1:
            random_question2 = random.randrange(0,35,6)
        while random_question3 == random_question1 or random_question3 == random_question2:
            random_question3 = random.randrange(0,35,6)

    if steps == 6:

            #Draw questions
        random_question1 = random.randrange(0,35,6)
        random_question2 = random.randrange(0,35,6)
        random_question3 = random.randrange(0,35,6)

        while random_question2 == random_question1:
            random_question2 = random.randrange(0,35,6)
        while random_question3 == random_question1 or random_question3 == random_question2:
            random_question3 = random.randrange(0,35,6)

    if steps == 0 or steps == 1 or steps == 2:
        easy_level()
    if steps == 3 or steps == 4 or steps == 5:
        medium_level()
    if steps == 6 or steps == 7 or steps ==8:
        hard_level()
    print(steps)
    if steps == 8:
        button_nq.destroy()
        button_exit.place(x=600,y=600, anchor=CENTER)

def exit():
    root.destroy()


def easy_level():
    global easy
    #Define easy level label
    easy = Label(root,
                text="Poziom łatwy",
                font=('Gill Sans Ultra Bold', 30),
                fg='#4e8c0b',
                bg='black',
                relief=SUNKEN,
                padx=10)

    easy.place(x=600,y=50, anchor=CENTER)
    questions_place()
    answers_place()

def medium_level():
    global medium
    #Define medium level label
    medium = Label(root,
                text="Poziom średni",
                font=('Gill Sans Ultra Bold', 30),
                fg='#f7720c',
                bg='black',
                relief=SUNKEN,
                padx=10)
    
    easy.destroy()
    medium.place(x=600,y=50, anchor=CENTER)
    questions_place()
    answers_place()

def hard_level():

    #Define hard level label
    hard = Label(root,
                text="Poziom trudny",
                font=('Gill Sans Ultra Bold', 30),
                fg='#ad0909',
                bg='black',
                relief=SUNKEN,
                padx=10)
    
    medium.destroy()
    hard.place(x=600,y=50, anchor=CENTER)
    questions_place()
    answers_place()



def start():
    button_start.destroy()
    next_exit_buttons()
    easy_level()



button_start = Button(root,
                        text='Kliknij, aby rozpocząć!',
                        command = start,
                        pady=100,
                        font='Arial')

button_start.place(x=600, y=300,anchor=CENTER, width=500)


root.mainloop()