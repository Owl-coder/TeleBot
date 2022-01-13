import dp as dp
import telebot
from telebot import types
import sqlite3
from random import randint
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

TOKEN = "1421524671:AAH4NUmvFI23rJLkIcv41brh5d9z4dRyPko"

bot = telebot.TeleBot(TOKEN)

# cd C:\Users\sulei\PycharmProjects\Bot

TYPE = 0
text_right = '''Правильный ответ'''
text_wrong = '''Неправильный ответ
Вопрос будет показан еще раз'''

@bot.message_handler(commands=['help'])
def help(message):
    text = '''Этот бот создан для изучения математических терминов на английском языке
    В нем есть 2 режима: learn и train, любой из которых можно выбрать после запуска бота командой /start
    Лучше сначала пройти learn режим, а потом train
    Основные команды:
    /start - начало работы
    /reset - сброс прогресса
    /help - информация'''
    bot.send_message(message.from_user.id, text=text)


@bot.message_handler(commands=['reset'])
def reset(message):
    connect = sqlite3.connect("data.db")
    cursor = connect.cursor()
    cursor.execute('''UPDATE train SET done = 0''')
    cursor.execute('''UPDATE learn SET remember = 0''')
    connect.commit()
    connect.close()
    text = '''данные о действиях сброшены'''
    bot.send_message(message.from_user.id, text=text, reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(commands=['start'])
def start(message):
    if message.text == '/start':
        keyboard = types.ReplyKeyboardMarkup()
        button_1 = types.KeyboardButton(text="/learn_words")
        keyboard.add(button_1)
        button_2 = types.KeyboardButton(text="/train_words")
        keyboard.add(button_2)
        question = "Привет, выбери тип задания"
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, 'Напиши /start')


# @bot.message_handler(content_types=['text'])



def rand_zero_2():
    global word_list
    f = True
    for i in word_list:
        if i[6] == 0:
            f = False
    if f:
        print("Everything is already learned")
        return 0
    ri = randint(0, len(word_list) - 1)
    while word_list[ri][6] != 0:
        ri = randint(0, len(word_list) - 1)
    return ri

right_ans = []
wrong_ans = []

@bot.message_handler(commands=['train_words'])
def dialogue_train_setting(message):
    global word_list, index, right_ans, wrong_ans
    word_list, index = [], 0
    connect = sqlite3.connect("data.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM train")
    word_list = cursor.fetchall()
    connect.close()
    index = rand_zero_2()
    i = word_list[index]
    ans1, ans2, ans3, ans4 = "/ans1", "/ans2", "/ans3", "/ans4"
    right_ans = i[5]
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text=ans1)
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text=ans2)
    keyboard.add(button_2)
    button_3 = types.KeyboardButton(text=ans3)
    keyboard.add(button_3)
    button_4 = types.KeyboardButton(text=ans4)
    keyboard.add(button_4)
    button_5 = types.KeyboardButton(text="/quit")
    keyboard.add(button_5)
    txt = i[0] + '\n' + "ans1: " + str(i[1]) + '\n' + "ans2: " + str(i[2]) + '\n' + "ans3: " + str(i[3]) + '\n' + "ans4: " + str(i[4])
    bot.send_message(message.chat.id, text=txt, reply_markup=keyboard)


@bot.message_handler(commands=['ans1'])
def func(message: types.Message):
    global word_list, index
    if right_ans == 'ans1':
        bot.send_message(message.chat.id, text=text_right)
        txt = word_list[index][0]
        connect = sqlite3.connect("data.db")
        cursor = connect.cursor()
        cursor.execute('''UPDATE train SET done = 1 WHERE task = ?''', (txt,))
        connect.commit()
        connect.close()
        dialogue_train_setting(message)
    else:
        bot.send_message(message.chat.id, text=text_wrong)
        dialogue_train_setting(message)


@bot.message_handler(commands=['ans2'])
def func(message: types.Message):
    global word_list, index
    if right_ans == 'ans2':
        bot.send_message(message.chat.id, text=text_right)
        txt = word_list[index][0]
        connect = sqlite3.connect("data.db")
        cursor = connect.cursor()
        cursor.execute('''UPDATE train SET done = 1 WHERE task = ?''', (txt,))
        connect.commit()
        connect.close()
        dialogue_train_setting(message)
    else:
        bot.send_message(message.chat.id, text=text_wrong)
        dialogue_train_setting(message)

@bot.message_handler(commands=['ans3'])
def func(message: types.Message):
    global word_list, index
    if right_ans == 'ans3':
        bot.send_message(message.chat.id, text=text_right)
        txt = word_list[index][0]
        connect = sqlite3.connect("data.db")
        cursor = connect.cursor()
        cursor.execute('''UPDATE train SET done = 1 WHERE task = ?''', (txt,))
        connect.commit()
        connect.close()
        dialogue_train_setting(message)
    else:
        bot.send_message(message.chat.id, text=text_wrong)
        dialogue_train_setting(message)


@bot.message_handler(commands=['ans4'])
def func(message: types.Message):
    global word_list, index
    if right_ans == 'ans4':
        bot.send_message(message.chat.id, text=text_right)
        txt = word_list[index][0]
        connect = sqlite3.connect("data.db")
        cursor = connect.cursor()
        cursor.execute('''UPDATE train SET done = 1 WHERE task = ?''', (txt,))
        connect.commit()
        connect.close()
        dialogue_train_setting(message)
    else:
        bot.send_message(message.chat.id, text=text_wrong)
        dialogue_train_setting(message)



@bot.message_handler(commands=['quit'])
def quit(message: types.Message):
    bot.send_message(message.chat.id, text="Бот завершил работу, для возобновления наберите /start",
                     reply_markup=types.ReplyKeyboardRemove())






word_list = []
index = 0


def rand_zero():
    global word_list
    f = True
    for i in word_list:
        if i[2] == 0:
            f = False
    if f:
        print("Everything is already learned")
        return 0
    ri = randint(0, len(word_list) - 1)
    while word_list[ri][2] != 0:
        ri = randint(0, len(word_list) - 1)
    return ri


@bot.message_handler(commands=['learn_words'])
def dialogue_learn_setting(message):
    global word_list, index
    connect = sqlite3.connect("data.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM learn")
    word_list = cursor.fetchall()
    connect.close()
    index = rand_zero()
    i = word_list[index]
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="/know")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="/do_not_know")
    keyboard.add(button_2)
    button_3 = types.KeyboardButton(text="/quit")
    keyboard.add(button_3)
    txt = i[0] + " - " + i[1]
    bot.send_message(message.chat.id, text=txt, reply_markup=keyboard)


@bot.message_handler(commands=['know'])
def know(message: types.Message):
    global word_list, index
    bot.send_message(message.chat.id, text=text_right)
    eng_word = word_list[index][0]
    connect = sqlite3.connect("data.db")
    cursor = connect.cursor()
    cursor.execute('''UPDATE learn SET remember = 1 WHERE eng_word = ?''', (eng_word,))
    connect.commit()
    connect.close()
    dialogue_learn_setting(message)


@bot.message_handler(commands=['do_not_know'])
def do_not_know(message: types.Message):
    bot.send_message(message.chat.id, text=text_wrong)
    dialogue_learn_setting(message)


@bot.message_handler(commands=['quit'])
def quit(message: types.Message):
    bot.send_message(message.chat.id, text="Бот завершил работу, для возобновления наберите /start",
                     reply_markup=types.ReplyKeyboardRemove())




bot.polling(none_stop=True, interval=0)
