DROP TABLE IF EXISTS users;

CREATE TABLE users (
    "id" INTEGER NOT NULL UNIQUE,
    "is_bot" INTEGER,
    "first_name" TEXT,
    "last_name" TEXT,
    "username" TEXT NOT NULL UNIQUE,
    "language_code" TEXT,
    "is_premium" BOOLEAN,
    "last_update" TEXT,
    "last_horoscope_request" TEXT,
    "♈ Овен" INTEGER DEFAULT 0,
    "♌ Лев" INTEGER DEFAULT 0,
    "♐ Стрелец" INTEGER DEFAULT 0,
    "♉ Телец" INTEGER DEFAULT 0,
    "♍ Дева" INTEGER DEFAULT 0,
    "♑ Козерог" INTEGER DEFAULT 0,
    "♊ Близнецы" INTEGER DEFAULT 0,
    "♎ Весы" INTEGER DEFAULT 0,
    "♒ Водолей" INTEGER DEFAULT 0,
    "♋ Рак" INTEGER DEFAULT 0,
    "♏ Скорпион" INTEGER DEFAULT 0,
    "♓ Рыбы" INTEGER DEFAULT 0,
    "⛎ Змееносец" INTEGER DEFAULT 0
);
