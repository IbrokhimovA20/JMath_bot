from audioop import add
from cgitb import text
from gc import callbacks
from unicodedata import category
from unittest.mock import call
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import follow_callback

follow_inline_button = InlineKeyboardMarkup(row_width=1)
follow_inline_button.insert(InlineKeyboardButton(text='Подписаться↗️', url='https://t.me/J_M_ath'))
follow_inline_button.insert(InlineKeyboardButton(text='Подписался/ась🟢', callback_data=follow_callback.new(item_name='followed')))
