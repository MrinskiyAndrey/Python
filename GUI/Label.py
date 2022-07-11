import tkinter as tk

#Создание окна
root = tk.Tk()                               #Обьявление перменной названия окна и типа Тк
root.title('моё приложение')                 #Заголовок
root.config(bg='#ffaaaa')                    #установка заднего фона окна
root.geometry('900x600+100+100')             #Размеры окнна(ширина, высота, отступы от края экрана)
root.minsize(200, 100)
root.maxsize(1200, 1100)                    #Объявление минимальных и максимальных размеров окна
root.resizable(True, True)                  #Включение и выключение возмжности изменения размеров окна(ширина, высота)
photo = tk.PhotoImage(file='fun.png')       #Подгрузка картинки из корня
root.iconphoto(False, photo)                #Установка иконки окна


#Виджит Label
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
root.mainloop()