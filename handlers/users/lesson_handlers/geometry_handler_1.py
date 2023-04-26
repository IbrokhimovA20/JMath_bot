from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.callback_data import themes_callback
from keyboards.inline.konspekts import *


from aiogram.types import CallbackQuery

from loader import dp,bot

@dp.callback_query_handler(themes_callback.filter(item_name = 'ugli'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDRWRJVd6vgFO0KvYp2xASlxQHKtNAAAJlLwACQdJJSi2imPWIMGl5LwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=smej_vert_ugli)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'paralel_pramoy'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDXmRJVnBaoDB2werIt_I-mEQBVU2SAAJqLwACQdJJSo7x2ZNbmXNLLwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=paralel_pramoy)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'treugolnik'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDYGRJVph9XuATPdl2XxyV9xZ8YYjsAAJrLwACQdJJSqn0S9DYxATlLwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=treugolnik)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'vidi_treugolnikov'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDYmRJVr17OsoiFwNqysyBarzdphipAAJvLwACQdJJSk2cD_f__GbMLwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=vidi_treugolnikov)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'sin_kos_tan_cotan'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDZGRJVvTNXVTbd9XC_QZ2IQ3gBeYuAAJxLwACQdJJSolmmB6hQe-5LwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=sin_kos_tan_cotan)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'biss_mediana_visota'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDZmRJVxIlYCdU1nWfAti8LXG25o9KAAJ1LwACQdJJSqXOSHktjc-gLwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=biss_mediana_visota)
    await call.message.delete()

# @dp.callback_query_handler(themes_callback.filter(item_name = 'biss_mediana_visota'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('В процессе скоро все дополним ...')
#     # await call.message.answer('Выберите что вам нужно', reply_markup=biss_mediana_visota)
#     await call.message.delete()

# @dp.callback_query_handler(themes_callback.filter(item_name = 'ploshad_treugolnikov'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('В процессе скоро все дополним ...')
#     # await call.message.answer('Выберите что вам нужно', reply_markup=ploshad_treugolnikov)
#     await call.message.delete()

# @dp.callback_query_handler(themes_callback.filter(item_name = 'podobiye_treugolnikov'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('В процессе скоро все дополним ...')
#     # await call.message.answer('Выберите что вам нужно', reply_markup=podobiye_treugolnikov)
#     await call.message.delete()
