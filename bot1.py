from re import match
from unittest import case

from pyowm import OWM
import telebot
from telebot import types
from pyowm.utils import config
from pyowm.utils import timestamps
from telebot import TeleBot
# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, "Добро пожаловать, я чат-бот и я умею делать некоторые вещи: \n"
                                           "1. Могу вывести тебе твое расписание на конкретный день учитывая четную и нечетную неделю \n"
                                           "2. Могу сказать тебе подробную погоду в Казани на сегодняшний день \n"
                                           "Пример: /rasp, /weather")
# ==================================================================================================
# @bot.message_handler(content_types=['text'])
@bot.message_handler(commands=['weather'])
def weatherW(message2):
    # if message2.text == '2':
    owm = OWM("API key")
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place('Kazan, RU')
    w = observation.weather

    w.detailed_status  # 'clouds'
    w.wind()    # {'speed': 4.6, 'deg': 330}
    w.humidity  # 87
    w.temperature('celsius')    # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    w.rain  # {}
    w.heat_index  # None
    w.clouds  # 75

    bot.send_message(message2.from_user.id, "-- г.Казань - Погода на сегодняшний день -- \n"
                                            "Температура: {} градуса по Цельсию \n"
                                            "Облака: {} \n"
                                            "Ветер: {} м/c \n"
                                            "Влажность: {} % \n"
                                            "Дождь: {} \n"
                                            "Тепловой индекс: {} \n".format(w.temperature('celsius')['temp'], w.detailed_status, w.wind()['speed'],
                                                                    w.humidity, w.rain, w.heat_index))

flag = True
q = 1
@bot.message_handler(content_types=['text'])
@bot.message_handler(commands=['rasp'])
def raspR(message1):

    global q
    global flag
    match q:
        case 1:
            while flag == True:
                bot.send_message(message1.from_user.id, 'Какой сегодня день недели?')
                flag = False
            s = message1.text

            if s.lower() == "понедельник" or s.lower() == 'пн':
                q = 2
                bot.send_message(message1.chat.id, 'Четная или нечетная неделя?')

            elif s.lower() == "вторник" or s.lower() == 'вт':
                q = 3
                bot.send_message(message1.chat.id, 'Четная или нечетная неделя?')
            elif s.lower() == "среда" or s.lower() == 'ср':
                q = 4
                bot.send_message(message1.chat.id, 'Четная или нечетная неделя?')
            elif s.lower() == "четверг" or s.lower() == 'чт':
                q = 5
                bot.send_message(message1.chat.id, 'Четная или нечетная неделя?')
            elif s.lower() == "пятница" or s.lower() == 'пт':
                q = 6
                bot.send_message(message1.chat.id, 'Четная или нечетная неделя?')
            elif s.lower() == "суббота" or s.lower() == 'сб':
                q = 7
                bot.send_message(message1.chat.id, 'Четная или нечетная неделя?')
            elif s.lower() == "воскресенье" or s.lower() == 'вс':
                bot.send_message(message1.from_user.id, 'Сегодня выходной :)')
        case 2:

            s1 = message1.text
            if s1.lower() == 'четная' or s1.lower() == 'чет':
                bot.send_message(message1.from_user.id, '12:00 - 13:30 Физическая культура \n'
                                                        '15:40 - 17:10 Объекто ориентированный анализ \n'
                                                        '17:50 - 19:20 Теория автоматов и формальных языков \n')
                q = 1
                flag = True
            elif s1.lower() == 'нечетая' or s1.lower() == 'нечет':
                bot.send_message(message1.from_user.id, '12:00 - 13:30 Физическая культура \n'
                                                        '15:40 - 17:10 Объекто ориентированный анализ \n'
                                                        '17:50 - 19:20 Теория автоматов и формальных языков \n')
                q = 1
                flag = True
        case 3:

            s1 = message1.text
            if s1.lower() == 'четная' or s1.lower() == 'чет':
                bot.send_message(message1.from_user.id, '8:30 - 10:00 Языки и методы программирования \n'
                                                        '10:10 - 11:40 Технологическая практика \n')
                q = 1
                flag = True
            elif s1.lower() == 'нечетая' or s1.lower() == 'нечет':
                bot.send_message(message1.from_user.id, '8:30 - 10:00 Языки и методы программирования')
                q = 1
                flag = True

        case 4:

            s1 = message1.text
            if s1.lower() == "четная" or s1.lower() == 'чет':
                bot.send_message(message1.from_user.id, '14:00 - 15:30 Английский язык \n'
                                                        '15:40 - 17:10 Языки и методы программирования \n')
                q = 1
                flag = True
            elif s1.lower() == "нечетная" or s1.lower() == 'нечет':
                bot.send_message(message1.from_user.id, '14:00 - 15:30 Английский язык \n'
                                                        '15:40 - 17:10 Объекто ориентированный анализ \n'
                                                        '17:50 - 19:20 Объекто ориентированный анализ \n')
                q = 1
                flag = True

        case 5:

            s1 = message1.text
            if s1.lower() == "нечетная" or s1.lower() == 'нечет':
                bot.send_message(message1.from_user.id, '10:10 - 11:40 Теория автоматов и формальных языков \n'
                                                        '12:00 - 13:30 Физическая культура \n'
                                                        '14:00 - 15:30 Проектированние человекомашинного интерфейса \n')
                q = 1
                flag = True
            elif s1.lower() == "четная" or s1.lower() == 'чет':
                bot.send_message(message1.from_user.id, '10:10 - 11:40 Базы данных \n'
                                                        '12:00 - 13:30 Физическая культура \n'
                                                        '14:00 - 15:30 Проектированние человекомашинного интерфейса \n')
                q = 1
                flag = True

        case 6:


            bot.send_message(message1.from_user.id, '10:10 - 11:40 Математическая логика \n'
                                                    '17:50 - 19:20 Проектированние человекомашинного интерфейса \n')
            q = 1
            flag = True

        case 7:

            s1 = message1.text
            if s1.lower() == "четная" or s1.lower() == 'чет':
                bot.send_message(message1.from_user.id, '8:30 - 10:00 Архитектура вычислительных систем \n'
                                                        '10:10 - 11:40 Математическая логика \n'
                                                        '11:50 - 13:20 Базы данных \n')
                q = 1
                flag = True
            elif s1.lower() == "нечетная" or s1.lower() == 'нечет':
                bot.send_message(message1.from_user.id, '8:30 - 10:00 Архитектура вычислительных систем \n'
                                                        '10:10 - 11:40 Математическая логика \n'
                                                        '11:50 - 13:20 Архитектура вычислительных систем \n')
                q = 1
                flag = True
# ==================================================================================================
bot.polling(none_stop=True, interval=0)