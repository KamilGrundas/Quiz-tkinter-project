from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
from buttons import Buttons
import sys
from settings import Settings
from language import Language

class QuizApp():
    
    #Function that changes language from english to another
    def language_def(self,change):


        self.language = Language()
        if change == True:
            self.language.another_language()

        self.button_destroy()
        self.main_menu(False)

        
    def __init__(self):

        self.root = Tk()
        self.root.title("Quiz")
        self.root.iconbitmap('icon.ico')
        self.settings = Settings()
        self.ws = self.root.winfo_screenwidth() # width of the screen
        self.hs = self.root.winfo_screenheight() # height of the screen
        self.x = (self.ws/2) - (self.settings.w/2)
        self.y = ((self.hs-100)/2) - (self.settings.h/2)
        self.root.minsize(self.settings.w, self.settings.h)
        self.root.geometry('%dx%d+%d+%d' % (self.settings.w, self.settings.h, self.x, self.y))
        self.root.resizable(True, True)
        self.root.config(background=self.settings.background_color)
        #Menu logo open
        self.head_menu = Image.open("head_.png")
        #Menu logo resize
        self.resized_head = self.head_menu.resize((500,350), Image.Resampling.LANCZOS)
        #Menu logo define and place
        self.head_to_label = ImageTk.PhotoImage(self.resized_head)


        #Define list of created buttons
        self.buttons_list = []

        self.head_menu_place()
        self.language_buttons()
        #Place buttons with (text, xplace, yplace, width, command(language selection))

    def head_menu_place(self):

        self.head_menu_label = Label(self.root, image=self.head_to_label,borderwidth=0)
        self.head_menu_label.pack(anchor=CENTER)




    def language_buttons(self):

        self.buttons = Buttons()
        self.button_destroy()

        self.language = Language()

        self.button_place(self.root,self.language.a_language, 
                            self.settings.menufont, 
                            lambda: self.language_def(True), 20, CENTER, TOP)
        self.button_place(self.root,self.language.english, 
                            self.settings.menufont, 
                            lambda: self.language_def(False), 20, CENTER, TOP)

    def button_place(self, place, text, font, command, width, position, side):
        
        self.button = Button(place,
                                    text = text,
                                    font= font,
                                    background=self.buttons.background,
                                    activebackground=self.buttons.activebackground,
                                    padx=self.buttons.padx,
                                    pady=self.buttons.pady,
                                    disabledforeground=self.buttons.disabledforeground,
                                    command=command,
                                    state = ACTIVE,
                                    width=width)

        self.buttons_list.append(self.button)

        self.button.pack(pady=10, padx=10, anchor=position, side=side)

        

    def button_destroy(self):

        for self.button in self.buttons_list:
            self.button.destroy()

    def main_menu(self, logo):

        if logo == True:
            self.frames_destroy()
            self.head_menu_place()


        self.button_place(self.root,self.language.play, self.settings.menufont, self.play, 20, CENTER, TOP)
        self.button_place(self.root,self.language.exit, self.settings.menufont, self.exit, 20, CENTER, TOP)
        self.button_place(self.root,self.language.settings, self.settings.settingsfont,lambda: self.settings_menu(False), 20, SE, BOTTOM)
        self.button_place(self.root,self.language.language, self.settings.settingsfont, self.language_buttons, 20, SE, BOTTOM)


    def play(self):

        print("graj")

    def list_questions(self):

        self.frames()
        self.buttons_settings()

        self.active_questions_l = Label(self.frame_right2, 
                                        text=self.language.active_questions, 
                                        font=self.settings.menufont,
                                        background=self.settings.background_color)

        self.active_questions_l.pack(side=TOP)

        self.active_questions_l = Label(self.frame_left2, 
                                        text=self.language.no_active_questions,
                                        font=self.settings.menufont,
                                        background=self.settings.background_color)

        self.active_questions_l.pack(side=TOP)

        self.active_questions = Listbox(self.frame_right2,
                                            font=self.settings.settingsfont,
                                            width= 50,
                                            height= 25)

        # self.scrollbar = Scrollbar(self.root, orient='vertical', command=self.active_questions.yview)
        # self.active_questions.config(yscrollcommand=self.scrollbar.set)

        self.active_questions.pack(side=TOP)
        # self.scrollbar.pack(side=RIGHT, fill=Y)

        self.no_active_questions = Listbox(self.frame_left2,
                                            font=self.settings.settingsfont,
                                            width= 50,
                                            height= 25)

        self.no_active_questions.pack(side=TOP)

    def frames_destroy(self):
        self.frame_center.destroy()
        self.frame_buttons.destroy()
        self.frame_top.destroy()

    def add_question(self):

        self.frames_destroy()
        self.frames()
        self.edit_section_labels()
        self.entries_place()
        self.edit_section_buttons()

    def edit_section_buttons(self):


        self.button_place(self.frame_buttons,self.language.add, 
                            self.settings.menufont, 
                            self.add_question, 15, CENTER, LEFT)

        self.button_place(self.frame_buttons,self.language.back, 
                            self.settings.menufont, 
                            lambda: self.settings_menu(True), 15, CENTER, LEFT)


    def entries_place(self):

        self.question_entry = Entry(self.frame_top,
                                    font=self.settings.menufont,
                                    width=50)
        self.question_entry.pack(pady= 50, side=RIGHT)

        self.entry_answer_A = Entry(self.frame_left2,
                                    font=self.settings.edit_section_font)
        self.entry_answer_A.pack(pady=60)

        self.entry_answer_B = Entry(self.frame_right2,
                                    font=self.settings.edit_section_font)
        self.entry_answer_B.pack(pady=60)

        self.entry_answer_C = Entry(self.frame_left2,
                                    font=self.settings.edit_section_font)
        self.entry_answer_C.pack(pady=60)

        self.entry_answer_D = Entry(self.frame_right2,
                                    font=self.settings.edit_section_font)
        self.entry_answer_D.pack(pady=60)

    def edit_section_labels(self):

        self.question_label = Label(self.frame_top, 
                                        text=self.language.question,
                                        font=self.settings.edit_section_font,
                                        background=self.settings.background_color)
        self.question_label.pack(side=LEFT, pady=50)

        self.answer_A_label = Button(self.frame_left, 
                                        text="A:",
                                        font=self.settings.edit_section_font,
                                        background=self.buttons.background,
                                        width=4,
                                        command= lambda: self.good_answer_highlight(1))
        self.answer_A_label.pack(pady=40)

        self.answer_B_label = Button(self.frame_right, 
                                        text="B:",
                                        font=self.settings.edit_section_font,
                                        background=self.buttons.background,
                                        width=4,
                                        command= lambda: self.good_answer_highlight(2))
        self.answer_B_label.pack(pady=40)

        self.answer_C_label = Button(self.frame_left, 
                                        text="C:",
                                        font=self.settings.edit_section_font,
                                        width= 4,
                                        background=self.buttons.background,
                                        command= lambda: self.good_answer_highlight(3))
        self.answer_C_label.pack(pady=40)

        self.answer_D_label = Button(self.frame_right, 
                                        text="D:",
                                        font=self.settings.edit_section_font,
                                        background=self.buttons.background,
                                        width=4,
                                        command= lambda: self.good_answer_highlight(4))
        self.answer_D_label.pack(pady=40)

    def good_answer_highlight(self, answer):

        self.answer_A_label.config(background=self.buttons.bad_answer_background)
        self.answer_B_label.config(background=self.buttons.bad_answer_background)
        self.answer_C_label.config(background=self.buttons.bad_answer_background)
        self.answer_D_label.config(background=self.buttons.bad_answer_background)

        if answer == 1:
            self.answer_A_label.config(background=self.buttons.selected_background)
        elif answer == 2:
            self.answer_B_label.config(background=self.buttons.selected_background)
        elif answer == 3:
            self.answer_C_label.config(background=self.buttons.selected_background)
        elif answer == 4:
            self.answer_D_label.config(background=self.buttons.selected_background)

    def frames(self):

        #Top frame
        self.frame_top = Frame(self.root, background=self.settings.background_color)
        self.frame_top.pack(anchor=CENTER, side=TOP)

        #Main center frame
        self.frame_center = Frame(self.root, background=self.settings.background_color)
        self.frame_center.pack(anchor=CENTER)

        #Frame for A,B,C,D labels
        self.frame_left = Frame(self.frame_center, background=self.settings.background_color)
        self.frame_left.pack(pady=10, anchor=CENTER, side=LEFT)

        #Frame for entries and listboxes left side
        self.frame_left2 = Frame(self.frame_center, background=self.settings.background_color)
        self.frame_left2.pack(padx=10, pady=10, anchor=CENTER, side=LEFT)

        self.frame_right = Frame(self.frame_center, background=self.settings.background_color)
        self.frame_right.pack(pady=10, anchor=CENTER, side=LEFT)

        #Frame for entries and listboxes right side
        self.frame_right2 = Frame(self.frame_center, background=self.settings.background_color)
        self.frame_right2.pack(padx=10, pady=10, anchor=CENTER, side=RIGHT)

        #Frame for buttons
        self.frame_buttons = Frame(self.root, background=self.settings.background_color)
        self.frame_buttons.pack(side=BOTTOM)



    def buttons_settings(self):

        self.button_place(self.frame_center,self.language.move, 
                            self.settings.menufont, 
                            lambda: self.main_menu(True), 20, CENTER, LEFT)

        self.button_place(self.frame_buttons,self.language.add, 
                            self.settings.menufont, 
                            self.add_question, 15, CENTER, LEFT)
        self.button_place(self.frame_buttons,self.language.edit, 
                            self.settings.menufont, 
                            lambda: self.main_menu(True), 15, CENTER, LEFT)
        self.button_place(self.frame_buttons,self.language.delete, 
                            self.settings.menufont, 
                            lambda: self.main_menu(True), 15, CENTER, LEFT)
        self.button_place(self.frame_buttons,self.language.back, 
                            self.settings.menufont, 
                            lambda: self.main_menu(True), 15, CENTER, LEFT)



        




        

    

    def settings_menu(self, back):

        # if back from edit section
        if back == True:
            self.frames_destroy()
            self.list_questions()

        #enter from main menu
        else:
            self.button_destroy()
            self.list_questions()
            self.head_menu_label.destroy()


    def exit(self):
        app.root.quit()
        










app=QuizApp()
app.root.mainloop()