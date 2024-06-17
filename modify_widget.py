from tkinter import *
from tkinter.messagebox import *


def my_handler(e):
    print(lbl.cget('text'))
    showinfo('Mybox',lbl.cget('text'))
    lbl.config(bg='red')

win=Tk()
win.title("My nth Applicatin")
win.geometry("600x400")

lbl=Label(win,text='Blue color',bg='yellow',fg='green')
lbl.pack()

lbl.bind('<Button-1>',my_handler)

win.mainloop()