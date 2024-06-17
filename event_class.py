from tkinter import *
from tkinter.messagebox import *



def my_handler(e):
    print(e)
    print(e.type)
    print(e.char)


win = Tk()

win.title("MySecondApplication")
win.geometry('600x400')

b1 = Entry(win,bg='red',fg='blue')
b1.pack()

#b1.bind('<Button-1>',my_handler)

b1.bind('<KeyPress>',my_handler)

win.mainloop()