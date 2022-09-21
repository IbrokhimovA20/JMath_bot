from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

rus_books  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🇷🇺 Книга Шарыгина')
        ],
        [
            KeyboardButton(text='📑 Сканави'),
            KeyboardButton(text='🎩 М.М.Медицинский')
        ],
        [
            KeyboardButton(text='Назад ⬆️')
        ]
    ], 
resize_keyboard=True

)