from tkinter import *
from tkinter.font import *

def myhandler():
    lb1['text']=cb1['text'] if var.get()==1 else ' '


def buthandler():
    #cb1.deselect()
    #cb1.toggle()
    cb1.invoke()

win=Tk()

win.title("Hello")
win.geometry('600x400')




lb1=Label(win,text=' ')
lb1.pack()

var=IntVar()
cb1=Checkbutton(win,text='Java',variable=var,command=myhandler)
cb1.pack()


but=Button(win,text='clickme',command=buthandler)
but.pack()

win.mainloop()