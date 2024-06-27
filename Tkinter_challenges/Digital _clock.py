import time
from tkinter import *

def myclock():
    watch = time.strftime('%-I:%M:%S')
    lb1['text']=watch
    lb1.after(100,myclock)




win=Tk()
win.geometry('400x200')
win.title("DigitalClock")

lb1=Label(win,bg='blue',font=('Times new roman',40))
lb1.pack(fill=BOTH,expand=True)

myclock()
win.mainloop()