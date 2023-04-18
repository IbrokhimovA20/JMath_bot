from cgitb import text
import logging
from xml.dom.minidom import Document
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from .all_books import *

from keyboards.inline.classes import category_classes
from keyboards.default.library import math_books,olimpiada_books

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

@dp.message_handler(text='🎒 Школьный учебники')
async def send_book(message: Message):
    await message.answer("Выберите класс: ", reply_markup = category_classes)

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

@dp.message_handler(text='ЕГЭ')
async def send_book(message: Message):
    for book in EGE:
        await message.reply_document(document = book)

@dp.message_handler(text='ОГЭ')
async def send_book(message: Message):
    for book in OGE:
        await message.reply_document(document = book)

@dp.message_handler(text='📝 SAT/GMAT/GRE')
async def send_book(message: Message):
    await message.answer("Выберите то что вам нужно: ", reply_markup=math_books)

@dp.message_handler(text='SAT')
async def send_book(message: Message):
    for book in SAT_BOOKS:
        await message.reply_document(document = book)

@dp.message_handler(text='GMAT')
async def send_book(message: Message):
    for book in GMAT_BOOKS:
        await message.reply_document(document = book)

@dp.message_handler(text='GRE')
async def send_book(message: Message):
    for book in GRE_BOOKS:
        await message.reply_document(document = book)

@dp.message_handler(text='🔖 Олимпиада')
async def send_book(message: Message):
    await message.answer("Выберите нужный вам язык: ", reply_markup=olimpiada_books)

@dp.message_handler(text='Узбекский 🇺🇿')
async def send_book(message: Message):
    for book in olimpiada_books_uzb:
        await message.reply_document(document = book)

@dp.message_handler(text='Русский 🇷🇺')
async def send_book(message: Message):
    for book in olimpiada_books_rus:
        await message.reply_document(document = book)