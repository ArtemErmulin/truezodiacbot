from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup

from .utils import get_env_vars, current_datetime, is_zodiac
from . import horoscope
from . import reply_msg


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

    elif command == "Назад":
        send_start_msg(uid)

    elif is_zodiac(command):
        zodiac = [i for i in reply_msg.zodiacs if command.lower() in i.lower()]
        send_horoscope(uid, zodiac[0])


def send_start_msg(uid, text=None):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Получить гороскоп")
    keyboard.row("О проекте", "Обновить")

    if text is None:
        start_msg = reply_msg.main_description.format(current_datetime())
    else:
        start_msg = text

    bot.send_message(
        chat_id=uid,
        text=start_msg,
        reply_markup=keyboard,
        parse_mode="html",
    )


def show_zodiacs(uid):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    for i in [0, 3, 6, 9]:  # grouped by it's element (3 in each)
        keyboard.row(*reply_msg.zodiacs[i : i + 3])

    keyboard.add(reply_msg.zodiacs[-1])  # + ophiuchus
    keyboard.add("Назад")

    text = "Для какого знака зодиака будем правду узнавать?"

    bot.send_message(uid, text, reply_markup=keyboard)


def send_about(uid):
    bot.send_message(
        chat_id=uid,
        text=reply_msg.about,
        parse_mode="html",
        disable_web_page_preview=True,
    )


def update_horoscope(uid):
    update_msg = (
        "Гороскоп обновлён!\n"
        "Данные актуальны на:\n<b>{}</b>.\n\n<i>{}</i>"
        "".format(current_datetime(), reply_msg.get_update_msg())
    )

    bot.send_message(
        chat_id=uid,
        text=update_msg,
        parse_mode="html",
    )


def send_horoscope(uid, zodiac):
    text = horoscope.generate(zodiac)

    # generate reply buttons like on '/start' command
    send_start_msg(uid, text=text)
