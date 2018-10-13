from tkinter import *
root = Tk()

l = ['apple', 'bananas', 'carrot', 'bread', 'butter', 'meat', 'potato', 'tomato', 'milk']

lbl = Listbox(selectmode=EXTENDED)
lbr = Listbox(selectmode=EXTENDED)

frame = Frame()

lbl.pack(side=LEFT)
frame.pack(side=LEFT)
lbr.pack(side=LEFT)

for i in l:
    lbl.insert(0, i)

def right():
    select = list(lbl.curselection())
    for i in select:
        lbr.insert(END, lbl.get(i))
        lbl.delete(i)

def left():
    select = list(lbr.curselection())
    for i in select:
        lbl.insert(END, lbr.get(i))
        lbr.delete(i)

br = Button(frame, text='>>>', command=right)
bl = Button(frame, text='<<<', command=left)

br.pack()
bl.pack()

mainloop()