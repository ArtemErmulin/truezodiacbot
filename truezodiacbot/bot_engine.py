from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup

from .utils import get_env_vars


BOT_TOKEN, ADMIN_ID = get_env_vars()
bot = TeleBot(BOT_TOKEN)
bot.send_message(ADMIN_ID, "I'm running.")


@bot.message_handler(commands=["start"])
def start_message(incoming_msg):
    uid = incoming_msg.from_user.id
    send_start_msg(uid)


@bot.message_handler(content_types=["text"])
def reply(incoming_msg):
    uid = incoming_msg.from_user.id
    command = incoming_msg.text

    if command == "Получить гороскоп":
        show_zodiacs(uid)

    elif command == "О проекте":
        send_about(uid)

    elif command == "Обновить":
        update_horoscope(uid)
    else:
        bot.send_message(chat_id=uid, text=command)


def send_start_msg(uid):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Получить гороскоп")
    keyboard.row("О проекте", "Обновить")
    start_msg = "start message"

    bot.send_message(
        chat_id=uid,
        text=start_msg,
        reply_markup=keyboard,
    )


def show_zodiacs(uid):
    text = "zodiacs"
    bot.send_message(chat_id=uid, text=text)


def send_about(uid):
    text = "about"
    bot.send_message(chat_id=uid, text=text)


def update_horoscope(uid):
    text = "update"
    bot.send_message(chat_id=uid, text=text)
