from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.callback_data import themes_callback
from keyboards.inline.konspekts import *


from aiogram.types import CallbackQuery

from loader import dp,bot

@dp.callback_query_handler(themes_callback.filter(item_name = 'okrujnost_krug'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDeGRJWUWhOw5DtiAwnWEHCg5VZIrsAAKnLwACQdJJSutEgS_vYMyFLwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=okrujnost_krug)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'ploshad'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDfGRJWXsXBMl6RN3DtyibwuQREjOMAAKpLwACQdJJSg2GVAtYKlF5LwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=mnogougol_okrujnost)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'okrujnost_treugolnik'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDfmRJWa7ILLbbzLGD1xwwpP1k8MQbAAKsLwACQdJJSkQuNrXbW9fTLwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=vektori)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'okrujnost_chugolnik'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDgGRJWfxXY78aBlppbTgDSl8Vtdf2AAKxLwACQdJJStHY9pRywkLgLwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=mnogogranniki)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'sistema_koordinat'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDgmRJWiiffhN7S1F4geGrhbY9YoACAAKzLwACQdJJSoy-FH2itKCrLwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=prizma)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'prizma'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDhGRJWkuGhOIVmqtGJrLkpinPjszhAAK1LwACQdJJSuKEzakzMa5ELwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=trapetsiya)
    await call.message.delete()

# @dp.callback_query_handler(themes_callback.filter(item_name = 'paralepiped'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('В процессе скоро все дополним ...')
#     # await call.message.answer('Выберите что вам нужно', reply_markup=paralepiped)
#     await call.message.delete()

# @dp.callback_query_handler(themes_callback.filter(item_name = 'kub'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('В процессе скоро все дополним ...')
#     # await call.message.answer('Выберите что вам нужно', reply_markup=kub)
#     await call.message.delete()
