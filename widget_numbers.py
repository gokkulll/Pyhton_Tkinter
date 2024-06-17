from tkinter import *

win=Tk()
win.title("MyApp")
win.geometry("600x400")


#var=IntVar(value=20)
#s1=Scale(win,variable=var,from_=0,to=100,orient=HORIZONTAL)
#s1.pack()

sb1=Scrollbar(win,orient=VERTICAL)
t1=Text(win)

t1.config(yscrollcommand = sb1.set)
sb1.config(command=t1.yview)


sb1.pack(side=RIGHT,fill=Y)
t1.pack()
win.mainloop()