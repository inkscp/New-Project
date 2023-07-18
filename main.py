
from tkinter import Tk, Button
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import lxml
import requests

url = 'https://quotes.toscrape.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

length = len(quotes)

for index in range(length):
    print(quotes[index].text)
    print(f'\t\t\t{authors[index].text}')
    t = tags[index].find_all('a', class_='tag')
    for item in t:
        print(f'\t\t\t{item.text}')


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
