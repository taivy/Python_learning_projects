from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb


def insertText():
    file_name = fd.askopenfilename()
    if file_name == '':
        mb.showerror("Ошибка", "Файл не загружен")
    else:
        f = open(file_name)
        s = f.read()
        text.insert(1.0, s)
        f.close()


def extractText():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                ("HTML files", "*.html;*.htm"),
                                                ("All files", "*.*")))
    if file_name == '':
        mb.showerror("Ошибка", "Файл не сохранен")
    else:
        f = open(file_name, 'w')
        s = text.get(1.0, END)
        f.write(s)
        f.close()

def clear_t():
    answer = mb.askyesno('Подтвердите удаление текста', 'Удалить текст?')
    if answer == True:
        text.delete(1.0, END)

root = Tk()
text = Text(width=50, height=25)
text.grid(columnspan=3)
b1 = Button(text="Открыть", command=insertText)
b1.grid(row=1, sticky=E)
b2 = Button(text="Сохранить", command=extractText)
b2.grid(row=1, column=1)
bc = Button(text='Очистить', command=clear_t)
bc.grid(row=1, column=2, sticky=W)

root.mainloop()

