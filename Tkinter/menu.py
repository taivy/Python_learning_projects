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

def clear_m(event):
    x = event.x
    y = event.y
    menuclear.post(event.x_root, event.y_root)


root = Tk()

mainmenu = Menu(root)
root.config(menu=mainmenu)

mainmenu.add_command(label='Открыть', command=insertText)
mainmenu.add_command(label='Сохранить', command=extractText)

menuclear = Menu(tearoff=0)
menuclear.add_command(label="Очистить", command=clear_t)

text = Text(width=50, height=25)
text.grid(columnspan=3)

text.bind("<Button-3>", clear_m)

root.mainloop()

