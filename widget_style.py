from tkinter import *
from tkinter.messagebox import *

win = Tk()
win.title('MyApplication')
win.geometry('600x400')



b1=Button(win,text='Button1',bd=10,bg='orange',fg='yellow',anchor=N,relief=RAISED,overrelief=SUNKEN)
b1.pack()

win.mainloop()