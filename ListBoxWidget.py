from tkinter import *



def myhandler():
    var.set(lb1.curselection())
win=Tk()
win.title("Hello")
win.geometry("600x400")

var=StringVar()
t1=Entry(win, textvariable=var)
t1.pack()

lb1=Listbox(win)
lb1.insert('0','C')
lb1.insert('1','C++')
lb1.insert('2','Rust')
lb1.insert('3','Java')

lb1.pack()

b1=Button(win,text='ClickMe',command=myhandler)
b1.pack() 
win.mainloop()