from tkinter import *
root = Tk()
e1 = Entry(root)
e2 = Entry(root)
b1 = Button(root, text='+', width=10)
b2 = Button(root, text='-', width=10)
b3 = Button(root, text='*', width=10)
b4 = Button(root, text='/', width=10)
l = Label(root, width=20)

def calc_plus(event):
    n1 = int(e1.get())
    n2 = int(e2.get())
    l['text'] = n1 + n2

def calc_minus(event):
    n1 = int(e1.get())
    n2 = int(e2.get())
    l['text'] = n1 - n2

def calc_mult(event):
    n1 = int(e1.get())
    n2 = int(e2.get())
    l['text'] = n1 * n2

def calc_divide(event):
    n1 = int(e1.get())
    n2 = int(e2.get())
    l['text'] = n1 / n2

b1.bind('<Button-1>', calc_plus)
b2.bind('<Button-1>', calc_minus)
b3.bind('<Button-1>', calc_mult)
b4.bind('<Button-1>', calc_divide)

e1.pack()
e2.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
l.pack()

mainloop()

