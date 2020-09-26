import asyncio
import io
import logging
import threading
import time
from multiprocessing.context import Process

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputMediaDocument, KeyboardButton, ReplyKeyboardMarkup
from urllib.request import urlopen
import json
import sqlite3
#--------------------Настройки бота-------------------------

# Ваш токен от BotFather
TOKEN = '1366803662:AAG-hV14FHfSjIS87nScCRCXKb8ZcN-A24c'


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Ваш айди аккаунта администратора и айди сообщения где хранится файл с данными
admin_id=852450369
config_id=4

# conn = sqlite3.connect("mydb.db")  # или :memory: чтобы сохранить в RAM
# cursor = conn.cursor()


# #--------------------Получение данных-------------------------
async def get_data():
    to = time.time()
    # Пересылаем сообщение в данными от админа к админу
    forward_data = await bot.forward_message(admin_id, admin_id, config_id)

    # Получаем путь к файлу, который переслали
    file_data = await bot.get_file(forward_data.document.file_id)

    # Получаем файл по url
    file_url_data = bot.get_file_url(file_data.file_path)
    data_db=urlopen(file_url_data).read()
    # Считываем данные с файла
    f = open('database.sqlite', 'wb')
    f.write(data_db)
    f.close()
    print('Время получения бекапа :=' + str(time.time() - to))
    timer_start()
    thread1 = threading.Thread(target=logic)
    thread1.start()
    # Переводим данные из json в словарь и возвращаем



#--------------------Сохранение данных-------------------------
async def save_data():
    to = time.time()

    try:
        # Переводим словарь в строку
        f = open("database.sqlite", "rb")

        # Обновляем  наш файл с данными
        await bot.edit_message_media(InputMediaDocument(f), admin_id, config_id)

    except Exception as ex:
        print(ex)
    print('Время сохранения бекапа:='+str(time.time() - to))

#--------------------Метод при нажатии start-------------------------
@dp.message_handler(commands='start')
async def start(message: types.Message):
    # Добавляем нового пользователя
    await bot.send_message(message.chat.id,'Приветствую {}'.format(message.chat.first_name))



#--------------------Основная логика бота-------------------------
@dp.message_handler()
async def main_logic(message: types.Message):

    to=time.time()
# Логика для администратора
    if message.text == 'admin':
        # cursor.execute("CREATE TABLE users (chatid INTEGER , name TEXT, click INTEGER, state INTEGER)")
        # cursor.execute("INSERT INTO users VALUES (1234, 'eee', 1,0)")
        # conn.commit()
        # sql = "SELECT * FROM users "
        # cursor.execute(sql)
        # data = cursor.fetchall()
        # str_data = json.dumps(data)
        f = open("database.sqlite", "rb")
        await bot.send_document(message.chat.id, f)
        await bot.send_message(message.chat.id, 'admin_id = {}'.format(message.chat.id))
        await bot.send_message(message.chat.id, 'config_id = {}'.format(message.message_id+1))
    print(time.time()-to)


def logic():
    import main

def timer_start():
    threading.Timer(120.0, timer_start).start()
    try:
        asyncio.run_coroutine_threadsafe(save_data(),bot.loop)
    except Exception as exc:
        print(exc)

def main_start():
    print('start lol')
    try:
        asyncio.run_coroutine_threadsafe(get_data(), bot.loop)
    except Exception as exc:
        print(exc)
    timer_start()
    executor.start_polling(dp, skip_updates=True)

def proc_start():
    print('gogo')
    proc =  Process(target=main_start)
    proc.start()
#--------------------Запуск бота-------------------------
if __name__ == '__main__':
    try:
        asyncio.run_coroutine_threadsafe(get_data(), bot.loop)
    except Exception as exc:
        pass

    executor.start_polling(dp, skip_updates=True)