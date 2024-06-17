from tkinter import *

win=Tk()
win.title("hello")
win.geometry('600x400')


lst1=['Amazon','Flipkart','Shopsy','Meesho']
sb1=Spinbox(win,values=lst1)
sb1.pack()

win.mainloop()