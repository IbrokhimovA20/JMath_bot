from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Темы📝'),
            KeyboardButton(text='Тесты✅❌'),
            KeyboardButton(text='Логические задания🧠'),
        ],
        [KeyboardButton(text='Библиотека📚')
        ],
    ], 
resize_keyboard=True

)