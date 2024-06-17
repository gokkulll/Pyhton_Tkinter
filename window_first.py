from tkinter import *

win = Tk()

win.geometry('600x400+100+100')
win.title("My First Application")
win.resizable(True,True)


'''l = Label(win,text='Name')
l.pack()
'''


e = Entry()
e.pack()
'''
b = Button(win,text='Click Me')
b.pack()


win.attributes('-alpha',0.20)'''


'''t = Text(win,width=40,height=20)
t.pack()
'''
'''
c = Checkbutton(win, text='Yes')
c.pack()
'''


'''
r = Radiobutton(win,text='option1',variable='v1',value=1)
r.pack()
r2 = Radiobutton(win,text='option2',variable='v1',value=2)
r2.pack()
r3 = Radiobutton(win,text='option3',variable='v1',value=3)
r3.pack()
'''

'''
v = StringVar()
o = OptionMenu(win, v ,*('python','java','C++','Javascript'))
o.pack()
'''

'''
s = Scale(win, from_=0, to=100)
s.pack()
'''
win.mainloop()
               