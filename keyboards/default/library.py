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
            KeyboardButton(text='Назад⬆️')
        ]
    ], 
resize_keyboard=True

)