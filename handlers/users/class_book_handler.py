
from aiogram.types import CallbackQuery
from .all_books_programms import *

from loader import dp, bot


@dp.callback_query_handler(text='1_book')
async def buy_courses(call: CallbackQuery):
    for book in class_1:
        await call.message.reply_document(document = book)
    await call.message.delete()

@dp.callback_query_handler(text='2_book')
async def buy_courses(call: CallbackQuery):
    for book in class_2:
        await call.message.reply_document(document = book)
    await call.message.delete()

@dp.callback_query_handler(text='3_book')
async def buy_courses(call: CallbackQuery):
    for book in class_3:
        await call.message.reply_document(document = book)
    await call.message.delete()

@dp.callback_query_handler(text='4_book')
async def buy_courses(call: CallbackQuery):
    for book in class_4:
        await call.message.reply_document(document = book)
    await call.message.delete()

@dp.callback_query_handler(text='5_book')
async def buy_courses(call: CallbackQuery):
    for book in class_5:
        await call.message.reply_document(document = book)
    await call.message.delete()

@dp.callback_query_handler(text='6_book')
async def buy_courses(call: CallbackQuery):
    for book in class_6:
        await call.message.reply_document(document = book)
    await call.message.delete()

@dp.callback_query_handler(text='7_book')
async def buy_courses(call: CallbackQuery):
    for book in class_7:
        await call.message.reply_document(document = book)
    await call.message.delete()

@dp.callback_query_handler(text='8_book')
async def buy_courses(call: CallbackQuery):
    for book in class_8:
        await call.message.reply_document(document = book)
    await call.message.delete()

@dp.callback_query_handler(text='9_book')
async def buy_courses(call: CallbackQuery):
    for book in class_9:
        await call.message.reply_document(document = book)
    await call.message.delete()

@dp.callback_query_handler(text='10_book')
async def buy_courses(call: CallbackQuery):
    for book in class_10:
        await call.message.reply_document(document = book)
    await call.message.delete()

@dp.callback_query_handler(text='11_book')
async def buy_courses(call: CallbackQuery):
    for book in class_11:
        await call.message.reply_document(document = book)
    await call.message.delete()