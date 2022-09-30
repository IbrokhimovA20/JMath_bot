from distutils.util import change_root
from itertools import count
import sqlite3
from xml.dom.domreg import registered
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import USERS
from keyboards.default.main_keyboard import menu
from keyboards.inline.follow_button import follow_inline_button
from aiogram.types import Message
from keyboards.inline.callback_data import follow_callback
from aiogram.types import CallbackQuery
from data.config import CHANNEL_ID

from loader import dp, bot

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

def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else: 
        return False

@dp.message_handler(CommandStart(), chat_id = USERS)
async def bot_start(message: types.Message):
    await message.answer(f"Здравствуйте уважаемый {message.from_user.full_name}, добро пожаловать на бот J.M.ath! для того чтобы пользоваться ботом подпишитесь на канал J.M.ath", reply_markup=follow_inline_button)

@dp.callback_query_handler(follow_callback.filter(item_name = 'followed'), chat_id = USERS)
async def chech_following(call: CallbackQuery, callback_data: dict):
    if check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID, user_id = call.from_user.id)):
        await bot.send_message(chat_id = call.from_user.id, text = f"Здравствуйте уважаемый {call.from_user.full_name}, добро пожаловать на бот J.M.ath! приятного пользования", reply_markup=menu)
        await call.message.delete()
    else:
        await bot.send_message(chat_id = call.from_user.id,text = f"Здравствуйте уважаемый {call.from_user.full_name}, добро пожаловать на бот J.M.ath! для того чтобы пользоваться ботом подпишитесь на канал J.M.ath", reply_markup=follow_inline_button)
        await call.message.delete()



    
