from tkinter import *
root = Tk()
e1 = Entry(root)
l = Label(root)
def red():
    e1.delete(0, END)
    e1.insert(0,'#ff0000')

def orange():
    e1.delete(0, END)
    e1.insert(0,'#ff7d00')

def yellow():
    e1.delete(0, END)
    e1.insert(0,'#ffff00')

def green():
    e1.delete(0, END)
    e1.insert(0,'#00ff00')

def blue():
    e1.delete(0, END)
    e1.insert(0,'#007dff')

def blue2():
    e1.delete(0, END)
    e1.insert(0,'#0000ff')

def violet():
    e1.delete(0, END)
    e1.insert(0,'#7d00ff')

e1.pack()
Button(bg='#7d00ff', width=20, command=violet).pack()
Button(bg='#007dff', width=20, command=blue).pack()
Button(bg='#0000ff', width=20, command=blue2).pack()
Button(bg='#00ff00', width=20, command=green).pack()
Button(bg='#ffff00', width=20, command=yellow).pack()
Button(bg='#ff7d00', width=20, command=orange).pack()
Button(bg='#ff0000', width=20, command=red).pack()

mainloop()