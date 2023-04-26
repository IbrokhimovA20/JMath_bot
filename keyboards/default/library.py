from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

library_books  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🇺🇿 Узбекские книги'),
            KeyboardButton(text='📖 Сборник'),
        ],
        [
            KeyboardButton(text='🇷🇺 Российские книги'),
            KeyboardButton(text='🏅 Алгебраический тренажёр')
        ],
        [
            KeyboardButton(text='📓 Cambridge Assessment')
        ],
        [
            KeyboardButton(text='📝 SAT/GMAT/GRE')
        ],
        [
            KeyboardButton(text='🔖 Олимпиада'),
            KeyboardButton(text='💾 программы')
        ],
        [
            KeyboardButton(text='Назад⬆️')
        ]
    ], 
resize_keyboard=True
)

math_books  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='SAT')
        ],
        [
            KeyboardButton(text='GMAT')
        ],
        [
            KeyboardButton(text='GRE')
        ],
        [
            KeyboardButton(text='Библиотека📚')
        ]
    ], 
resize_keyboard=True
)

olimpiada_books  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Узбекский 🇺🇿')
        ],
        [
            KeyboardButton(text='Русский 🇷🇺')
        ],
        [
            KeyboardButton(text='Английский 🇬🇧')
        ],
        [
            KeyboardButton(text='Библиотека📚')
        ]
    ], 
resize_keyboard=True
)

programs  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='IOS 🍏')
        ],
        [
            KeyboardButton(text='Android 📱')
        ],
        [
            KeyboardButton(text='Библиотека📚')
        ]
    ], 
resize_keyboard=True
)