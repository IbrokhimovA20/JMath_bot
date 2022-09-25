from audioop import add
from cgitb import text
from gc import callbacks
from unicodedata import category
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


category_subject = InlineKeyboardMarkup(
    inline_keyboard=[
        [ 
        InlineKeyboardButton(text='Алгебра', callback_data='algebra'),
        InlineKeyboardButton(text='Геометрия', callback_data='geometry'),
    ]
    ]
)
category_type = InlineKeyboardMarkup(
inline_keyboard=[
    [ 
        InlineKeyboardButton(text='5 класс', callback_data='5_class'),
        InlineKeyboardButton(text='6 класс', callback_data='6_class'),
        InlineKeyboardButton(text='7 класс', callback_data='7_class'),
    ],
    [
        InlineKeyboardButton(text='8 класс', callback_data='8_class'),
        InlineKeyboardButton(text='9 класс', callback_data='9_class'),
    ],
    [
        InlineKeyboardButton(text='10 класс', callback_data='10_class'),
        InlineKeyboardButton(text='11 класс', callback_data='11_class')
    ]
])

