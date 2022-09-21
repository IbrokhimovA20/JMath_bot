import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from telegram import CallbackQuery, ReplyMarkup
from keyboards.inline.callback_data import years_callback

from aiogram.types import CallbackQuery

from loader import dp

@dp.callback_query_handler(years_callback.filter(item_name = 'bmu_l_2019'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('bmu_2019')
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'bmu_l_2020'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('bmu_2020')
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'bmu_l_2021'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('bmu_2021')
    await call.message.delete()