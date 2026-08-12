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
        InlineKeyboardButton(text='Арифметика', callback_data='5_6_class'),
        InlineKeyboardButton(text='Алгебра', callback_data='7_8_class'),
    ],
    [
        InlineKeyboardButton(text='Тригонометрия', callback_data='9_class'),
        InlineKeyboardButton(text='Алгебра и начала анализа', callback_data='10_class')
    ],
    [
        InlineKeyboardButton(text='Дополнительные темы', callback_data='11_class')
    ],
    [
        InlineKeyboardButton(text='Алгебра с 0 1.1', url='https://t.me/+7FNDp39bWk4xMjE6'),
        InlineKeyboardButton(text='Алгебра с 0 1.2', url='https://t.me/+8ZEFcitGxRU4MjZi'),
    ],
    [
        InlineKeyboardButton(text='Алгебра с 0 1.3', url='https://t.me/+JFU8NJbwgQMzMjI6'),
        InlineKeyboardButton(text='Алгебра с 0 1.4', url='https://t.me/+O102MBMPh5k0Mjdi'),
    ]
])

category_classes = InlineKeyboardMarkup(
inline_keyboard=[
    [
        InlineKeyboardButton(text='1 класс', callback_data='1_book'),
        InlineKeyboardButton(text='2 класс', callback_data='2_book'),
        InlineKeyboardButton(text='3 класс', callback_data='3_book'),
        InlineKeyboardButton(text='4 класс', callback_data='4_book'),
    ],
    [ 
        InlineKeyboardButton(text='5 класс', callback_data='5_book'),
        InlineKeyboardButton(text='6 класс', callback_data='6_book'),
        InlineKeyboardButton(text='7 класс', callback_data='7_book'),
    ],
    [
        InlineKeyboardButton(text='8 класс', callback_data='8_book'),
        InlineKeyboardButton(text='9 класс', callback_data='9_book'),
    ],
    [
        InlineKeyboardButton(text='10 класс', callback_data='10_book'),
        InlineKeyboardButton(text='11 класс', callback_data='11_book')
    ]
])

