from audioop import add
from cgitb import text
from gc import callbacks
from unicodedata import category
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# class_5 = InlineKeyboardButton(text = '5 класс', callback_data = 'class')
# class_6 = InlineKeyboardButton(text = '6 класс', callback_data = 'class')
# class_7 = InlineKeyboardButton(text = '7 класс', callback_data = 'class')
# class_8 = InlineKeyboardButton(text = '8 класс', callback_data = 'class')
# class_9 = InlineKeyboardButton(text = '9 класс', callback_data = 'class')
# class_10 = InlineKeyboardButton(text = '10 класс', callback_data = 'class')
# class_11 = InlineKeyboardButton(text = '11 класс', callback_data = 'class')

# category_type = InlineKeyboardMarkup().add(class_5,class_6,class_7,class_8,class_9,class_10,class_11)

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

