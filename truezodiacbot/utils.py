import os


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
