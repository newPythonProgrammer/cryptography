from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText

root = Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2  # середина экрана
h = h // 2
w = w - 250  # смещение от середины
h = h - 330
root.geometry(f'500x500+{w}+{h}')  # Устанавливаю размер окна
root.resizable(False, False)  # делаю чтоб окно нельзя было изменять в размере
root.title('Шифр цезаря')

SYMVOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 ?!'
translete = ''


def crypt():
    global translete
    msg = in_txt.get(0.0, END)
    for symbol in msg:
        if symbol in SYMVOLS:
            symbolIndex = SYMVOLS.find(symbol)
            k = key.get()
            k = int(k)
            translatedIndex = symbolIndex + k

            if translatedIndex >= len(SYMVOLS):
                translatedIndex -= len(SYMVOLS)
            elif translatedIndex < 0:
                translatedIndex += len(SYMVOLS)
            translete += SYMVOLS[translatedIndex]
        else:
            translete += symbol
        out_txt.delete(0.0, END)
        out_txt.insert(0.0, translete)


def nocrypt():
    global translete
    msg = in_txt.get(0.0, END)
    for symbol in msg:
        if symbol in SYMVOLS:
            symbolIndex = SYMVOLS.find(symbol)
            k = key.get()
            k = int(k)
            translatedIndex = symbolIndex - k

            if translatedIndex >= len(SYMVOLS):
                translatedIndex -= len(SYMVOLS)
            elif translatedIndex < 0:
                translatedIndex += len(SYMVOLS)
            translete += SYMVOLS[translatedIndex]
        else:
            translete += symbol
        out_txt.delete(0.0, END)
        out_txt.insert(0.0, translete)


Label(text='Введите текст').pack(anchor=W)
in_txt = ScrolledText(height=10, font=('FranklinGothic'))
in_txt.pack()
Label(text='Ключ').pack()
key = Entry()
key.pack(anchor=S)
encrypt = Button(text='Encrypt', command=crypt)
encrypt.pack()
decrypt = Button(text='Decrypt', command=nocrypt)
decrypt.pack()
Label(text='Получите текст').pack(anchor=W)
out_txt = ScrolledText(font=('FranklinGothic') )
out_txt.pack()

root.mainloop()
