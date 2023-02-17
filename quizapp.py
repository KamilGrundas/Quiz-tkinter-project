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
        self.root.resizable(False, False)
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
        self.head_menu_label.place(x=630, y=180, anchor=CENTER)




    def language_buttons(self):

        self.buttons = Buttons()
        self.button_destroy()

        self.language = Language()

        self.button_place(self.language.a_language, self.buttons.menufont, 600, 550, 250, lambda: self.language_def(True))
        self.button_place(self.language.english, self.buttons.menufont, 600, 450, 250, lambda: self.language_def(False))

    def button_place(self, text, font, x, y, width, command):
        
        self.button = Button(self.root,
                                    text = text,
                                    font= font,
                                    background=self.buttons.background,
                                    activebackground=self.buttons.activebackground,
                                    padx=self.buttons.padx,
                                    pady=self.buttons.pady,
                                    disabledforeground=self.buttons.disabledforeground,
                                    command=command,
                                    state = ACTIVE)

        self.buttons_list.append(self.button)

        self.button.place(x=x, y=y,anchor=CENTER, width=width)

        

    def button_destroy(self):

        for self.button in self.buttons_list:
            self.button.destroy()

    def main_menu(self, logo):

        if logo == True:
            self.head_menu_place()

        self.button_place(self.language.play, self.buttons.menufont, 600, 450, 250, self.play)
        self.button_place(self.language.exit, self.buttons.menufont, 600, 550, 250, self.exit)
        self.button_place(self.language.language, self.buttons.settingsfont, 100,100, 100, self.language_buttons)
        self.button_place(self.language.settings, self.buttons.settingsfont, 100,200, 100, self.settings_menu)

    def play(self):

        print("graj")

    def settings_menu(self):

        self.button_destroy()


        self.button_place(self.language.back, self.buttons.menufont, 600, 550,250, lambda: self.main_menu(True))

        self.head_menu_label.destroy()

    def exit(self):
        app.root.quit()
        










app=QuizApp()
app.root.mainloop()