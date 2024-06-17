from tkinter import *
from tkinter.font import *


def myhandler(e):
    f = Font(size=str(s1.get()))
    e1['font']=f

win=Tk()
win.title("Hello")
win.geometry("600x400")


var1=IntVar(value='HelloWorld')
e1=Entry(win,textvariable=var1)
e1.pack()

s1=Scale(win,from_=1,to=100,command=myhandler)
s1.pack()

win.mainloop()