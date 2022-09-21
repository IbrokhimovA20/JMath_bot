from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from telegram import CallbackQuery, ReplyMarkup
from keyboards.inline.callback_data import themes_callback
from keyboards.inline.konspekts import *


from aiogram.types import CallbackQuery

from loader import dp

@dp.callback_query_handler(themes_callback.filter(item_name = 'nod_nok'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=nod_nok)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'obiknovenniye_drobi'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=obiknovenniye_drobi)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'desyatichniye_drobi'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=desyatichniye_drobi)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'zadachi_na_dvijeniye'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=obiknovenniye_drobi)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'delimosti_chisel'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=desyatichniye_drobi)
    await call.message.delete()
