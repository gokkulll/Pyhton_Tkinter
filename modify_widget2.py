from tkinter import *
from tkinter.messagebox import *


def my_handler(e):
    
    l1.config(bg='yellow')
    l1.config(text='1Label')


def my_handler2(e):
  
    l1.config(bg='green')
    l1.config(text="Label1")
 
    



win=Tk()
win.title('My Nth Application')
win.geometry("600x400")

l1=Label(win,text="Label1",bg='green',fg='black')
l1.pack()

l1.bind('<Enter>',my_handler)
l1.bind('<Leave>',my_handler2,add='+')

win.mainloop()