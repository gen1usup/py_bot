import time
import random
import telebot
from telebot import types
import requests


bot = telebot.TeleBot('5131105468:AAFuIyda_LtJ5fHseUBoOY0Tfiu-aayAsN8')
video_name = ["vechak.mp4", "prikol.mp4", "vremyaichak.mp4", "chakino.mp4", "guchak.mp4", "davaichak.mp4", "atrachik.mp4"]


@bot.message_handler(commands=["start"])
def start(message):
    varib = f"Привет, <b>{message.from_user.first_name}</b>"
    # varib = message.chat.first_name
    baton = types.ReplyKeyboardMarkup(resize_keyboard=True)
    baton_da = types.KeyboardButton("Хочу прикол")
    baton.add(baton_da)
    bot.send_message(message.chat.id, varib, parse_mode='html', reply_markup=baton)
    # bot.send_message(message.chat.id, 'Хочешь прикол?', reply_markup=baton)


@bot.message_handler()
def prikol(message):
    video = open(video_name[random.randint(1, len(video_name))], "rb")

    if message.text == "Хочу прикол":
        # bot.send_message(message.chat.id, "Сейчас будет")
        bot.send_video(message.chat.id, video)
        # -----запрос номера-------
        # time.sleep(3)
        # request_contact = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        # rc_a = types.KeyboardButton("Ок", request_contact=True)
        # rc_d = types.KeyboardButton("Не ок")
        # request_contact.add(rc_a)
        # request_contact.add(rc_d)
        # bot.send_message(message.chat.id, 'Понравился прикол? Дай номерок', reply_markup=request_contact)
        # bot.send_message(message.chat.id, message)
        # bot.send_message(424324631, f"новый номер от {message.chat.first_name} {message.chat.last_name}")
    #     ----------------
    elif message.text.lower() == "привет":
        bot.send_message(424324631, f"новое сообщение от {message.chat.first_name} {message.chat.last_name}")


@bot.message_handler(content_types=['contact'])
def contact(message):
    bot.send_message(424324631, message.contact.phone_number)


bot.polling(none_stop=True)
