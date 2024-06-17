from tkinter import *


def myhandler():
    var.set(var.get() + 1)



win=Tk()
win.title("Hello bro")
win.geometry('600x400')

var=IntVar()
lb1=Label(win,text='0',textvariable=var)
lb1.pack()




bt1=Button(win,text='Click to count',command=myhandler)
bt1.pack()

win.mainloop()