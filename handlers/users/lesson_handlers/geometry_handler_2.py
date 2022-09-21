from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from telegram import CallbackQuery, ReplyMarkup
from keyboards.inline.callback_data import themes_callback
from keyboards.inline.konspekts import *


from aiogram.types import CallbackQuery

from loader import dp

@dp.callback_query_handler(themes_callback.filter(item_name = 'chetirohugolnik'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=chetirohugolnik)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'parallelogram'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('Выберите что вам нужно', reply_markup=parallelogram)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'romb'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=romb)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'pryamougolnik'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=pryamougolnik)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'kvadrat'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=kvadrat)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'okrujnost_krug'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=okrujnost_krug)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'sektor_segment'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=sektor_segment)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'urav_okrujnosti'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=urav_okrujnosti)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'treugol_okrujnost'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=treugol_okrujnost)
    await call.message.delete()
    