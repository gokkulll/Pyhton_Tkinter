from tkinter import *

win=Tk()
win.title('My first Application')
win.geometry('600x400')

t1=Text(win,wrap=WORD,spacing1=100,)
t1.pack()

win.mainloop()