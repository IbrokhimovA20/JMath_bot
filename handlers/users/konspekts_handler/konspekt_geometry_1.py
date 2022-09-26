from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.callback_data import lesson_callback
from keyboards.inline.konspekts import *
from keyboards.inline.themes import geometriya_themes_1


from aiogram.types import CallbackQuery

from loader import dp

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_smej_vert_ugli'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_paralel_pramoy'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_treugolnik'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_vidi_treugolnikov'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_sin_kos_tan_cotan'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_teorema_sin_cos'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_biss_mediana_visota'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_ploshad_treugolnikov'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_podobiye_treugolnikov'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(text='nazad_geometry_1')
async def buying_corse(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup = geometriya_themes_1)
    await call.message.delete()