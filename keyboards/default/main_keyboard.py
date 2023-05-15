from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Темы📝'),
            KeyboardButton(text='Университеты 🎓'),
            KeyboardButton(text='Логические задания🧠'),
        ],
        [
            KeyboardButton(text='Лайфхаки 💯'),
            KeyboardButton(text='Лицеи 🎒')
        ],
        [
            KeyboardButton(text='Библиотека📚')
        ]
    ], 
resize_keyboard=True

)