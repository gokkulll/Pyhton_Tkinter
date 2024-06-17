from tkinter import *
from tkinter.messagebox import *

def fun(win):
    showinfo('MyBox','Event is Generated')

win=Tk()
win.title("MyFourthApplication")
win.geometry('600x400')

e=Entry(win,bg='blue',fg='grey')
e.pack()

e1=Entry(win,bg='blue',fg='grey')
e1.pack()

e2=Entry(win,bg='blue',fg='grey')
e2.pack()

win.bind_all('<Button-1>',fun)

win.mainloop()