from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from telegram import CallbackQuery, ReplyMarkup
from keyboards.inline.callback_data import lesson_callback
from keyboards.inline.konspekts import *


from aiogram.types import CallbackQuery

from loader import dp

@dp.callback_query_handler(lesson_callback.filter(item_name = 'test_piramida'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'test_silindr'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'test_konus'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'test_shar_sfera'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'test_prizma_shar'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'test_piramida_shar'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'test_silindr_shar'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'test_konus_shar'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()