from tkinter import *

win=Tk()
win.geometry('600x400')

f1=LabelFrame(win,text='Frame1',bg='Blue',width=200)
f1.pack(side=LEFT,fill=Y)

f2=LabelFrame(win,text='Frame2',bg='Red',width=200)
f2.pack(side=RIGHT,fill=Y)

b1=Button(f1,text="Button1")
b2=Button(f1,text="Button2")
b3=Button(f1,text="Button3")
b4=Button(f1,text="Button4")

b1.grid(row=0,column=0)
b1.grid(row=0,column=1)
b1.grid(row=1,column=0)
b1.grid(row=1,column=1)



b11=Button(f2,text="Button1")
b12=Button(f2,text="Button2")
b13=Button(f2,text="Button3")
b14=Button(f2,text="Button4")

b11.grid(row=0,column=0)
b12.grid(row=0,column=1)
b13.grid(row=1,column=0)
b14.grid(row=1,column=1)




win.mainloop()

