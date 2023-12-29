from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.callback_data import lesson_callback
from keyboards.inline.konspekts import *


from aiogram.types import CallbackQuery

from loader import dp

@dp.callback_query_handler(lesson_callback.filter(item_name = 'prim_obiknovenniye_drobi'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.reply_document(document = "BQACAgIAAxkBAAKffmWOyMwsGoGjiuXZsAUCge0xN9yUAAKSOAACbbVpSJBbN1A_IDpdNAQ")
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'prim_desyatichniye_drobi'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.reply_document(document = "BQACAgIAAxkBAAKfgGWOySBAlnoI-2G5Z_9Cq1uwRTMPAAKVOAACbbVpSBNGwn14CVybNAQ")
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'prim_per_drobi'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.reply_document(document = "BQACAgIAAxkBAAKfgmWOyTPR32cmP6mWq1nOwZ8y-CaCAAKYOAACbbVpSKYiPc7t7SCfNAQ")
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'prim_ratsion_chisla'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.reply_document(document = "BQACAgIAAxkBAAKfhGWOyUoYVgABuSMHZmK3M_D6OL54AAOcOAACbbVpSGebTgnV8iACNAQ")
    await call.message.delete()

@dp.callback_query_handler(lesson_callback.filter(item_name = 'prim_stepen_rat_chisla'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.reply_document(document = "BQACAgIAAxkBAAKfhmWOyVmQD50d3bAjOq4aRn7hQ4dSAAKfOAACbbVpSNkjsgioxN-TNAQ")
    await call.message.delete()