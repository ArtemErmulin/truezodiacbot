from datetime import datetime
import os
from pytz import timezone

from . import reply_msg


SHOWING_STRFTIME = "%H:%M %d.%m.%Y"
HOST_URL = "https://truezodiacbot.herokuapp.com/"
HOST_LOCAL_IP = "0.0.0.0"


def running_from_heroku():
    return "BOT_TOKEN" in list(os.environ.keys())


def get_env_vars():
    if running_from_heroku():
        BOT_TOKEN = os.environ.get("BOT_TOKEN")
        ADMIN_ID = os.environ.get("ADMIN_ID")
    else:
        with open("misk") as misk:
            BOT_TOKEN, ADMIN_ID, *_ = misk.read().split("\n")

    return BOT_TOKEN, ADMIN_ID


def current_datetime(strftime=SHOWING_STRFTIME, as_datetime=False):
    current = datetime.now().astimezone(timezone("Europe/Moscow"))

    return current if as_datetime else current.strftime(strftime)


def is_zodiac(text):
    return (
        len(text) >= reply_msg.min_zodiac_len and
        any([text.lower() in i.lower() for i in reply_msg.zodiacs])
    )
