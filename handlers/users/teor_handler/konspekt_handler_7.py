from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.callback_data import lesson_callback
from keyboards.inline.konspekts import *
from keyboards.inline.themes import themes_7


from aiogram.types import CallbackQuery

from loader import dp

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_stepen'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_odnochlen'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_mnogochlen'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_razloj_mnojiteli'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_formula_umnoj'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_algebra_drobi'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_lin_uravneniya'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_sistema_lin_urav'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_lin_func'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(text='nazad_7')
async def buying_corse(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup = themes_7)
    await call.message.delete()