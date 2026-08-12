from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

lyceum  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Лицей И.М. Губкина'),
            KeyboardButton(text='WIUT Lyceum exam samples')
        ],
        [
            KeyboardButton(text="International House (InterHouse)")
        ],
        [
            KeyboardButton(text="Лицейские варианты📄")
        ],
        [
            KeyboardButton(text="назад")
        ]
    ], 
resize_keyboard=True

)