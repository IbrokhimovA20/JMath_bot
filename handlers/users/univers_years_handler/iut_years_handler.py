from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.callback_data import years_callback
from handlers.users.all_books_programms import IUT_BOOKS

from aiogram.types import CallbackQuery

from loader import dp
from loader import bot

@dp.callback_query_handler(years_callback.filter(item_name = 'iut_2015'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    for book in IUT_BOOKS[6:12]:
        await call.message.reply_document(document=book)
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'iut_2016'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    for book in IUT_BOOKS[12:]:
        await call.message.reply_document(document=book)
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'iut_2019'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.reply_document(document=IUT_BOOKS[3])
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'iut_2020'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.reply_document(document=IUT_BOOKS[0])
    await call.message.delete()

# @dp.callback_query_handler(years_callback.filter(item_name = 'iut_2021'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('Жаха не скинул файлы🍌')
#     await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'iut_2022'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    for book in IUT_BOOKS[1:6]:
        await call.message.reply_document(document=book)
    await call.message.delete()