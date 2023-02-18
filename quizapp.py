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

        self.button_place(self.language.a_language, 
                            self.settings.menufont, 
                            lambda: self.language_def(True), 20, CENTER, TOP)
        self.button_place(self.language.english, 
                            self.settings.menufont, 
                            lambda: self.language_def(False), 20, CENTER, TOP)

    def button_place(self, text, font, command, width, position, side):
        
        self.button = Button(self.root,
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
            self.head_menu_place()
            self.frame_active_questions.destroy()
            self.frame_no_active_questions.destroy()
            self.button_destroy()

        self.button_place(self.language.play, self.settings.menufont, self.play, 20, CENTER, TOP)
        self.button_place(self.language.exit, self.settings.menufont, self.exit, 20, CENTER, TOP)
        self.button_place(self.language.language, self.settings.settingsfont, self.language_buttons, 20, SE, TOP)
        self.button_place(self.language.settings, self.settings.settingsfont, self.settings_menu, 20, SE, TOP)

    def play(self):

        print("graj")

    def list_questions(self):

        self.frame_active_questions = Frame(self.root, background=self.settings.background_color)
        self.frame_active_questions.pack(side=RIGHT)

        self.frame_no_active_questions = Frame(self.root, background=self.settings.background_color)
        self.frame_no_active_questions.pack(padx=10, pady=10, side='left')

        self.active_questions_l = Label(self.frame_active_questions, 
                                        text=self.language.active_questions, 
                                        font=self.settings.menufont,
                                        background=self.settings.background_color)

        self.active_questions_l.pack(side=TOP)

        self.active_questions_l = Label(self.frame_no_active_questions, 
                                        text=self.language.no_active_questions,
                                        font=self.settings.menufont,
                                        background=self.settings.background_color)

        self.active_questions_l.pack(side=TOP)

        self.active_questions = Listbox(self.frame_active_questions,
                                            font=self.settings.settingsfont,
                                            width= 50,
                                            height= 20)

        # self.scrollbar = Scrollbar(self.root, orient='vertical', command=self.active_questions.yview)
        # self.active_questions.config(yscrollcommand=self.scrollbar.set)

        self.active_questions.pack(side=TOP)

        # self.scrollbar.pack(side=RIGHT, fill=Y)

        self.no_active_questions = Listbox(self.frame_no_active_questions,
                                            font=self.settings.settingsfont,
                                            width= 50,
                                            height= 20)

        self.no_active_questions.pack(side=TOP)
        

    

    def settings_menu(self):

        self.button_destroy()
        self.list_questions()

        self.button_place(self.language.back, self.settings.menufont, lambda: self.main_menu(True), 20, CENTER, BOTTOM)
        self.head_menu_label.destroy()


    def exit(self):
        app.root.quit()
        










app=QuizApp()
app.root.mainloop()