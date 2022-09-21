from cgitb import text
import logging
from xml.dom.minidom import Document
from aiogram.dispatcher.filters import Command, Text
# from aiogram.types import URLInputFile
from aiogram.types import Message

from aiogram.types import CallbackQuery
from data.config import SBORNIK, SHARIGINA, SKANAVI, TRENAJOR, USMONOV, SCHOOL_BOOKS, MEDIC

from loader import dp
from loader import bot

@dp.message_handler(text='📑 Сканави')
async def send_book(message: Message):    
    for book in SKANAVI:
        await message.reply_document(document = book)

@dp.message_handler(text='👨 Усмонов')
async def send_book(message: Message):
    for book in USMONOV:
        await message.reply_document(document = book)

@dp.message_handler(text='Школьные книги 🏫')
async def send_book(message: Message):
    for book in SCHOOL_BOOKS:
        await message.reply_document(document = book)

@dp.message_handler(text='🇷🇺 Книга Шарыгина')
async def send_book(message: Message):
    for book in SHARIGINA:
        await message.reply_document(document = book)

@dp.message_handler(text='🏅 Алгебраический тренажёр')
async def send_book(message: Message):
    for book in TRENAJOR:
        await message.reply_document(document = book)

@dp.message_handler(text='📖 Сборник')
async def send_book(message: Message):
    for book in SBORNIK:
        await message.reply_document(document = book)

@dp.message_handler(text='🎩 М.М.Медицинский')
async def send_book(message: Message):
    for book in MEDIC:
        await message.reply_document(document = book)