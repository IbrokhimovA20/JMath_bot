from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.callback_data import years_callback
from handlers.users.all_books_programms import GUBKIN_BOOKS

from aiogram.types import CallbackQuery

from loader import dp
from loader import bot

@dp.callback_query_handler(years_callback.filter(item_name = 'gubkina_2017'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.reply_document(document=GUBKIN_BOOKS[2])
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'gubkina_2018'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.reply_document(document=GUBKIN_BOOKS[1])
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'gubkina_2019'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.reply_document(document=GUBKIN_BOOKS[0])
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'gubkina_2021'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.reply_document(document=GUBKIN_BOOKS[3])
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'gubkina_2022'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    for book in GUBKIN_BOOKS[4:]:
        await call.message.reply_document(document=book)
    await call.message.delete()