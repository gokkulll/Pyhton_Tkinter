from tkinter import *
from tkinter.messagebox import *

win=Tk()
win.title("My Application")
win.geometry('600x400')

#b1=Entry(win,highlightbackground='red',highlightthickness=5,highlightcolor='yellow')
b1 = Button(win,text='Button1',state=ACTIVE,activebackground='red',activeforeground='yellow',takefocus=1)

'''b1 = Listbox(win,activestyle=UNDERLINE)
b1.insert(1,'a')
b1.insert(2,'b')
b1.insert(3,'c')
b1.insert(4,'d')
b1.pack()

'''

b1.pack()

b2=Checkbutton(win,text='Button2',takefocus=1,indicatoron=False)
b2.pack()

win.mainloop()