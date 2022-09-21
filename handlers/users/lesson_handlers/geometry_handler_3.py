from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from telegram import CallbackQuery, ReplyMarkup
from keyboards.inline.callback_data import themes_callback
from keyboards.inline.konspekts import *


from aiogram.types import CallbackQuery

from loader import dp

@dp.callback_query_handler(themes_callback.filter(item_name = 'chetiryoh_okrujnost'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=chetiryoh_okrujnost)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'mnogougol_okrujnost'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=mnogougol_okrujnost)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'vektori'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=vektori)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'mnogogranniki'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=mnogogranniki)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'prizma'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=prizma)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'trapetsiya'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=trapetsiya)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'paralepiped'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=paralepiped)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'kub'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=kub)
    await call.message.delete()
