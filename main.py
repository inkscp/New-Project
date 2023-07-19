import asyncio
from tkinter import Tk, Button
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import lxml
import requests
# https://ngrok.com/
# ngrok config add-authtoken 2Sjy0F689bedqNileftPv0MrN2C_by1QTJdKWbf6R1qiSuyc - скачиваем на компьютер. открываем зип и в той же папке сделать 2 текстовых файла с расширением bat
import os
from flask import Flask
from multiprocessing import \
    Process  # симулировали каждый вызов ф-ции отдельным процессом, параллельным.так можно ф-ции(приложения) запускать параллельно.минус - нагрузка на операционку
import threading
import telebot
from telebot import types  # для указания типов
import config

# /start

# инициировали бота
bot = telebot.TeleBot(config.bot_token)


@bot.message_handler(commands=['start'])  # реагируем на '/start'
def start(message):
    # создаем кнопку-ссылку. 0.first_name - то, как ты зарегистрированы в телеге
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Поздороваться')
    btn2 = types.KeyboardButton('Задать вопрос')
    markup.add(btn1, btn2)  # добавляем в контейнер кнопки, так мы их регистрируем
    bot.send_message(message.chat.id, text='Привет, {0.first_name}! '
                                           'Я бот, приятно познакомиться)'.format(message.from_user),
                     reply_markup=markup)  # это я

@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Поздороваться":
        bot.send_message(message.chat.id, text='Привет. Спасибо. что зашел!')
    elif message.text == "Задать вопрос":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Как меня зовут?')
        btn2 = types.KeyboardButton('Что я умею?')
        back = types.KeyboardButton('Назад в главное меню')
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text='Задайте мне вопрос', reply_markup=markup)
    elif message.text == 'Как меня зовут?':
        bot.send_message(message.chat.id, text='Я всего лишь бот')
    elif message.text == 'Что я умею?':
        bot.send_message(message.chat.id, text='Здороваться')
    elif message.text == 'Назад в главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Поздороваться')
        button2 = types.KeyboardButton('Задать вопрос')
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text='Вы вернулись в главное меню', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text='Я не знаю такой команды')

# запустили бота
bot.polling(non_stop=True)  # будет работать пока мы его не остановим

# """
# Asyncio - модуль асинхронного программирования, который был представлен в Питон. Все карутины содержат точки и ты переключаемся между ними
# """
# # from lib import count_word_at_url
# # from redis import Redis  # для организации очереди. он считает кол-во слов на сайте
# # from rg import Queue
# import time
# from datetime import datetime
#
# def dish(num, prepare, wait):
#     """
#
#     :param num: номер блюда п\п
#     :param prepare: время на подготовку
#     :param wait: ожидание готовности
#     """
#     print(f'Подготовка к приготовлению блюда {num} - {datetime.now().strftime("%H:%S")} - подготовка к приготовлению блюда {num} - {prepare} мин.')
#     time.sleep(prepare)
#     print(f'Начало приготовления блюда {num} - {datetime.now().strftime("%%H:%S")}. Ожидание блюда {num} {wait} мин.')
#     time.sleep(wait)
#     print(f'В {datetime.now().strftime("%%H:%S")}. Блюдо {num} готово.')
#
#     t0 = time.time() # время начала работы
#     dish(1, 2, 3)
#     dish(2, 5, 10)
#     dish(3, 3, 5)
#     delta = int(time.time() - t0)  # затраченное время
#     print(f'0{datetime.now().strftime("%%H:%S")} мы закончили')
#     print(f'Затраченное время {delta}')

# асинхронный вариант
# async def dish(num, prepare, wait):
#     """
#     num: номер блюда по порядку
#     prepare: время на подготовку
#     wait: ожидание готовности
#     """
#     print(f'{datetime.now().strftime("%H:%S")} - подготовка к приготовлению блюда {num} - {prepare} мин.')
#     time.sleep(prepare)
#     print(f'Начало приготовления блюда {num} - {datetime.now().strftime("%H:%S")}. Ожидание блюда {num} {wait} мин.')
#     await asyncio.sleep(wait)
#     print(f'В {datetime.now().strftime("%H:%S")}. блюдо {num} готово.')
#
# async def main():
#     tasks = [
#         asyncio.create_task(dish(1, 2, 3)),
#         asyncio.create_task(dish(2, 5, 10)),
#         asyncio.create_task(dish(3, 3, 5))
#     ]
#     await asyncio.gather(*tasks)
#
# if __name__ == '__main__':
#     t0 = time.time()  # время начало работы
#     if os.name == 'nt':
#         asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#     asyncio.run(main())  # запустили асинхронное приготовление
#     delta = int(time.time() - t0)  # затраченное время
#     print(f'В {datetime.now().strftime("%H:%S")} мы закончили')
#     print(f'Затрачено времени - {delta}')

# q = Queue(connection=Redis())
# job = q.enqueue(count_word_at_url, 'https://quotes.toscrape.com')


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
