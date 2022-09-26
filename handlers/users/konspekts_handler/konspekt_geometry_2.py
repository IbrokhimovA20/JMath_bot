from cgitb import text
from email import message
import logging
from os import link
import types
from xml.dom.minidom import Document
from aiogram import Bot
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.callback_data import lesson_callback
from keyboards.inline.konspekts import *
from keyboards.inline.themes import geometriya_themes_2
from loader import bot

from aiogram.types import CallbackQuery

from loader import dp

registered_users = [1521296013,296979322]

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_chetirohugolnik'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_parallelogram'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/konspekts_handler/konspekts/Параллелограмм и его площадь.pdf', 'rb'))
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_romb'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_pryamougolnik'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_kvadrat'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_okrujnost_krug'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_sektor_segment'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_urav_okrujnosti'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_treugol_okrujnost'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    await call.message.delete()

@dp.callback_query_handler(text='nazad_geometry_2')
async def buying_corse(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup = geometriya_themes_2)
    await call.message.delete()