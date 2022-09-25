from atexit import register
from cgitb import text
from re import U
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.main_keyboard import menu
from keyboards.default.univers_1 import univers_1
from keyboards.default.univers_2 import univers_2
from keyboards.default.univers_3 import univers_3
import sqlite3
from data.config import ADMINS


from loader import dp

conn = sqlite3.connect("userlar.db")
cursor = conn.cursor()
users = cursor.execute("SELECT * FROM 'users'")
registered_users = []
for user in users:
    registered_users.append(user[1])
    
@dp.message_handler(text='Тесты✅❌', chat_id=ADMINS)
async def send_tests(message: Message):
    await message.answer('Выберите ВУЗ', reply_markup=univers_1)

@dp.message_handler(text='назад')
async def send_lesson(message: Message):
    await message.answer("Choose",reply_markup=menu)

@dp.message_handler(text='➡️')
async def send_lesson(message: Message):
    await message.answer("Выберите ВУЗ",reply_markup=univers_2)

@dp.message_handler(text='⬅️')
async def send_lesson(message: Message):
    await message.answer("Выберите ВУЗ",reply_markup=univers_1)


@dp.message_handler(text='⬅️')
async def send_lesson(message: Message):
    await message.answer("Выберите ВУЗ",reply_markup=univers_1)

@dp.message_handler(text="Российские ВУЗы")
async def send_russian(message: Message):
    await message.answer("Выберите ВУЗ", reply_markup=univers_3)



