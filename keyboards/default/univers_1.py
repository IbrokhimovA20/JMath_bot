from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

univers_1  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='WIUT'),
            KeyboardButton(text='IUT'),
            KeyboardButton(text='Российские ВУЗы')
        ],
        [
            KeyboardButton(text='Национальные университеты')
        ],
        [
         KeyboardButton(text='назад'),
         KeyboardButton(text='➡️')   
        ]
    ], 
resize_keyboard=True

)