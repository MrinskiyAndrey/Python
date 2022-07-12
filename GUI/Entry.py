import tkinter as tk

def get_entry():
    value = name.get()              #Получение данных из поля Entry
    if value:
        print(value)
    else:
        print('Empty Entry')

def delete_entry():
    name.delete(0, 'end')           #удаление в строке Entry(начало, конец)


def submit():
    print(name.get())
    print(password.get())
    name.delete(0, 'end')
    password.delete(0, 'end')

win = tk.Tk()
win.geometry(f'400x500+100+200')
win.title('My first Application')

tk.Label(win, text='Имя').grid(row=0, column=0, stick='w')
tk.Label(win, text='Пароль').grid(row=1, column=0, stick='w')

name = tk.Entry(win)                                                                         #Создание поля Entry
name.grid(row=0, column=1, sticky='w')

password = tk.Entry(win, show='*')
password.grid(row=1, column=1)

tk.Button(win, text='get', command=get_entry).grid(row=2, column=0, sticky='we')            #Кнопка получения данных из поля Entry
tk.Button(win, text='delete', command=delete_entry).grid(row=2, column=1, sticky='we')      #Кнопка удаления данных из поля Entry
tk.Button(win, text='Submit', command=submit).grid(row=3, column=0, sticky='we')
tk.Button(win, text='insert', command=lambda : name.insert(0, 'hello'))\
    .grid(row=2, column=2, sticky='we')                                                       #Кнопка вставки данных в поле Entry

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()