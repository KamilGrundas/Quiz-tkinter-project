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
        self.main_menu()

        
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
        self.head_menu_label = Label(self.root, image=self.head_to_label,borderwidth=0)
        self.head_menu_label.place(x=630, y=180, anchor=CENTER)

        #Define list of created buttons
        self.buttons_list = []

        self.language = Language()
        #Place buttons with (text, xplace, yplace, width, command(language selection))
        self.button_place(self.language.a_language, 600, 550, 250, lambda: self.language_def(True))
        self.button_place(self.language.english, 600, 450, 250, lambda: self.language_def(False))

        

    def button_place(self, text, x, y, width, command):
        
        self.buttons = Buttons()
        
        self.button = Button(self.root,
                                    text = text,
                                    font=self.buttons.menufont,
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

    def main_menu(self):

        self.button_place(self.language.play, 600, 450, 250, self.play)
        self.button_place(self.language.exit, 600, 550, 250, self.exit)
        self.button_place(self.language.settings, 100,100, 100, self.language_def)

    def play(self):

        print("graj")

    def exit(self):
        app.root.quit()
        










app=QuizApp()
app.root.mainloop()