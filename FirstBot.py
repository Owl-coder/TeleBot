import dp as dp
import telebot
from telebot import types
import time
import sqlite3
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

TOKEN = "1421524671:AAH4NUmvFI23rJLkIcv41brh5d9z4dRyPko"

bot = telebot.TeleBot(TOKEN)

# cd C:\Users\sulei\PycharmProjects\Bot

name = ''
surname = ''
age = 0
TYPE = 0


@bot.message_handler(commands=['start'])
def start(message):
    if message.text == '/start':
        keyboard = telebot.types.InlineKeyboardMarkup()  # наша клавиатура
        key_yes = telebot.types.InlineKeyboardButton(text='Изучение слов', callback_data='learn')  # кнопка «Да»
        keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
        key_no = telebot.types.InlineKeyboardButton(text='Тренировка слов', callback_data='train')
        keyboard.add(key_no)
        question = "Привет, выбери тип задания"
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, 'Напиши /start')
        time.sleep(1)


# @bot.message_handler(content_types=['text'])



@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "learn":  # call.data это callback_data, которую мы указали при объявлении кнопки
        # код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'one')
        TYPE = 0
    elif call.data == "train":
        TYPE = 1
        bot.send_message(call.message.chat.id, 'two')
    if TYPE == 0:
        # bot.register_next_step_handler(call.message, dialogue_learn)
        dialogue_learn_setting(call.message)
        print('hr')
    if TYPE == 1:
        pass


def dialogue_learn_setting(message):
    print(12)
    connect = sqlite3.connect("data.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM learn")
    res = cursor.fetchall()
    print(res)
    dialogue_learn(res, message)


def dialogue_learn(word_list, message):
    # global msg
    # message = msg
    for i in word_list:
        keyboard = types.ReplyKeyboardMarkup()
        button_1 = types.KeyboardButton(text="Знаю")
        keyboard.add(button_1)
        button_2 = types.KeyboardButton(text="Не знаю")
        keyboard.add(button_2)
        txt = i[0] + " - " + i[1]
        bot.send_message(message.chat.id, text=txt, reply_markup=keyboard)
        if message.text == "Знаю"


@bot.message_handler(lambda message: message.text == "Знаю")
def know(message: types.Message):
    message.reply("Отлично!")


@bot.message_handler(Text(equals="Не Знаю"))
def know(message: types.Message):
    message.reply("Это слово будет показано еще раз!")


def dialogue_train():
    pass


bot.polling(none_stop=True, interval=0)
