from tkinter import *
from tkinter.messagebox import *

'''def myhandler():
    def mychildhandler():
        showinfo('My','Child App')
    
    Tl=Toplevel(win)
    Tl.geometry('300x300')
    b2=Button(Tl,text='Click',command=mychildhandler)
    b2.pack()
    Tl.mainloop()
'''






class MyTop(Toplevel):
        def mychildhandler(self):
            showinfo('My','child App')
        
    

        def __init__(self):
            Toplevel.__init__(self)
            b1=Button(self,text="Click",command=self.mychildhandler)
            b1.pack()




def myhandler():
    Tk=MyTop()
    Tk.geometry("300x300")
    Tk.mainloop()



win=Tk()
win.geometry('600x400')

b1=Button(win,text='click me', command=myhandler)
b1.pack()

win.mainloop()