from atexit import register
from cgitb import text
from re import U
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.main_keyboard import menu
from keyboards.default.univers_1 import univers_1
from keyboards.default.univers_3 import univers_3
import sqlite3
from data.config import USERS
from data.config import CHANNEL_ID_1, CHANNEL_ID_2
from keyboards.inline.follow_button import follow_inline_button

from loader import dp, bot

def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else: 
        return False
    
@dp.message_handler(text='Тесты✅❌', chat_id=USERS)
async def send_tests(message: Message):
    if check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID_1, user_id = message.chat.id)) and check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID_2, user_id = message.chat.id)):
        await message.answer('Выберите ВУЗ', reply_markup=univers_1)
    else:
        await bot.send_message(chat_id = message.chat.id,text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот J.M.ath! для того чтобы пользоваться ботом подпишитесь на канал J.M.ath", reply_markup=follow_inline_button)
        await message.delete()

@dp.message_handler(text='назад')
async def send_lesson(message: Message):
    await message.answer("Choose",reply_markup=menu)

@dp.message_handler(text='⬅️')
async def send_lesson(message: Message):
    await message.answer("Выберите ВУЗ",reply_markup=univers_1)


@dp.message_handler(text='⬅️')
async def send_lesson(message: Message):
    await message.answer("Выберите ВУЗ",reply_markup=univers_1)

@dp.message_handler(text="Российские ВУЗы")
async def send_russian(message: Message):
    await message.answer("Выберите ВУЗ", reply_markup=univers_3)