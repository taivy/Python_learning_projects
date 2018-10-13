from tkinter import *
root = Tk()

c = Canvas(root, width=200, height=230, bg='white')
c.pack()

c.create_rectangle(50, 100, 150, 200, fill='#61B7CF', outline='white')
c.create_polygon((40, 100), (160, 100), (100, 70), fill='#61B7CF', outline='white')
c.create_oval(150, 10, 190, 50, fill='yellow', outline='white')

x = 0
for i in range(20):
    y = 230
    b = 7
    y1 = y
    for j in range(13):
        y2 = y1 - b
        c.create_line(x, y1, x, y2, fill='green', width=3)
        x += 2
        b -= 0.6
        y1 = y2
    x -= 15

root.mainloop()

