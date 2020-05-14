import json
import os
import random

from .utils import current_datetime


SOURCE = os.path.join(os.path.dirname(__file__), "predictions.json")

with open(SOURCE) as file:
    predictions = json.load(file)


def random_prediction(key):
    return random.choice(predictions[key])


def generate(zodiac):
    title = (
        f"<b>{zodiac} | {current_datetime()}</b>"
        "\n\n"
    )

    body = (
        random_prediction("first") + "\n\n" +
        random_prediction("second") +
        random_prediction("second_add") + "\n\n" +
        random_prediction("third") +
        ""
    )

    end = ""

    return title + body + end
