# 🔮 TrueZodiacBot

[![CodeFactor](https://www.codefactor.io/repository/github/artemermulin/truezodiacbot/badge)](https://www.codefactor.io/repository/github/artemermulin/truezodiacbot)

Телеграм бот, для получения гороскопа на каждый день.

**Попробовать: [@TrueZodiacbot](https://t.me/truezodiacbot)**

## Техническая информация

Все предсказания генерируются случайным образом из четырех блоков заранее составленных предложений. В каждом блоке по 13 предложений. Общее количество уникальных комбинаций предсказаний: **28 561**.  
Все совпадения с реальным миром случайны.

- Telegram API - [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- Сервер - [Flask](https://flask.palletsprojects.com/en/1.1.x/) на [Heroku](https://www.heroku.com/home)
- База данных - [SQLite3](https://docs.python.org/3/library/sqlite3.html)
- Способ получения сообщений - Webhook

Идея и текст предсказаний заимствован и дополнен из [статей](https://thecode.media/zodiac/) журнала **КОД**
