
from tkinter import Tk, Button
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import lxml
import requests
# https://ngrok.com/
# ngrok config add-authtoken 2Sjy0F689bedqNileftPv0MrN2C_by1QTJdKWbf6R1qiSuyc - скачиваем на компьютер. открываем зип и в той же папке сделать 2 текстовых файла с расширением bat
import os
from flask import Flask
from multiprocessing import Process  # симулировали каждый вызов ф-ции отдельным процессом, параллельным.так можно ф-ции(приложения) запускать параллельно.минус - нагрузка на операционку
import threading

"""
Asyncio - модуль асинхронного программирования, который был представлен в Питон. Все карутины содержат точки и ты переключаемся между ними
"""
import signal, sys, json, asyncio, aiohttp
from lib import count_word_at_url
from redis import Redis  # для организации очереди. он считает кол-во слов на сайте
from rg import Queue

q = Queue(connection=Redis())
job = q.enqueue(count_word_at_url, 'https://quotes.toscrape.com')



# loop = asyncio.get_event_loop()  # все будет выполняться независимо и асинхронно
# client = aiohttp.ClientSession(loop=loop)
#
# async def get_json(client, url):
#     async with client.get(url) as response:
#         assert response.status == 200  # утверждение. если не так - выбросится искл-е
#         return await response.read()
#
#
# async def get_reddit_top(subreddit, client):
#     url = 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5'
#     print(url)
#     data1 = await get_json(client, url)
#     j = json.loads(data1.decode('utf-8'))
#     for i in j['data']['children']:
#         score = i['data']['score']
#         title = i['data']['title']
#         link = i['data']['url']
#         print(str(score) + ': ' + title + ' (' + link + ')')
#     print('Готово:', subreddit + '\n')
#
#     def signal_handler(signal, frame):
#         loop.stop()
#         client.close()
#         sys.exit(0)
#
#     signal.signal(signal.SIGINT, signal_handler)
#
#     # asyncio.ensure_future(get_reddit_top('python', 'client'))
#     asyncio.ensure_future(get_reddit_top('programming', 'client'))
#     asyncio.ensure_future(get_reddit_top('compsci', 'client'))
#     loop.run_forever()




# def print_name(prefix):
#     print(f'Ищем префикс {prefix}')
#     try:
#         while True:
#             name = (yield)
#             if prefix in name:
#                 print(name)
#     except GeneratorExit:
#         print('Корутина (coroutine) завершена')
#
# corou = print_name('Уважаемый')
# corou.__next__()
# corou.send('товарищ')
# corou.send('Уважаемый товарищ')
# corou.close()




# def print_cube(num):
#     """
#     Вычисляет куб от заданного числа num (комментарий к методу по PEP8)
#     """
#
#     print(f'Куб {num} -> {num * num * num}')
#
#
# def print_square(num):
#
#  """
# Вычисляет квадрат от заданного числа num
#  """
#
# print(f'Квадрат {num} -> {num ** 2}')
#
# if __name__ == '__main__':
#     # создаем 2 потока
#     thread1 = threading.Thread(target=print_square, args=(10,))
#     thread2 = threading.Thread(target=print_cube, args=(10,))
#
#     thread1.start()  # запуск первого потока
#     thread2.start()   # запуск второго потока
#
#     thread1.join()  #ожидание пока поток1 завершится
#     thread2.join()  # ожидание пока поток2 завершится
#
#     print('Процессы завершены')




# def print_func(continent='Asia'):
#     print(f'Это - {continent}.')
#
#
# # print_func()
# if __name__ == '__main__':
#     names = ['America', 'Europe', 'Africa']  # подаем ф-ции аргументы
#     procs = []
#     proc = Process(target=print_func)  # вызываем в кач-ве объекта, поэтому скобки не нужны
#     procs.append(proc)
#     proc.start()
#
#     for name in names:  # в цикле перебираем имена
#         proc = Process(target=print_func, args=(name,))
#         procs.append(proc)
#         proc.start()
#
#     for proc in procs:
#         proc.join()   # процессы в связке



# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return 'Flask приветствует Вас'
#
# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))  # прописываем эти 2 строки. чтобы создать ссылку на свой сайт, создать 2 файла с расширением bat, запустить оба, в одном из них будет ссылка  https://3efc-5-17-85-133.ngrok-free.app
#     app.run(host='0.0.0.0', port=port)
# # HEROKU - раньше был бесплатный хостинг




# url = 'https://quotes.toscrape.com/'
#
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# quotes = soup.find_all('span', class_='text')
# authors = soup.find_all('small', class_='author')
# tags = soup.find_all('div', class_='tags')
#
# length = len(quotes)
#
# for index in range(length):
#     print(quotes[index].text)
#     print(f'\t\t\t{authors[index].text}')
#     t = tags[index].find_all('a', class_='tag')
#     for item in t:
#         print(f'\t\t\t{item.text}')


# for q in quotes:
#     print(q.text)
# print(quotes)  # так можно получить код страницы


# class MyButton(Button):
#     def __init__(self, pict, command):
#         self.image = Image.open(pict)
#         self.image = self.image.resize((100, 100))
#         # self.command = command
#         self.pict = ImageTk.PhotoImage(self.image)
#         super().__init__(image=self.pict, command=command)
#
#
# root = Tk()
# root.geometry('800x600')
# root.title('Красивая кнопка')
# image = 'sc.png'
# pict = ImageTk.PhotoImage(file=image)
# Button(root, image=pict, command=lambda: print('click')).pack()
