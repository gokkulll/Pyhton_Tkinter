from tkinter import *


def myhandler():
    text1.insert(1.0,"HelloWorld")

def pophandler(e):
    file.tk_popup(e.x_root,e.y_root,0)


win=Tk()
win.geometry('600x400')



txt1=Text(win)
text1.pack(fill=BOTH)

menubar=Menu(win)
win['menu']=menubar

file=Menu(menubar)
menubar.add_cascade(label='File',menu=file)

file.add_command(label='New',command=myhandler)
file.add_command(label='Open')
file.add_command(itemtype=command,label='Save')
file.add_seperator()
file.add_Checkbutton(label='Save As',onvalue=1,offvalue=0)


rad1=Menu(file)
rad1.add_Radiobtutton(label='option1')
rad1.add_Radiobutton(label='option2')
rad1.add_Radiobutton(label='option3')
file.add_cascade(label='Options',menu=rad1)

txt1.bind('<Button-3>',command=pophandler)


win.mainloop()