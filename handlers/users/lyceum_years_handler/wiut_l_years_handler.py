from cgitb import text
import imp
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from telegram import CallbackQuery
from data.config import WIUT_L_2015_BOOKS,WIUT_L_2018_BOOKS,WIUT_L_2019_BOOKS,WIUT_L_2021_BOOKS
from keyboards.inline.callback_data import years_callback

from aiogram.types import CallbackQuery

from loader import dp
from loader import bot

@dp.callback_query_handler(years_callback.filter(item_name = 'wiut_l_2015'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    for book in WIUT_L_2015_BOOKS:
        await bot.send_document(chat_id = call.from_user.id, document = book)
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'wiut_l_2018'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    for book in WIUT_L_2018_BOOKS:
        await bot.send_document(chat_id = call.from_user.id, document = book)
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'wiut_l_2019'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    for book in WIUT_L_2019_BOOKS:
        await bot.send_document(chat_id = call.from_user.id, document = book)
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'wiut_l_2021'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    for book in WIUT_L_2021_BOOKS:
        await bot.send_document(chat_id = call.from_user.id, document = book)
    await call.message.delete()