from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

dtm_language  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🇷🇺 Русский язык'),
            KeyboardButton(text='🇺🇿 Узбекский язык')
        ],
        [
            KeyboardButton(text='➡️')
        ]
    ], 
resize_keyboard=True
)

dtm_years  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='2019'),
            KeyboardButton(text='2020'),
            KeyboardButton(text='2022')
        ],
        [
            KeyboardButton(text='➡️')
        ]
    ], 
resize_keyboard=True
)