from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.callback_data import themes_callback
from keyboards.inline.konspekts import *


from aiogram.types import CallbackQuery

from loader import dp,bot

@dp.callback_query_handler(themes_callback.filter(item_name = 'piramida'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDiGRJWpvJv3ga-Soy055yfgNWlVcpAAK8LwACQdJJSoVoyo7K8VBTLwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=piramida)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'silindr'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDimRJWrtG40wX_0NBTlKtLCwk9-gGAALALwACQdJJSvlIPAIotiAULwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=silindr)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'konus'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDjGRJWtroqYvFW9WnIZZocS3EGSxpAALFLwACQdJJSoHb4pM-pcxgLwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=konus)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'shar_sfera'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDjmRJWvz46Wbbr4sVbgk97F29-OIPAALGLwACQdJJSsdRkI-NScCJLwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=shar_sfera)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'kombinasiya'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document="BQACAgIAAxkBAAJDkGRJWyRn_-lJfND8dUM8PzfmHyxmAALILwACQdJJSh6Yse2bFF-7LwQ")
    # await call.message.answer('Выберите что вам нужно', reply_markup=prizma_shar)
    await call.message.delete()

# @dp.callback_query_handler(themes_callback.filter(item_name = 'piramida_shar'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('В процессе скоро все дополним ...')
#     # await call.message.answer('Выберите что вам нужно', reply_markup=piramida_shar)
#     await call.message.delete()

# @dp.callback_query_handler(themes_callback.filter(item_name = 'silindr_shar'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('В процессе скоро все дополним ...')
#     # await call.message.answer('Выберите что вам нужно', reply_markup=silindr_shar)
#     await call.message.delete()

# @dp.callback_query_handler(themes_callback.filter(item_name = 'konus_shar'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('В процессе скоро все дополним ...')
#     # await call.message.answer('Выберите что вам нужно', reply_markup=konus_shar)
#     await call.message.delete()
