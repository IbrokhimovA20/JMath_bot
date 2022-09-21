from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from telegram import CallbackQuery, ReplyMarkup
from keyboards.inline.callback_data import themes_callback
from keyboards.inline.konspekts import *

from aiogram.types import CallbackQuery

from loader import dp

@dp.callback_query_handler(themes_callback.filter(item_name = 'kvadrad_korni'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=kvadrad_korni)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'kvadrad_uravneniya'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=kvadrad_uravneniya)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'nepolniye_kvadrad_uravneniya'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=nepolniye_kvadrad_uravneniya)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'teorema_vieta'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=teorema_vieta)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'urav_svod_kvadrad'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=urav_svod_kvadrad)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'lin_neravenstva'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=lin_neravenstva)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'sistema_lin_neravenstv'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=sistema_lin_neravenstv)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'metod_intervalov'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=metod_intervalov)
    await call.message.delete()
