import os

from telebot.types import Update
from flask import Flask, request

from truezodiacbot import (
    HOST_LOCAL_IP,
    HOST_URL,
    running_from_heroku,
    bot,
    get_env_vars,
)

if running_from_heroku():
    BOT_TOKEN, _ = get_env_vars()
    server = Flask(__name__)

    @server.route("/" + BOT_TOKEN, methods=["POST"])
    def get_message():
        bot.process_new_updates([Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200

    @server.route("/")
    def set_webhook():
        bot.remove_webhook()
        bot.set_webhook(url=HOST_URL + BOT_TOKEN)
        return "Webhooks activated!", 200

    port = int(os.environ.get("PORT", 80))
    server.run(host=HOST_LOCAL_IP, port=port)

else:
    bot.remove_webhook()
    bot.polling(none_stop=True)
