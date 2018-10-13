from tkinter import *
root = Tk()

frame = Frame(width=10)
frame.pack(side=LEFT)

var = IntVar()
var.set('Default')

def change():
    if var.get() == 1:
        label['text'] = 'Текст 1'
    elif var.get() == 2:
        label['text'] = 'Текст 2'
    elif var.get() == 3:
        label['text'] = 'Текст 3'

Radiobutton(frame, text='Вася', indicatoron=0, variable=var, value=1, command=change).pack()
Radiobutton(frame, text='Петя', indicatoron=0, variable=var, value=2, command=change).pack()
Radiobutton(frame, text='Маша', indicatoron=0, variable=var, value=3, command=change).pack()

label = Label()
label.pack(expand=1)

mainloop()