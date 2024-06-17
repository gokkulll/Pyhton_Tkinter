from tkinter import *
from tkinter.messagebox import *


def fun(e):
    showinfo('MYBox',"something has happened")



win=Tk()

win.title("My Third Application")
win.geometry('600x400')

e  = Entry(win,bg='red',fg='blue')
e.pack()

e.bind('<Double-Button-1>', fun)

win.mainloop()