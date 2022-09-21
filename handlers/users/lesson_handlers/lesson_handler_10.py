from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from telegram import CallbackQuery, ReplyMarkup
from keyboards.inline.callback_data import themes_callback
from keyboards.inline.konspekts import *


from aiogram.types import CallbackQuery

from loader import dp

@dp.callback_query_handler(themes_callback.filter(item_name = 'pokaz_urav_neravenstva'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=pokaz_urav_neravenstva)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'pokaz_funksiya'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=pokaz_funksiya)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'log_preobrazovaniya'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=log_preobrazovaniya)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'log_urav_neravenstva'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=log_urav_neravenstva)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'log_funskiya'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=log_funskiya)
    await call.message.delete()