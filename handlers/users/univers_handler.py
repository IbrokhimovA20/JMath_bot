from cgitb import text
import imp
from re import U
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.years_univers import years_national
from keyboards.inline.years_univers import years_wiut
from keyboards.inline.years_lyceum import years_wiut_l
from keyboards.inline.years_univers import years_mifi
from keyboards.inline.years_univers import years_lomonosova
from keyboards.inline.years_univers import years_plehanova
from keyboards.inline.years_univers import years_gubkina
from keyboards.default.univers_keyboards.west_keyboard import west
from keyboards.default.univers_1 import univers_1
from data.config import AMITY_BOOKS, GUBKIN_BOOKS, IUT_BOOKS

from loader import dp
from loader import bot

@dp.message_handler(text='WIUT')
async def send_lesson(message: Message):
    await message.answer("Choose",reply_markup=west)

@dp.message_handler(text='WIUT exam samples')
async def send_lesson(message: Message):
    await message.answer("Выберите год",reply_markup=years_wiut)

@dp.message_handler(text='WIUT Lyceum exam samples')
async def send_lesson(message: Message):
    await message.answer("Выберите год",reply_markup=years_wiut_l)

@dp.message_handler(text='IUT')
async def send_lesson(message: Message):
    for book in IUT_BOOKS:
        await message.reply_document(document = book)

@dp.message_handler(text='Amity')
async def send_lesson(message: Message):
    for book in AMITY_BOOKS:
        await message.reply_document(document =book)

@dp.message_handler(text='BMU')
async def send_lesson(message: Message):
    await message.answer("В процессе скоро все дополним ...")

@dp.message_handler(text='РЭУ им. Плеханова')
async def send_lesson(message: Message):
    await message.answer("В процессе скоро все дополним ...")

@dp.message_handler(text='Губкина')
async def send_lesson(message: Message):
    for book in GUBKIN_BOOKS:
        await message.reply_document(document=book)

@dp.message_handler(text='МГУ им. Ломоносова')
async def send_lesson(message: Message):
    await message.answer("В процессе скоро все дополним ...")

@dp.message_handler(text='МИФИ')
async def send_lesson(message: Message):
    await message.answer("В процессе скоро все дополним ...")

@dp.message_handler(text='Национальные университеты')
async def send_lesson(message: Message):
    await message.answer("В процессе скоро все дополним ...")

@dp.message_handler(text='back')
async def go_back_to_unis(message: Message):
    await message.answer('Выберите ВУЗ', reply_markup=univers_1)