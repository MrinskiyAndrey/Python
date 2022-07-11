import tkinter as tk

#Создание окна___________________________________________________________________________________________
root = tk.Tk()                               #Обьявление перменной названия окна и типа Тк
root.title('моё приложение')                 #Заголовок
root.config(bg='#ffaaaa')                    #установка заднего фона окна
root.geometry('900x600+100+100')             #Размеры окнна(ширина, высота, отступы от края экрана)
root.minsize(200, 100)
root.maxsize(1200, 1100)                    #Объявление минимальных и максимальных размеров окна
root.resizable(True, True)                  #Включение и выключение возмжности изменения размеров окна(ширина, высота)
photo = tk.PhotoImage(file='fun.png')       #Подгрузка картинки из корня
root.iconphoto(False, photo)                #Установка иконки окна


#Виджит Label_____________________________________________________________________________________________
labal_1 = tk.Label(root, text='Hello World',    #Создание лейбла
                   bg='red',                    #цвет лефбла
                   fg='white',                  #цвет фона лейбла
                   font=('Arial', 20, 'bold'),  #шрифт, размер, тип
                   padx=20,
                   pady=20,                     #отcтупы по x, y от текста
                   width=20,                    #ширина
                   height=5,                    #высота
                   anchor='s',                  #прикрепление у стороне света(n, ne, e, se, s, sw, w, nw, center)
                   relief=tk.RAISED,            #обтекание (контур лейбла)
                   bd=20,                       #ширина границ (обтекания)
                   justify=tk.LEFT              #Выравнивание теста по краю (LEFT, RIGHT, CENTER)
                   )
labal_1.pack()

#Виджит  Button________________________________________________________________________________________________
count = 0

def say_hello():                                #Функция для кнопки выводящей текст в консоль
    print('Hello world')

def add_label():
    label2=tk.Label(root, text='NEW LABEL')     #Функция для кнопки создающей лейбл
    label2.pack()

def counter():                                  #Функция для подсчета количества нажатия кнопки 4
    global count
    count+=1
    btn_4['text'] = f'Счетчик: {count}'




btn_1 = tk.Button(root, text='Button1',         #Кнопка выводящая текст в консоль
                  command=say_hello)
btn_1.pack()


btn_2 = tk.Button(root, text='Button2',         #Кнопка создающая лейбл
                  command=add_label)
btn_2.pack()


btn_3 = tk.Button(root, text='Button3',         #кнопка использующая лябда функцию, для создания лейбла
                  command=lambda : tk.Label(root, text='lambda LABEL').pack())
btn_3.pack()


btn_4 = tk.Button(root, text=f'Счетчик: {count} ',         #кнопка счетчик нажатий
                  command=counter,
                  bg='yellow',
                  activebackground='green'                  #изменение цвета кнопки во время нажатия
                  )
btn_4.pack()


root.mainloop()                             #Запуск цикла