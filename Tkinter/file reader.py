from tkinter import *
root = Tk()
frame = Frame()
frame.pack()

def open_f():
    f = entry.get()
    with open(f, 'r') as inf:
        f_text = inf.readlines()
        text.insert(1.0, f_text)

def save_f():
    f = entry.get()
    with open(f, 'w') as ouf:
        f_text = text.get(1.0, END)
        ouf.write(f_text)

entry = Entry(frame)
entry.pack(side=LEFT)

open_b = Button(frame, text='Открыть', command=open_f)
open_b.pack(side=LEFT)

save_b = Button(frame, text='Сохранить', command=save_f)
save_b.pack(side=LEFT)

text = Text(wrap=WORD)
text.pack(side=LEFT)

scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)

root.mainloop()

