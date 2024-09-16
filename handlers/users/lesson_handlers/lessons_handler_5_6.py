from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.callback_data import themes_callback
from keyboards.inline.konspekts import *

from aiogram.types import CallbackQuery

from loader import dp

@dp.callback_query_handler(lambda call: 'theme' in call.data)
async def handle_themes(call: CallbackQuery):
    await call.message.answer('Выберите что вам нужно', reply_markup = await give_documents(call.data.split(':')[1][6:]))
    await call.message.delete()


@dp.callback_query_handler(themes_callback.filter(item_name = 'obiknovenniye_drobi'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    # await call.message.answer('В процессе скоро все дополним ...')
    await call.message.answer('Выберите что вам нужно', reply_markup=obiknovenniye_drobi)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'desyatichniye_drobi'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    # await call.message.answer('В процессе скоро все дополним ...')
    await call.message.answer('Выберите что вам нужно', reply_markup=desyatichniye_drobi)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'period_drobi'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    # await call.message.answer('В процессе скоро все дополним ...')
    await call.message.answer('Выберите что вам нужно', reply_markup=per_drobi)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'ratsion_chisla'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    # await call.message.answer('В процессе скоро все дополним ...')
    await call.message.answer('Выберите что вам нужно', reply_markup=ratsion_chisla)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'stepen_ratsion_chisel'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    # await call.message.answer('В процессе скоро все дополним ...')
    await call.message.answer('Выберите что вам нужно', reply_markup=stepen_rat_chisla)
    await call.message.delete()
