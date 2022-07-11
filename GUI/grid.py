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


btn1=tk.Button(root, text='Hello_1')
btn2=tk.Button(root, text='Hello_2')
btn3=tk.Button(root, text='Hello_3')
btn4=tk.Button(root, text='Hello_4')
btn5=tk.Button(root, text='Hello_5')
btn6=tk.Button(root, text='Hello_6')
btn7=tk.Button(root, text='Hello_7')
btn8=tk.Button(root, text='Hello_8')

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=1, column=0)
btn4.grid(row=1, column=1)
btn5.grid(row=2, column=0)
btn6.grid(row=2, column=1)
btn7.grid(row=3, column=0, columnspan=2, sticky='we')             #широкая кнопка по горизонтали
btn8.grid(row=0, column=3, rowspan=4, sticky='ns')                #Длинная кнопка по вертикали

root.columnconfigure(0, minsize=200)





root.mainloop()