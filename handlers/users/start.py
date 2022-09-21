from distutils.util import change_root
from itertools import count
import sqlite3
from xml.dom.domreg import registered
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from keyboards.default.main_keyboard import menu
# from aiogram.dispatcher import filters
from aiogram.types import Message
import sqlite3

from loader import dp, db, bot
# conn = sqlite3.connect("userlar.db")
# cursor = conn.cursor()
# users = cursor.execute("SELECT * FROM 'users'")
# registered_users = []
# for user in users:
#     registered_users.append(user[1])
@dp.message_handler(text_contains='id_add')
async def check_answers(message: Message):
    global registered_users
    conn = sqlite3.connect("userlar.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT OR IGNORE INTO 'users' ('user_id') VALUES (?)", (int(message.text.split(' ')[1]),))
    users = cursor.execute("SELECT * FROM 'users'")
    for user in users:
        if user[1] not in registered_users:
            registered_users.append(user[1])
    conn.commit()
    await message.answer('saved')

@dp.message_handler(CommandStart(), chat_id = ADMINS)
async def bot_start(message: types.Message):
    await message.answer(f"Здравствуйте уважаемый {message.from_user.full_name}, добро пожаловать на бот J.M.ath!", reply_markup=menu)
    
