from tkinter import *


mytime=0
flag=True


def start():
    global mytime,flag
    flag=True
    update_time()
   


def update_time():
    global mytime,flag
    if flag==True:
        mytime+=10
        milli = mytime % 1000
        sec=mytime // 1000
        min=sec//60
        sec=sec%60

        lb1['text']=f'{min:02d}:{sec:02d}:{milli:03d}'
        
        lb1.after(10,update_time)
def stop():
    global flag
    flag=False

def reset():
    global mytime,flag
    mytime=0
    flag=False
    
    lb1['text']='00:00:000'
   


win=Tk()

win.title("stop_clock")
win.geometry("400x200")

lb1=Label(win,text='00:00:000',font=('Times new roman', 45))
lb1.grid(row=0,column=0,columnspan=3)

b1=Button(win,text='Start',command=start)
b1.grid(row=1,column=0)

b2=Button(win,text='Stop',command=stop)
b2.grid(row=1,column=1)

b3=Button(win,text='Reset',command=reset)
b3.grid(row=1,column=2)

win.mainloop()