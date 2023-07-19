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
import asyncio
import os
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


# asyncio - модуль асинхронного программирования, кторый был представлен в Python
#
# import signal
# import sys
# import json
# import asyncio
# import aiohttp
#
# loop = asyncio.get_event_loop()
# client = aiohttp.ClientSession(loop=loop)
#
# async def get_json(client, url):
#     async with client.get(url) as response:
#         assert response.status == 200
#         return await response.read()
#         # except_AssertionError:
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
# def signal_handler(signal, frame):
#     loop.stop()
#     client.close()
#     sys.exit(0)
#
# signal.signal(signal.SIGINT, signal_handler)
#
# # asyncio.ensure_future(get_reddit_top('python', client))
# asyncio.ensure_future(get_reddit_top('programming', client))
# asyncio.ensure_future(get_reddit_top('compsci', client))
# loop.run_forever()
#
# from lib import count_word_at_url
# from redis import Redis
# from rq import Queue
#
#
#
# q = Queue(connection=Redis())
# job = q.enqueue(count_word_at_url, 'https://quotes.toscrape.com/')

# Асинхронное программирование
#
# import os
# import time
# from datetime import datetime
# import asyncio
#
# import config
#
#
# async def dish(num, prepare, wait):
#
#     """
#     num: номер блюда по порядку
#     prepare: время на подготовку
#     wait: ожидание готовности
#     """
#
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
#     asyncio.run(main()) # запустили асинхронное приготовление
#     delta = int(time.time() - t0)  # затраченное время
#     print(f'В {datetime.now().strftime("%H:%S")} мы закончили')
#     print(f'Затрачено времени - {delta}')

#
# import logging
# import telebot
# import config
# from telebot import types  # для указания типов


# # /start
#
# # инициировали бота
# bot = telebot.TeleBot(config.bot_token)
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("👋 Поздороваться")
#     btn2 = types.KeyboardButton("❓ Задать вопрос")
#     markup.add(btn1, btn2)
#     bot.send_message(message.chat.id,
#                      text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(
#                          message.from_user), reply_markup=markup)
#
#
# @bot.message_handler(content_types=['text'])
# def func(message):
#     if (message.text == "👋 Поздороваться"):
#         bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
#     elif (message.text == "❓ Задать вопрос"):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton("Как меня зовут?")
#         btn2 = types.KeyboardButton("Что я могу?")
#         back = types.KeyboardButton("Вернуться в главное меню")
#         markup.add(btn1, btn2, back)
#         bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
#     elif (message.text == "Как меня зовут?"):
#         bot.send_message(message.chat.id, "У меня нет имени..")
#     elif message.text == "Что я могу?":
#         bot.send_message(message.chat.id, text="Поздороваться с читателями")
#     elif (message.text == "Вернуться в главное меню"):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         button1 = types.KeyboardButton("👋 Поздороваться")
#         button2 = types.KeyboardButton("❓ Задать вопрос")
#         markup.add(button1, button2)
#         bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, text="На такую команду я не запрограммировал..")

#
# name = ''
# surname = ''
# age = 0
#
#
#
#
# bot = telebot.TeleBot(config.bot_token)
#
#
# @bot.message_handler(content_types=['text'])
# def start(message):
#     if message.text == '/start':
#         bot.send_message(message.from_user.id,
#                          "Как тебя зовут?")
#         bot.register_next_step_handler(message, get_name)
#     else:
#         bot.send_message(message.from_user.id,
#                          'Я вас не понял, напишите /start')
#
#
# def get_name(message):
#     global name
#     name = message.text
#     bot.send_message(message.from_user.id,
#                      'Как твоя фамилия имя?')
#     bot.register_next_step_handler(message, get_surname)
#
#
# def get_surname(message):
#     global surname
#     surname = message.text
#     bot.send_message(message.from_user.id,
#                      'Сколько тебе лет?')
#     bot.register_next_step_handler(message, get_age)
#
#
# def get_age(message):
#     global age
#     while age == 0:
#         try:
#             age = int(message.text)
#         except ValueError:
#             bot.send_message(message.from_user.id,
#                      'Вводите цифры')
#             age = 1
#             break
#     quastion = f'Тебе {age} лет , и ты {name} {surname}'
#     keyboard = types.InlineKeyboardMarkup()
#     yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
#     keyboard.add(yes)
#     no = types.InlineKeyboardButton(text='Нет', callback_data='no')
#     keyboard.add(no)
#     bot.send_message(message.from_user.id, text=quastion,
#                      reply_markup=keyboard)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
# # """
# # call.data - callback_data, которую мы указали при объявлении кнопки
# # """
#     if call.data == 'yes':
#         bot.send_message(call.message.chat.id,
#                          'Приятно познакомиться')
#     elif call.data == 'no':
#         bot.send_message(call.message.chat.id,
#                          'Тогда начнем сначала...')
#         bot.register_next_step_handler(call.message, get_name())
#
#
# # запустили бота
# bot.polling(none_stop=True)


import logging  # фиксация действий
import config
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove

# Запустим логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)

reply_buttons = [
    ['/address', '/site'],
    ['/help', '/start']
]

TIMER = 5

markup = ReplyKeyboardMarkup(reply_buttons, one_time_keyboard=False)


def remove_job(name, context):
    current_job = context.job_queue.get_jobs_by_name(name)
    if not current_job:
        return False
    for job in current_job:
        job.schedule_removal()
    return True


"""
Функция обработки сообщений
update - принимает
context - доп. информация о сообщении 
"""


async def echo(update, context):
    await update.message.reply_text(update.message.text)


async def start(update, context):
    """
    Реакция на команду /start
    """
    user = update.effective_user
    await update.message.reply_html(
        rf'Привет {user.mention_html()}! Я эхо-бот. Напишите мне что-то.',
        reply_markup=markup
    )


async def set_timer(update, context):
    chat_id = update.effective_message.chat_id
    job_removed = remove_job(str(chat_id), context)
    context.job_queue.run_once(task, TIMER,
                               chat_id=chat_id,
                               name=str(chat_id),
                               data=TIMER)
    text = f'Буду через {TIMER} сек!'
    if job_removed:
        text += ' Старая задача удалена.'
    await update.effective_message.reply_text(text)


async def task(context):
    await context.bot.send_message(context.job.chat_id,
                                   text=f'Вот и прошли {TIMER} сек.')


async def help_command(update, context):
    await update.message.reply_text('Я простой справочник')


async def unset(update, context):
    chat_id = update.message.chat_id
    job_removed = remove_job(str(chat_id), context)
    text = 'Таймер отменён' if job_removed else 'Таймеры не были установлены'
    await update.message.reply_text(text)


async def address(update, context):
    await update.message.reply_text('Адрес ИПАП: СПб, Можайская, 2')


async def site(update, context):
    await update.message.reply_text('https://google.com')


async def close_keyboard(update, context):
    await update.message.reply_text('Ok', reply_markup=ReplyKeyboardRemove())


def main():
    application = Application.builder().token(config.bot_token).build()
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    application.add_handler(text_handler)
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('address', address))
    application.add_handler(CommandHandler('site', site))
    application.add_handler(CommandHandler('close', close_keyboard))
    application.add_handler(CommandHandler('set', set_timer))
    application.add_handler(CommandHandler('unset', unset))
    application.run_polling()


if __name__ == '__main__':
    main()



