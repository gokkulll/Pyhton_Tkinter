from tkinter import *

win=Tk()
win.title("My nth Application")
win.geometry('600x400')

e1 = Entry(win,selectbackground='yellow',selectforeground='red',selectborderwidth=10)
e1.pack()

l1=Listbox(win,selectbackground='yellow',selectforeground='red',selectborderwidth=10,exportselection=FALSE)
l1.insert(1,'AA')
l1.insert(2,'BB')
l1.insert(3,'CC')
l1.insert(4,'DD')
l1.pack()

win.mainloop()