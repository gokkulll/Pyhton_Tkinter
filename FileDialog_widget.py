from tkinter import *
from tkinter.filedialog import *


def openhandler():
    fname=askopenfile()
    txt = fname.read()
    t1.insert('1.0',txt)
    

def savehandler():
    fname=asksaveasfile()
    fname.write(t1.get('1.0','end-1c'))

def otherhandler():
    t1.delete('1.0','end-1c')
    
win=Tk()
win.geometry('600x400')
t1=Text(win)
t1.pack()

b1=Button(win,text='Open',command=openhandler)
b1.pack()

b2=Button(win,text='Save',command=savehandler)
b2.pack()

b3=Button(win,text='Other',command=otherhandler)
b3.pack()

win.mainloop()