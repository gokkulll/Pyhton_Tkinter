from tkinter import *
import tkinter.messagebox as msg

def myhandler():
    ans=msg.askyesno('My','Do you want to continue?')
    print(ans)



win=Tk()
win.geometry("600x400")

b1=Button(win,text='Click Me',command=myhandler)
b1.pack()

win.mainloop()