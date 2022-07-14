import random
import linecache
from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Quiz")
root.iconbitmap('icon.ico')
w = 1200
h = 700
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
x = (ws/2) - (w/2)
y = ((hs-100)/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(False, False)
root.config(background='#FEDE27')

#Menu logo open
head_menu = Image.open("head_.png")
#Menu logo resize
resized_head = head_menu.resize((500,350), Image.Resampling.LANCZOS)
#Menu logo define and place
head_to_label = ImageTk.PhotoImage(resized_head)
head_menu_label = Label(root, image=head_to_label,borderwidth=0)
head_menu_label.place(x=630, y=180, anchor=CENTER)

user_score = 0
steps = 0

def language_def(numb):
    global language
    global lang

    if numb == 1:
        language = str('en-lang.txt')
        lang = 1
    if numb == 2:
        language = str('pl-lang.txt')
        lang = 2

    button_english.destroy()
    button_polish.destroy()
    main_menu()


def draw_questions():  #Draw questions
    global random_question1
    global random_question2
    global random_question3

    random_question1 = random.randrange(0,35,6)
    random_question2 = random.randrange(0,35,6)
    random_question3 = random.randrange(0,35,6)

    while random_question2 == random_question1:
        random_question2 = random.randrange(0,35,6)
    while random_question3 == random_question1 or random_question3 == random_question2:
        random_question3 = random.randrange(0,35,6)


#Questions place function
def questions_place():
    global random_question
    global good_answer
    global quest_label
    global steps
    global questions
#Define level of the question
    if steps == 0:
        if lang == 1:
            questions = str('easy_questions-en.txt')
        else:
            questions = str('easy_questions-pl.txt')
    if steps == 3:
        if lang == 1:
            questions = str('medium_questions-en.txt')
        else:
            questions = str('medium_questions-pl.txt')
    if steps == 6:
        if lang == 1:
            questions = str('hard_questions-en.txt')
        else:
            questions = str('hard_questions-pl.txt')

#Place question depends at steps
    if steps == 0 or steps == 3 or steps == 6:
        random_question = random_question1
    if steps == 1 or steps == 4 or steps == 7:
        random_question = random_question2
    if steps == 2 or steps == 5 or steps ==8:
        random_question = random_question3
    
    quest = linecache.getline(questions, random_question + 1).strip()
    quest_label = Label(root, 
                    text = quest,
                    font = ('Gill Sans Ultra Bold',17,'bold'),
                    fg='white',
                    bg='black',
                    relief = SUNKEN,
                    pady = 30,
                    padx = 30)

    quest_label.place(x=600,y=150, anchor=CENTER)
#Define good answer
    good_answer = linecache.getline(questions, random_question + 6)
def next_exit_buttons():

    global button_nq
    global button_end
    button_nq = Button(root,
                        text = linecache.getline(language,1).strip(),
                        font=('Gill Sans Ultra Bold',15,'bold'),
                        background='white',
                        activebackground='white',
                        padx=15,
                        pady=18,
                        disabledforeground='#6f6f6f',
                        command=next_question,
                        state = DISABLED)
    button_end = Button(root,
                        text = linecache.getline(language,2).strip(),
                        font=('Gill Sans Ultra Bold',15,'bold'),
                        background='white',
                        activebackground='white',
                        padx=10,
                        pady=18,
                        disabledforeground='#6f6f6f',
                        command=end,
                        state = DISABLED)

    button_nq.place(x=600,y=600, anchor=CENTER,width=300)

def answers_place():
    global button_A
    global button_B
    global button_C
    global button_D
    global button_nq
    global questions
    global button_exit
    ans1 = linecache.getline(questions, random_question + 2).strip()
    ans2 = linecache.getline(questions, random_question + 3).strip()
    ans3 = linecache.getline(questions, random_question + 4).strip()
    ans4 = linecache.getline(questions, random_question + 5).strip()
    button_A = Button(root,
                        text = ans1,
                        font=('Gill Sans Ultra Bold',15,'bold'),
                        background='white',
                        padx=10,
                        pady=20,
                        disabledforeground='black',
                        command=lambda: check_answer(1))
    button_B = Button(root,
                        text = ans2,
                        font=('Gill Sans Ultra Bold',15,'bold'),
                        background='white',
                        padx=10,
                        pady=20,
                        disabledforeground='black',
                        command=lambda: check_answer(2))
    button_C = Button(root,
                        text = ans3,
                        font=('Gill Sans Ultra Bold',15,'bold'),
                        background='white',
                        padx=10,
                        pady=20,
                        disabledforeground='black',
                        command=lambda: check_answer(3))
    button_D = Button(root,
                        text = ans4,
                        font=('Gill Sans Ultra Bold',15,'bold'),
                        background='white',
                        padx=10,
                        pady=20,
                        disabledforeground='black',
                        command=lambda: check_answer(4))


    button_A.place(x=180, y=250,width=350)
    button_B.place(x=680, y=250,width=350)
    button_C.place(x=180, y=400,width=350)
    button_D.place(x=680, y=400,width=350)
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
        if steps == 0 or steps == 1 or steps == 2:
            user_score += 5
        if steps == 3 or steps == 4 or steps == 5:
            user_score += 10
        if steps == 6 or steps == 7 or steps == 8:
            user_score += 15
    if int(good_answer) != ans:
        if steps == 0 or steps == 1 or steps == 2:
            user_score -= 15
        if steps == 3 or steps == 4 or steps == 5:
            user_score -=10
        if steps == 6 or steps == 7 or steps == 8:
            user_score -=5
    

    if steps == 8:
        button_end.config(state=ACTIVE)
    else:
        button_nq.config(state=ACTIVE)




def next_question():
    global random_question1
    global random_question2
    global random_question3
    global steps
    steps += 1
    if steps == 1 or steps == 2 or steps == 3:
        easy.destroy()
    if steps == 4 or steps == 5 or steps == 6:
        medium.destroy()
    if steps == 7 or steps == 8:
        hard.destroy()
    quest_label.destroy()
    button_A.destroy()
    button_B.destroy()
    button_C.destroy()
    button_D.destroy()

    if steps == 3:
        draw_questions()

    if steps == 6:
        draw_questions()

    if steps == 0 or steps == 1 or steps == 2:
        easy_level()
    if steps == 3 or steps == 4 or steps == 5:
        medium_level()
    if steps == 6 or steps == 7 or steps ==8:
        hard_level()
    if steps == 8:
        button_nq.destroy()
        button_end.place(x=600,y=600, anchor=CENTER)


def end():
    global button_try_again
    global button_exit2
    global user_score_label
    global end_screen_label
    hard.destroy()
    quest_label.destroy()
    button_A.destroy()
    button_B.destroy()
    button_C.destroy()
    button_D.destroy()
    button_end.destroy()
    button_try_again = Button(root,
                        text = linecache.getline(language,3).strip(),
                        font=('Gill Sans Ultra Bold',15,'bold'),
                        background='white',
                        activebackground='white',
                        padx=10,
                        pady=16,
                        disabledforeground='black',
                        command=start,
                        state = ACTIVE)
    button_exit2 = Button(root,
                        text = linecache.getline(language,4).strip(),
                        font=('Gill Sans Ultra Bold',15,'bold'),
                        background='white',
                        activebackground='white',
                        padx=10,
                        pady=16,
                        disabledforeground='black',
                        command=exit,
                        state = ACTIVE)
    end_screen_label = Label(root, text=linecache.getline(language,5).strip(),
                            background='#FEDE27',
                            font=('Gill Sans Ultra Bold',30,'bold'))
    user_score_label = Label(root, text=linecache.getline(language,6).strip()+ " " + str(user_score),
                            background='#FEDE27',
                            font=('Gill Sans Ultra Bold',20,'bold'))

    end_screen_label.place(x=600, y=200,anchor=CENTER)
    user_score_label.place(x=600, y=300,anchor=CENTER)
    button_exit2.place(x=600, y=500,anchor=CENTER, width=300)
    button_try_again.place(x=600, y=400,anchor=CENTER, width=300)


def easy_level():
    global easy
    #Define easy level label
    easy = Label(root,
                text=linecache.getline(language,7).strip(),
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
                text=linecache.getline(language,8).strip(),
                font=('Gill Sans Ultra Bold', 30),
                fg='#f7720c',
                bg='black',
                relief=SUNKEN,
                padx=10)
    
    medium.place(x=600,y=50, anchor=CENTER)
    questions_place()
    answers_place()

def hard_level():
    global hard
    #Define hard level label
    hard = Label(root,
                text=linecache.getline(language,9).strip(),
                font=('Gill Sans Ultra Bold', 30),
                fg='#ad0909',
                bg='black',
                relief=SUNKEN,
                padx=10)
    
    hard.place(x=600,y=50, anchor=CENTER)
    questions_place()
    answers_place()

def exit():
    root.destroy()


    

def start():
    global steps
    global user_score
    button_start.destroy()
    button_exit.destroy()
    if steps == 8:
        button_try_again.destroy()
        button_exit2.destroy()
        end_screen_label.destroy()
        user_score_label.destroy()
    if steps == 0:
        head_menu_label.destroy()
    steps = 0
    user_score = 0

    next_exit_buttons()
    easy_level()

def main_menu():
    global button_exit
    global button_start
    draw_questions()

    button_exit = Button(root,
                            text = linecache.getline(language,4).strip(),
                            font=('Gill Sans Ultra Bold',20,'bold'),
                            background='white',
                            activebackground='white',
                            padx=10,
                            pady=12,
                            disabledforeground='black',
                            command=exit,
                            state = ACTIVE)

    button_start = Button(root,
                            text = linecache.getline(language,10).strip(),
                            font=('Gill Sans Ultra Bold',20,'bold'),
                            background='white',
                            activebackground='white',
                            padx=10,
                            pady=12,
                            disabledforeground='black',
                            command=start,
                            state = ACTIVE)



    button_start.place(x=600, y=400,anchor=CENTER, width=250)
    button_exit.place(x=600, y=500,anchor=CENTER, width=250)

button_english = Button(root,
                            text = "English",
                            font=('Gill Sans Ultra Bold',20,'bold'),
                            background='white',
                            activebackground='white',
                            padx=10,
                            pady=12,
                            disabledforeground='black',
                            command=lambda: language_def(1),
                            state = ACTIVE)
                    
button_polish = Button(root,
                            text = "Polish",
                            font=('Gill Sans Ultra Bold',20,'bold'),
                            background='white',
                            activebackground='white',
                            padx=10,
                            pady=12,
                            disabledforeground='black',
                            command=lambda: language_def(2),
                            state = ACTIVE)

button_english.place(x=600, y=400,anchor=CENTER, width=250)
button_polish.place(x=600, y=500,anchor=CENTER, width=250)

root.mainloop()