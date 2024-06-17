from tkinter import *



def fun():
    print("Button1 is clicked")
    




win=Tk()

win.title("MyFirstApllication")
win.geometry("600x400")


b1=Button(win, text="Button1",command=fun)
b1.pack()

win.mainloop()