from cgitb import text
import imp
from re import U
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.years_univers import years_wiut,years_gubkina,years_iut
from keyboards.inline.years_lyceum import years_wiut_l
from keyboards.default.univers_keyboards.west_keyboard import west
from keyboards.default.univers_1 import univers_1
from keyboards.default.univers_2 import univers_2

from .all_books_programms import *
from states.dtm_state import StateDtm
from keyboards.default.dtm import *
from aiogram.dispatcher import FSMContext


from loader import dp
from loader import bot

@dp.message_handler(text='WIUT')
async def send_lesson(message: Message):
    await message.answer("Выберите год",reply_markup=years_wiut)

# @dp.message_handler(text='WIUT exam samples')
# async def send_lesson(message: Message):
#     await message.answer("Выберите год",reply_markup=years_wiut)

@dp.message_handler(text='WIUT Lyceum exam samples')
async def send_lesson(message: Message):
    await message.answer("Выберите год",reply_markup=years_wiut_l)

@dp.message_handler(text='IUT')
async def send_lesson(message: Message):
    await message.answer("Выберите год",reply_markup=years_iut)

@dp.message_handler(text='International House (InterHouse)')
async def send_lesson(message: Message):
    for book in INTERHOUSE_BOOKS:
        await message.reply_document(document = book)
    
@dp.message_handler(text='Лицей И.М. Губкина')
async def send_lesson(message: Message):
    for book in GUBKIN_LITSEY:
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
    for book in PLEHANOVA_BOOKS:
        await message.reply_document(document=book)

@dp.message_handler(text='Губкина')
async def send_lesson(message: Message):
    await bot.send_message(chat_id=message.from_user.id, text="Выберите год",reply_markup=years_gubkina)

@dp.message_handler(text='МГУ им. Ломоносова')
async def send_lesson(message: Message):
    for book in MGU_BOOKS:
        await message.reply_document(document = book)

@dp.message_handler(text='МИФИ')
async def send_lesson(message: Message):
    for book in MIFI_BOOKS:
        await message.reply_document(document = book)

@dp.message_handler(text='МГИМО')
async def send_lesson(message: Message):
    for book in MGIMO_BOOKS:
        await message.reply_document(document = book)

@dp.message_handler(text='Акфа')
async def send_lesson(message: Message):
    for book in AKFA_BOOKS:
        await message.reply_document(document = book)

@dp.message_handler(text='Турин')
async def send_lesson(message: Message):
    for book in TURIN_BOOKS:
        await message.reply_document(document = book)

@dp.message_handler(text='Национальные университеты')
async def send_lesson(message: Message):
    await message.answer("Выберите язык: ", reply_markup=dtm_language)
    await StateDtm.language.set()

@dp.message_handler(text='🇷🇺 Русский язык', state=StateDtm.language)
async def send_lesson(message: Message, state = FSMContext):
    await message.answer("Выберите год: ", reply_markup=dtm_years)
    await state.update_data(
        {"language" : message.text}
    )
    await StateDtm.year.set()


@dp.message_handler(text='🇺🇿 Узбекский язык', state=StateDtm.language)
async def send_lesson(message: Message, state = FSMContext):
    await message.answer("Выберите год: ", reply_markup=dtm_years)
    await state.update_data(
        {"language" : message.text}
    )
    await StateDtm.year.set()

@dp.message_handler(text='➡️', state=StateDtm.year)
async def send_lesson(message: Message, state = FSMContext):
    await message.answer("Выберите ВУЗ",reply_markup=univers_2)
    await state.reset_state()

@dp.message_handler(text='➡️', state=StateDtm.language)
async def send_lesson(message: Message, state = FSMContext):
    await message.answer("Выберите ВУЗ",reply_markup=univers_2)
    await state.reset_state()

@dp.message_handler(state=StateDtm.year)
async def send_book(message: Message, state = FSMContext):
    data = await state.get_data()
    language = data.get('language')
    if language == "🇷🇺 Русский язык":
        if message.text == "2019":
            for book in dtm_19_rus:
                await message.reply_document(document = book, reply_markup=univers_1)
        elif message.text == "2020":
            for book in dtm_20_rus:
                await message.reply_document(document = book, reply_markup=univers_1)
        elif message.text == "2022":
            for book in dtm_22_rus:
                await message.reply_document(document = book, reply_markup=univers_1)

    elif language == "🇺🇿 Узбекский язык":
        if message.text == "2019":
            for book in dtm_19_uzb:
                await message.reply_document(document = book, reply_markup=univers_1)
        elif message.text == "2020":
            for book in dtm_20_uzb:
                await message.reply_document(document = book, reply_markup=univers_1)
        elif message.text == "2022":
            for book in dtm_22_uzb:
                await message.reply_document(document = book, reply_markup=univers_1)
    await state.reset_state()

@dp.message_handler(text='➡️')
async def send_lesson(message: Message):
    await message.answer("Выберите ВУЗ",reply_markup=univers_2)

# @dp.message_handler(text='back')
# async def go_back_to_unis(message: Message):
#     await message.answer('Выберите ВУЗ', reply_markup=univers_1)