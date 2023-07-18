# from tkinter import Tk, Button
# from PIL import ImageTk, Image
#
#
# class MyButton(Button):
#     def __init__(self, pict, command):
#         self.image = Image.open(pict)
#         self.image = self.image.resize((100, 100))
#         self.pict = ImageTk.PhotoImage(self.image)
#         super().__init__(image=self.pict, command=command)
#
# root = Tk()
# root.geometry('800x600')
# root.title('Красивая кнопка')
# image = 'image.jpg'
# # pict = ImageTk.PhotoImage(file=image)
# # Button(root, image=pict, command=lambda: print('click')).pack()
# MyButton('image.jpg', command=lambda: print('click')).pack()
# root.mainloop()

# https://quotes.toscrape.com/
# Парсинг

#
# from bs4 import BeautifulSoup
# import lxml
# import requests
#
#
# url = 'https://quotes.toscrape.com/'
#
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# quotes = soup.find_all('span', class_='text')
# author = soup.find_all('small', class_='author')
# tags = soup.find_all('div', class_='tags')
#
# length = len(quotes)
#
# for index in range(length):
#     print(quotes[index].text)
#     print(f'\t\t\{author[index].text}')
#     t = tags[index].find_all('a', class_='tag')
#     for item in t:
#         print(f'\t\t\t#{item.text}')

# for q in quotes:
#     print(q.text)

# print(quotes)
# https://ngrok.com/

# import os
# from flask import Flask
#
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return 'Flask приветствует вас'
#
# if __name__=='__main__':
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)

#
# from multiprocessing import Process
#
#
# def print_func(continent='Asia'):
#     print(f'Это -{continent}.')
#
# if __name__ == '__main__':
#     names = ['America', 'Europe', 'Africa']
#     procs = []
#     proc = Process(target=print_func)
#     procs.append(proc)
#     proc.start()
#
#     for name in names:
#         proc = Process(target=print_func, args=(name,))
#         procs.append(proc)
#         proc.start()
#
#     for proc in procs:
#         proc.join()
#
#
# import threading
#
#
# def print_cube(num):
#     """
#     Вычисляет куб от заданного числа num
#     """
#     print(f'Куб {num} -> {num * num * num}')
#
#
# def print_squre(num):
#     """
#     Вычисляет квадрат от заданного числа num
#     """
#     print(f'Квадрат {num} -> {num ** 2}')
#
# if  __name__ == '__main__':
#     # создаем два потока
#     thread1 = threading.Thread(target=print_squre, args=(10,))
#     thread2 = threading.Thread(target=print_cube, args=(10,))
#
#     thread1.start()  # запуск первого потока
#     thread2.start()  # запуск второго потока
#
#     thread1.join()  # ожидание пока поток 1 завершится
#     thread2.join()  # ожидание пока поток 2 завершится
#
#     print('Процессы завершены')


def print_name(prefix):
    print(f'Ищем префикс {prefix}')
    try:
        while True:
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print('Корутина (coroutine) завершена')

corou = print_name('Уважаемый')
corou.__next__()
corou.send('товарищ')
corou.send('Уважаемый товарищ')