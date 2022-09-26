from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.callback_data import themes_callback
from keyboards.inline.konspekts import *


from aiogram.types import CallbackQuery

from loader import dp

@dp.callback_query_handler(themes_callback.filter(item_name = 'piramida'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=piramida)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'silindr'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=silindr)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'konus'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=konus)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'shar_sfera'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=shar_sfera)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'prizma_shar'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=prizma_shar)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'piramida_shar'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=piramida_shar)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'silindr_shar'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=silindr_shar)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'konus_shar'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=konus_shar)
    await call.message.delete()
