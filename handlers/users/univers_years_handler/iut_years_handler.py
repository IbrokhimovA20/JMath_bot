from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from telegram import CallbackQuery, ReplyMarkup
from keyboards.inline.callback_data import years_callback

from aiogram.types import CallbackQuery

from loader import dp
from loader import bot

@dp.callback_query_handler(years_callback.filter(item_name = 'iut_2019'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('Жаха не скинул файлы🍌')
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'iut_2020'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/inha/2020 IUT SOCIE_MATH_Sample_Problems.pdf', 'rb'))
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/inha/INHA_1(IT).pdf', 'rb'))
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/inha/INHA_2(IT).pdf', 'rb'))
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/inha/INHA_3(IT).pdf', 'rb'))
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/inha/INHA_4(IT).pdf', 'rb'))
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/inha/INHA_5(IT).pdf', 'rb'))
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/inha/INHA_6(LOGISTIKA).pdf', 'rb'))
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/inha/INHA_7(LOGISTIKA).pdf', 'rb'))
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'iut_2021'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('Жаха не скинул файлы🍌')
    await call.message.delete()

@dp.callback_query_handler(years_callback.filter(item_name = 'iut_2022'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/inha/2022-iut-sbl_math_sample_problems.pdf', 'rb'))
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/inha/2022-iut-socie_math_sample_problems-for-contract (1).pdf', 'rb'))
    await bot.send_document(chat_id=call.from_user.id, document=open('/Users/akhrorbek/test_go/python/JMath/handlers/users/inha/2022-iut-socie_math_sample_problems-for-contract.pdf', 'rb'))
    await call.message.delete()