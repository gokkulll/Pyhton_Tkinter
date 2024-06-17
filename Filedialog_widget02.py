from tkinter import *
from tkinter.filedialog import *


def newhandler():
    fname=askopenfile()
    txt=fname.read()
    t1.insert('1.0',txt)


def savehandler():
    fname=asksaveasfile()
    fname.write(t1.get('1.0','end-ic'))

def deletehandler():
    t1.delete('1.0','end-1c')
    
win=Tk()
win.title("hello")
win.geometry('600x400')

t1=Text(win)
t1.pack()

b1=Button(win,text='New',command=newhandler)
b1.pack()

b2=Button(win,text='Save',command=savehandler)
b2.pack()

b3=Button(win,text='Delete',command=deletehandler)
b3.pack()

win.mainloop()