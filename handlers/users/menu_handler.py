from cgitb import text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from keyboards.default.main_keyboard import menu
from keyboards.default.library import library_books
from keyboards.inline.classes import category_type
from keyboards.inline.classes import category_subject
from keyboards.default.univers_1 import univers_1
from keyboards.inline.themes import themes_5
from keyboards.inline.themes import themes_6
from keyboards.inline.themes import themes_7
from keyboards.inline.themes import themes_8
from keyboards.inline.themes import themes_9
from keyboards.inline.themes import themes_10
from keyboards.inline.themes import themes_11
from keyboards.inline.themes import geometriya_themes_1
from keyboards.inline.themes import geometriya_themes_2
from keyboards.inline.themes import geometriya_themes_3
from keyboards.inline.themes import geometriya_themes_4
from keyboards.inline.callback_data import themes_callback
from keyboards.default.uzbek_books import uzb_books
from keyboards.default.russian_books import rus_books
from keyboards.inline.follow_button import follow_inline_button
from .all_books import CAMBRIDGE,LOGICAL

from aiogram.types import CallbackQuery
from data.config import ADMINS,USERS
from data.config import CHANNEL_ID_1, CHANNEL_ID_2

from loader import dp, bot

def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else: 
        return False

@dp.message_handler(content_types=['file'], chat_id = USERS)
async def see_what(message:Message):
    print(message)

@dp.message_handler(text='Логические задания🧠', chat_id = USERS)
async def send_logical(message: Message):
    if check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID_1, user_id = message.chat.id)) and check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID_2, user_id = message.chat.id)):
        for book in LOGICAL:
            await message.reply_document(document = book)
    else:
        await bot.send_message(chat_id = message.chat.id,text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот J.M.ath! для того чтобы пользоваться ботом подпишитесь на канал J.M.ath", reply_markup=follow_inline_button)
        await message.delete()

@dp.message_handler(content_types=ContentType.DOCUMENT, chat_id = ADMINS)
async def download(message: Message):
    doc_id = message.document.file_id
    await message.answer(f"ID {doc_id}")

@dp.message_handler(text='Библиотека📚', chat_id = USERS)
async def send_libray(message: Message):
    if check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID_1, user_id = message.chat.id)) and check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID_2, user_id = message.chat.id)):
        await message.answer("Choose", reply_markup=library_books)
    else:
        await bot.send_message(chat_id = message.chat.id,text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот J.M.ath! для того чтобы пользоваться ботом подпишитесь на канал J.M.ath", reply_markup=follow_inline_button)
        await message.delete()

@dp.message_handler(text='📓 Cambridge Assessment', chat_id = USERS)
async def send_libray(message: Message):
    for book in CAMBRIDGE:
        await message.reply_document(document = book)

@dp.message_handler(text='🇺🇿 Узбекские книги', chat_id = USERS)
async def send_logical(message: Message):
    await message.answer("Choose", reply_markup = uzb_books)

@dp.message_handler(text='🇷🇺 Российские книги', chat_id = USERS)
async def send_logical(message: Message):
    await message.answer("Choose", reply_markup = rus_books)

@dp.message_handler(text='назад')
async def send_lesson(message: Message):
    await message.answer("Choose",reply_markup=menu)

@dp.message_handler(text='Назад⬆️')
async def send_lesson(message: Message):
    await message.answer("Choose",reply_markup=menu)

@dp.message_handler(text='Назад ⬆️')
async def send_lesson(message: Message):
    await message.answer("Choose",reply_markup=library_books)

@dp.message_handler(text='Темы📝', chat_id = USERS)
async def select_class(message: Message):
    if check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID_1, user_id = message.chat.id)) and check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID_2, user_id = message.chat.id)):
        await message.answer('Выберите предмет: ', reply_markup = category_subject)
    else:
        await bot.send_message(chat_id = message.chat.id,text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот J.M.ath! для того чтобы пользоваться ботом подпишитесь на канал J.M.ath", reply_markup=follow_inline_button)
        await message.delete()

@dp.callback_query_handler(text='algebra', chat_id = USERS)
async def buy_courses(call: CallbackQuery):
    await call.message.answer('Выберите класс', reply_markup = category_type)
    await call.message.delete()
    await call.answer(cache_time=10)

@dp.callback_query_handler(text='geometry', chat_id = USERS)
async def buy_courses(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup = geometriya_themes_1)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name='next_1'))
async def buy_courses(call: CallbackQuery, callback_data : dict):
    await call.message.edit_reply_markup(reply_markup=geometriya_themes_2)

@dp.callback_query_handler(themes_callback.filter(item_name='next_2'))
async def buy_courses(call: CallbackQuery, callback_data: dict):
    await call.message.edit_reply_markup(reply_markup=geometriya_themes_3)

@dp.callback_query_handler(themes_callback.filter(item_name='next_3'))
async def buy_courses(call: CallbackQuery, callback_data: dict):
    await call.message.edit_reply_markup(reply_markup=geometriya_themes_4)

@dp.callback_query_handler(themes_callback.filter(item_name='prev_1'))
async def buy_courses(call: CallbackQuery, callback_data: dict):
    await call.message.edit_reply_markup(reply_markup=geometriya_themes_1)
    

@dp.callback_query_handler(themes_callback.filter(item_name='prev_2'))
async def buy_courses(call: CallbackQuery, callback_data: dict):
    await call.message.edit_reply_markup(reply_markup=geometriya_themes_2)

@dp.callback_query_handler(themes_callback.filter(item_name='prev_3'))
async def buy_courses(call: CallbackQuery, callback_data: dict):
    await call.message.edit_reply_markup(reply_markup=geometriya_themes_3)

@dp.callback_query_handler(text='5_class')
async def buy_courses(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup = themes_5)
    await call.message.delete()

@dp.callback_query_handler(text='6_class')
async def buy_courses(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup = themes_6)
    await call.message.delete()

@dp.callback_query_handler(text='7_class')
async def buy_courses(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup = themes_7)
    await call.message.delete()

@dp.callback_query_handler(text='8_class')
async def buy_courses(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup = themes_8)
    await call.message.delete()

@dp.callback_query_handler(text='9_class')
async def buy_courses(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup = themes_9)
    await call.message.delete()

@dp.callback_query_handler(text='10_class')
async def buy_courses(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup = themes_10)
    await call.message.delete()

@dp.callback_query_handler(text='11_class')
async def buy_courses(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup = themes_11)
    await call.message.delete()

@dp.callback_query_handler(text='nazad_v_klass')
async def buy_courses(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup = category_type)
    await call.message.delete()

@dp.callback_query_handler(text='nazad_years')
async def buy_courses(call: CallbackQuery):
    await call.message.answer('Выберите ВУЗ', reply_markup = univers_1)
    await call.message.delete()