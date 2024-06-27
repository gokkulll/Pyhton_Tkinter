from tkinter import *
from PIL import ImageTk,Image

win=Tk()
win.geometry('600x400')

c1 = Canvas(win,bg='Yellow',width=300,height=200)
c1.pack()

#c1.create_line(100,100,200,200,width=20,fill='Blue',arrow=FIRST)



c1.create_rectangle(100,100,200,200,width=10,fill='Blue',outline='Black')

img1=ImageTk.PhotoImage(Image.open("python-programming-blue-green-wallpaper-preview.jpg"))
c1.create_image(10,10,image=img1,anchor=NW)

win.mainloop()