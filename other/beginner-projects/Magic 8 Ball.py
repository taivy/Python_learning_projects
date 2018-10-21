# coding=utf-8

from random import choice
from tkinter import *
from PIL import Image, ImageTk

answers = ['Весьма сомнительно', 'Перспективы не очень хорошие', 'По моим данным — «нет»', 'Мой ответ — «нет»',
           'Даже не думай', 'Сконцентрируйся и спроси опять', 'Сейчас нельзя предсказать', 'Лучше не рассказывать',
           'Спроси позже', 'Пока не ясно, попробуй снова', 'Да', 'Знаки говорят — «да»', 'Хорошие перспективы',
           'Вероятнее всего', 'Мне кажется — «да»', 'Можешь быть уверен в этом', 'Определённо да', 'Никаких сомнений',
           'Предрешено', 'Бесспорно']

def ask():
    answer = choice(answers)
    panel['text'] = answer

def clear():
    entry.delete(0, END)


root = Tk()

path = r'C:\Users\User1\Downloads\240px-Magic_eight_ball.png'

img = ImageTk.PhotoImage(Image.open(path))
panel = Label(root, image = img, fg='white', compound=CENTER)
panel.pack(side = "bottom", fill = "both", expand = "yes")

entry = Entry(width=38)
entry.pack()

frame = Frame()
frame.pack()

Button(frame, text='Ask', command=ask, width=10).pack(side=LEFT)
Button(frame, text='Clear', command=clear, width=10).pack(side=LEFT)
Button(frame, text="Quit", command=root.destroy, width=5).pack(side=LEFT)


root.mainloop()