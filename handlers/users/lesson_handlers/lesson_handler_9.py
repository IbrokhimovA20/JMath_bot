from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from telegram import CallbackQuery, ReplyMarkup
from keyboards.inline.callback_data import themes_callback
from keyboards.inline.konspekts import *

from aiogram.types import CallbackQuery

from loader import dp

@dp.callback_query_handler(themes_callback.filter(item_name = 'modul_uravneniya'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=modul_uravneniya)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'irrat_uravneniya_neravenstva'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=irrat_uravneniya_neravenstva)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'arif_progressiya'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=arif_progressiya)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'geometry_progressiya'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=geometry_progressiya)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'tekst_zadachi'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=tekst_zadachi)
    await call.message.delete()
