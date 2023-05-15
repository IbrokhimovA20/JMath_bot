from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

univers_2  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Amity'),
            KeyboardButton(text='BMU')
        ],
        [
            KeyboardButton(text='Акфа'),
            KeyboardButton(text='Турин')
        ]
        [
         KeyboardButton(text='⬅️'),   
        ]
    ], 
resize_keyboard=True

)