from tkinter import *
from tkinter.messagebox import *



def fun(e):
    showinfo('Mybox','Event is Generated')


def fun1(e):
    showinfo("MyBox",e)
win = Tk()

win.title("MySecondApplication")
win.geometry('600x400')

b1 = Entry(win,bg='red',fg='blue')
b1.place(x=100,y=100,width=200,height=100)

b1.bind('<Button-3>',fun)
#b1.bind('<Enter>',fun)
b1.bind('<Button-1>',fun1,add='+')

win.mainloop()