import random
import linecache
from tkinter import *
root = Tk()
root.title("Quiz")
root.geometry("1200x700")



def start():
    button_start.destroy()


button_start = Button(text='START',command = start)

button_start.place(x=350, y=300, width=500)

root.mainloop()