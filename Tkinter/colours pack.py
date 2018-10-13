from tkinter import *
root = Tk()
e1 = Entry(root)
l = Label(root)
def red():
    e1.insert(0,'#ff0000')

def orange():
    e1.insert(0,'#ff7d00')

def yellow():
    e1.insert(0,'#ffff00')

def green():
    e1.insert(0,'#00ff00')

def blue():
    e1.insert(0,'#007dff')

def blue2():
    e1.insert(0,'#0000ff')

def violet():
    e1.insert(0,'#7d00ff')

e1.pack()
Button(bg='#7d00ff', width=5, command=violet).pack(side=LEFT)
Button(bg='#007dff', width=5, command=blue).pack(side=LEFT)
Button(bg='#0000ff', width=5, command=blue2).pack(side=LEFT)
Button(bg='#00ff00', width=5, command=green).pack(side=LEFT)
Button(bg='#ffff00', width=5, command=yellow).pack(side=LEFT)
Button(bg='#ff7d00', width=5, command=orange).pack(side=LEFT)
Button(bg='#ff0000', width=5, command=red).pack(side=LEFT)

mainloop()