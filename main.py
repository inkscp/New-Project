
from tkinter import Tk, Button
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import lxml
import requests
# https://ngrok.com/
# ngrok config add-authtoken 2Sjy0F689bedqNileftPv0MrN2C_by1QTJdKWbf6R1qiSuyc - скачиваем на компьютер. открываем зип и в той же папке сделать 2 текстовых файла с расширением bat
import os
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask приветствует Вас'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # прописываем эти 2 строки. чтобы создать ссылку на свой сайт, создать 2 файла с расширением bat, запустить оба, в одном из них будет ссылка  https://3efc-5-17-85-133.ngrok-free.app
    app.run(host='0.0.0.0', port=port)
# HEROKU - раньше был бесплатный хостинг




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
