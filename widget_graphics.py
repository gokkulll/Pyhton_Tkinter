from tkinter import *


win=Tk()
win.title("My nth Application")
win.geometry('600x400')


img=PhotoImage(file='GOKUL M.png')
l1=Label(win,text='Label1',image=img)

l1.pack()

win.mainloop()