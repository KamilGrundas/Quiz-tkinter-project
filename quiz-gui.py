import random
import linecache
from tkinter import *
root = Tk()
root.title("Quiz")
root.geometry("1200x700")
root.config(background='#de9518')

steps = 0

if steps == 0:
    questions = str('easy_questions.txt')
if steps == 3:
    questions = str('medium_questions.txt')
if steps == 6:
    questions = str('hard_questions.txt')

def questions_place():
    #Draw questions
    random_question1 = random.randrange(0,35,6)
    random_question2 = random.randrange(0,35,6)
    random_question3 = random.randrange(0,35,6)

    while random_question2 == random_question1:
        random_question2 = random.randrange(0,35,6)
    while random_question3 == random_question1 or random_question3 == random_question2:
        random_question3 = random.randrange(0,35,6)

    if steps == 0 or steps == 3 or steps == 6:
        random_question = random_question1
    if steps == 1 or steps == 4 or steps == 7:
        random_question = random_question2
    if steps == 2 or steps == 5 or steps ==8:
        random_question = random_question3




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

def hard_level():

    #Define medium level label
    hard = Label(root,
                text="Poziom trudny",
                font=('Gill Sans Ultra Bold', 30),
                fg='#ad0909',
                bg='black',
                relief=SUNKEN,
                padx=10)
    
    medium.destroy()
    hard.place(x=600,y=50, anchor=CENTER)



def start():
    button_start.destroy()
    easy_level()



button_start = Button(root,
                        text='Kliknij, aby rozpocząć!',
                        command = start,
                        pady=100,
                        font='Arial')

button_start.place(x=600, y=300,anchor=CENTER, width=500)


root.mainloop()