from telebot import TeleBot

from .utils import get_env_vars


BOT_TOKEN, ADMIN_ID = get_env_vars()
bot = TeleBot(BOT_TOKEN)
bot.send_message(ADMIN_ID, "I'm running.")


@bot.message_handler(content_types=["text"])
def reply(incoming_msg):
    uid = incoming_msg.from_user.id
    text = incoming_msg.text

    bot.send_message(chat_id=uid, text=text)

