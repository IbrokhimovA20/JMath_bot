from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from telegram import CallbackQuery, ReplyMarkup
from keyboards.inline.callback_data import years_callback

from aiogram.types import CallbackQuery

from loader import dp
from loader import bot

@dp.callback_query_handler(years_callback.filter(item_name = 'amity_2019'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/amity/AMITY_Buisness.pdf', 'rb'))
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/amity/AMITY_Economics.pdf', 'rb'))
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'amity_2020'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/amity/AMITY_Engineering.pdf', 'rb'))
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/amity/AMITY_Foundation.pdf', 'rb'))
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'amity_2021'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/amity/AMITY_IT_1.pdf', 'rb'))
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/amity/AMITY_IT_2.pdf', 'rb'))
    await call.message.delete()