from tkinter import *


def myhandler():
    txt1.edit_undo()


win=Tk()
win.geometry("600x400")


sb1=Scrollbar(win,orient=VERTICAL)
sb1.pack(side=RIGHT,fill=Y)
txt1=Text(win,undo=True,yscrollcommand=sb1.set)
txt1.pack(side=LEFT)

sb1['command']=txt1.yview
'''
bt1=Button(win,text='undo',command=myhandler)
bt1.pack()
'''
win.mainloop()