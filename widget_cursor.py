from tkinter import *

win=Tk()
win.title('Hello')
win.geometry('600x400')

t1=Text(win,insertbackground='blue',insertwidth=10,insertborderwidth=55,insertofftime=0,cursor='pencil')
t1.pack()

win.mainloop()