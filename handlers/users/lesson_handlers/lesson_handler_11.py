from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.callback_data import themes_callback
from keyboards.inline.konspekts import *


from aiogram.types import CallbackQuery

from loader import dp

@dp.callback_query_handler(themes_callback.filter(item_name = 'proizvodnaya'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=proizvodnaya)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'sloj_prozivodnaya'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=sloj_prozivodnaya)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'promejutki_vozrast_ekstremum'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=promejutki_vozrast_ekstremum)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'geometry_smisl_proizvod'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=geometry_smisl_proizvod)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'mehanicheskiy_smisl_proizvod'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=mehanicheskiy_smisl_proizvod)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'pervoobraznaya'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=pervoobraznaya)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'neopredelenniy_integral'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=neopredelenniy_integral)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'opred_integral_trapetsiya'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=opred_integral_trapetsiya)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'metod_zamena_peremenniye'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=metod_zamena_peremenniye)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'integ_po_chastyam'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=integ_po_chastyam)
    await call.message.delete()