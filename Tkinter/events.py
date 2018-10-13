from tkinter import *
root = Tk()


def change():
    t['width'] = int(e1.get())
    t['height'] = int(e2.get())

def focus_out(event):
    t['bg'] = 'lightgrey'

def focus_in(event):
    t['bg'] = 'white'

frame = Frame(width=10)
frame.pack(side=TOP)

e1 = Entry(frame)
e2 = Entry(frame)

b = Button(frame, text='Изменить', command=change)

e1.bind('Return', change)
e2.bind('Return', change)

e1.pack()
e2.pack()
b.pack(side=LEFT)

t = Text()
t.pack(side=BOTTOM)
t.bind('<FocusIn>', focus_in)
t.bind('<FocusOut>', focus_out)

mainloop()
