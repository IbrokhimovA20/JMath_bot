from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

univers_3  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='РЭУ им. Плеханова'),
            KeyboardButton(text='Губкина'),
            KeyboardButton(text='МГУ им. Ломоносова'),
            KeyboardButton(text='МИФИ'), 
        ],
        [
         KeyboardButton(text='⬅️'),   
        ]
    ], 
resize_keyboard=True

)