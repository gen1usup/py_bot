import time

import telebot
from telebot import types
 
bot = telebot.TeleBot('5131105468:AAFuIyda_LtJ5fHseUBoOY0Tfiu-aayAsN8')


@bot.message_handler(commands=["start"])
def start(message):
    # varib = f"Привет, <b>{message.from_user.first_name}</b>"
    varib = "Привет, <b>пупсик</b>"
    baton = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    baton_da = types.KeyboardButton("Конечно, давай!")
    baton.add(baton_da)
    bot.send_message(message.chat.id, varib, parse_mode='html')
    bot.send_message(message.chat.id, 'Хочешь прикол?', reply_markup=baton)


@bot.message_handler()
def prikol(message):
    video = open("prikol.mp4", "rb")

    if message.text == "Конечно, давай!":
        bot.send_message(message.chat.id, "Сейчас скину, жди :*")
        bot.send_video(message.chat.id, video)
        time.sleep(3)
        request_contact = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        rc_a = types.KeyboardButton("Ок", request_contact = True)
        rc_d = types.KeyboardButton("Не ок")
        request_contact.add(rc_a)
        request_contact.add(rc_d)
        bot.send_message(message.chat.id, 'Понравился прикол? Дай номерок', reply_markup=request_contact)
        # bot.send_message(message.chat.id, message)
        # bot.send_message(424324631, f"новый номер от {message.chat.first_name} {message.chat.last_name}")
    elif message.text.lower() == "привет":
        bot.send_message(424324631, f"новое сообщение от {message.chat.first_name} {message.chat.last_name}")


@bot.message_handler(content_types=['contact'])
def contact(message):
    bot.send_message(424324631, message.contact.phone_number)


bot.polling(none_stop=True)
