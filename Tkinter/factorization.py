'''
https://younglinux.info/tkinter/gcd
'''



from tkinter import *

root = Tk()

def calc():
    a = int(e1.get())
    b = int(e2.get())
    la = []
    lb = []
    c = 2
    while a != 1:
        if a % c == 0:
            la += str(c)
            a = a / c
        else:
            c += 1
    c = 2
    while b != 1:
        if b % c == 0:
            lb += str(c)
            b = b / c
        else:
            c += 1

    Lb_4['text'] = ' '.join(la)
    Lb_5['text'] = ' '.join(lb)



Lb_1 = Label(text='Число 1')
Lb_2 = Label(text='Число 2')

Lb_1.grid(row=1, column=0)
Lb_2.grid(row=2, column=0)


Lb_3 = Label(text='Простые сомножители')
Lb_3.grid(row=0, column=2, columnspan=2)


Lb_4 = Label(bg='white')
Lb_5 = Label(bg='white')

Lb_4.grid(row=1, column=2, columnspan=2)
Lb_5.grid(row=2, column=2, columnspan=2)

Lb_nok = Label(text='НОК', bg='blue')
Lb_nod = Label(text='НОД', bg='green')

Lb_nok.grid(row=3, column=2, sticky=W+E)
Lb_nod.grid(row=4, column=2, sticky=W+E)


e1 = Entry()
e2 = Entry()
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

btn = Button(text='Вычислить', command=calc)
btn.grid(row=3, column=0, columnspan=2, rowspan=2, sticky=N+S+W+E)


mainloop()
