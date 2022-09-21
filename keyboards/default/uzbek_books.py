from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

uzb_books  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👨 Усмонов'),
            KeyboardButton(text='Школьные книги 🏫')
        ],
        [
        KeyboardButton(text='Назад ⬆️')
        ]
    ],
resize_keyboard=True
)