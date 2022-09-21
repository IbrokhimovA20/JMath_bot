from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from telegram import CallbackQuery, ReplyMarkup
from keyboards.inline.callback_data import years_callback

from aiogram.types import CallbackQuery

from loader import dp
from loader import bot

@dp.callback_query_handler(years_callback.filter(item_name = 'gubkina_2017'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/gubkina/Математика-2017.pdf', 'rb'))
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'gubkina_2018'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/gubkina/Математика_2018.pdf', 'rb'))
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'gubkina_2019'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/gubkina/Губкин 2019.pdf', 'rb'))
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'gubkina_2020'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('🍌')
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'gubkina_2021'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('🍌')
    await call.message.delete()