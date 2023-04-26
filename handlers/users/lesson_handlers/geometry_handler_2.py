from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.callback_data import themes_callback
from keyboards.inline.konspekts import *


from aiogram.types import CallbackQuery

from loader import dp,bot

@dp.callback_query_handler(themes_callback.filter(item_name = 'ploshad_treugolnikov'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDbGRJV0u4QidAhmxekfsgu3sl9R8WAAJ5LwACQdJJSmFwO9w-VYIZLwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=ploshad_treugolnikov)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'podobiye_treugolnikov'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDbmRJV4EwqdmPTJ0kBsq07P9BpFwqAAJ9LwACQdJJSqO5m8ldtDPtLwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=podobiye_treugolnikov)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'kvadrat'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDcGRJV6sHUw915c7ceVk5je4empMuAAKALwACQdJJSlm8c5UfpDmrLwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=kvadrat)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'parallelogram'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDcmRJWLsIVpb6dsQQbQUa9PEbxwfgAAKWLwACQdJJShJ7THT728f4LwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=parallelogram)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'trapetsiya'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDdGRJWPTS6VrNGYtWqavxLVCJBhhqAAKdLwACQdJJSj9vddGveOt8LwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=trapetsiya)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'mnogougolnik'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDdmRJWRSoLAOytmTSqGoXJdJXkyoaAAKgLwACQdJJSsEbkX_6d_yFLwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=mnogougolnik)
    await call.message.delete()

# @dp.callback_query_handler(themes_callback.filter(item_name = 'sektor_segment'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('В процессе скоро все дополним ...')
#     # await call.message.answer('Выберите что вам нужно', reply_markup=sektor_segment)
#     await call.message.delete()

# @dp.callback_query_handler(themes_callback.filter(item_name = 'urav_okrujnosti'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('В процессе скоро все дополним ...')
#     # await call.message.answer('Выберите что вам нужно', reply_markup=urav_okrujnosti)
#     await call.message.delete()

# @dp.callback_query_handler(themes_callback.filter(item_name = 'treugol_okrujnost'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('В процессе скоро все дополним ...')
#     # await call.message.answer('Выберите что вам нужно', reply_markup=treugol_okrujnost)
    # await call.message.delete()
    