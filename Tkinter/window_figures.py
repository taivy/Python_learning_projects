from tkinter import *

root = Tk()

c = Canvas(width=300, height=300, bg='white')

def add():
    a = Toplevel()
    a.geometry('+200+100')
    a.title('Фигура')
    a.resizable(True, True)


    lx1 = Label(a, text='x1')
    ly1 = Label(a, text='y1')

    lx2 = Label(a, text='x2')
    ly2 = Label(a, text='y2')

    ex1 = Entry(a, width=5)
    ey1 = Entry(a, width=5)

    ex2 = Entry(a, width=5)
    ey2 = Entry(a, width=5)

    var = IntVar()

    pr = Radiobutton(a, text='Прямоугольник', variable=var, value=0)
    ov = Radiobutton(a, text='Овал', variable=var, value=1)

    def draw():
        v = var.get()
        if v == 0:
            c.create_rectangle(ex1.get(), ey1.get(), ex2.get(), ey2.get())
        elif v == 1:
            c.create_oval(ex1.get(), ey1.get(), ex2.get(), ey2.get())
        a.destroy()

    bdraw = Button(a, text='Нарисовать', command=draw)

    lx1.grid(row=0, column=0, pady=5, sticky=E)
    ex1.grid(row=0, column=1, pady=5)

    ly1.grid(row=0, column=3, pady=5, sticky=E)
    ey1.grid(row=0, column=4, pady=5)

    lx2.grid(row=1, column=0, pady=5, sticky=E)
    ex2.grid(row=1, column=1, pady=5)

    ly2.grid(row=1, column=3, pady=5, sticky=E)
    ey2.grid(row=1, column=4, pady=5)

    pr.grid(row=2,  column=0, columnspan=5, sticky=W)
    ov.grid(row=3, column=0, columnspan=5, sticky=W)

    bdraw.grid(row=4, column=0, columnspan=5, padx=10, pady=10)

root.title('Прямовал')

badd = Button(text='Добавить фигуру', command=add)

c.pack()
badd.pack()


root.mainloop()