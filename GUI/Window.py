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

root.mainloop()