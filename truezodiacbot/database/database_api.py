from datetime import datetime, timedelta
import os
import sqlite3

from ..utils import current_datetime
from ..reply_msg import zodiacs


DATABASE_STRFTIME = "%Y-%m-%d %H:%M:%S"
MIN_UPDATE_TIME = timedelta(minutes=1)
MIN_REQUEST_TIME_FREQUENCY = timedelta(hours=3)

SCHEMA_NAME = "schema.sql"
TABLE = "users"
DB_NAME = "users.sqlite3"
DB_FOLDER = os.path.dirname(__file__)

SCHEMA_PATH = os.path.join(DB_FOLDER, SCHEMA_NAME)
DB_PATH = os.path.join(DB_FOLDER, DB_NAME)


def _dict_factory(cursor, row):
    d = {}
    for i, col in enumerate(cursor.description):
        d[col[0]] = row[i]
    return d


def get_db():
    db = sqlite3.connect(database=DB_PATH)
    db.row_factory = _dict_factory

    check = """SELECT name FROM sqlite_master WHERE type="table" """
    if "users" not in [i["name"] for i in db.execute(check).fetchall()]:
        with open(SCHEMA_PATH) as file:
            db.executescript(file.read())

        db.commit()

    return db


def _insert(script, data=None):
    db = get_db()
    if data is None:
        db.execute(script)
    else:
        db.execute(script, data)

    db.commit()


def _get(db, script):
    return db.execute(script).fetchall()


def add_user(data):
    """
    Add new user into database.

    Parameters:
    -----------
    data : dict
        key - database column
        value - column value
    """
    data["is_bot"] = int(data["is_bot"])
    data["last_update"] = current_datetime(strftime=DATABASE_STRFTIME)
    data["last_horoscope_request"] = ""

    columns = list(data.keys())
    placeholders = ", ".join(["?" for _ in columns])
    values = [data[tag] for tag in columns]

    script = 'INSERT INTO users ({}) VALUES ({})'.format(', '.join(columns), placeholders)
    _insert(script, values)


def get_users():
    db = get_db()

    columns = get_columns()
    placeholders = ", ".join(["?" for _ in columns])
    script = f"SELECT * FROM {TABLE}"

    return _get(db, script)


def get_columns():
    db = get_db()
    script = f"PRAGMA table_info({TABLE})"

    return [i["name"] for i in db.execute(script).fetchall()]


def is_new_user(uid):
    users = get_users()

    return uid not in [i["id"] for i in users]


def user_zodiac_request(uid, zodiac):
    return [
        i[zodiac] for i in get_users() if i["id"] == uid
    ][0]


def user_update_time(uid, strftime=None):
    update_time = datetime.strptime(
        [i["last_update"] for i in get_users() if i["id"] == uid][0],
        DATABASE_STRFTIME,
    )

    if strftime is None:
        return update_time
    else:
        return update_time.strftime(strftime)


def user_request_time(uid):
    current = current_datetime(as_datetime=True).replace(tzinfo=None)
    request_time_str = [
        i["last_horoscope_request"] for i in get_users() if i["id"] == uid
    ][0]

    if request_time_str == "":
        request_time = None
    else:
        request_time = datetime.strptime(request_time_str, DATABASE_STRFTIME)

    return request_time


def need_update(uid):
    current = current_datetime(as_datetime=True).replace(tzinfo=None)
    update_time = user_update_time(uid)

    return current - update_time > MIN_UPDATE_TIME


def update_user_datetime(uid):
    script = (
        f'UPDATE users SET last_update = "{current_datetime(strftime=DATABASE_STRFTIME)}" '
        f'WHERE "id" = {uid}'
    )
    _insert(script)


def update_user_horoscope_request(uid, zodiac):
    script = (
        f'UPDATE users SET '
        f'last_horoscope_request = "{current_datetime(strftime=DATABASE_STRFTIME)}", '
        f'"{zodiac}" = 1 WHERE "id" = {uid}'
    )
    _insert(script)


def request_too_often(uid, zodiac):
    request_time = user_request_time(uid)
    if request_time is None:
        return False
    else:
        if user_zodiac_request(uid, zodiac) == 1:
            return request_time.day == current_datetime(as_datetime=True).day
        else:
            return False


def reset_user_requests(uid):
    script = (
        'UPDATE users SET {} '
        'WHERE "id" = {}'.format(", ".join([f'"{i}" = 0'for i in zodiacs]), str(uid))
    )
    _insert(script)
