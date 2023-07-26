from distutils.util import change_root
from itertools import count
import sqlite3
from xml.dom.domreg import registered
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import USERS,ADMINS,KEY,MAIN_SHEET_ID
from keyboards.default.main_keyboard import menu
from keyboards.inline.follow_button import follow_inline_button
from aiogram.types import Message
from keyboards.inline.callback_data import follow_callback
from aiogram.types import CallbackQuery
from data.config import CHANNEL_ID_1, CHANNEL_ID_2
from states.dtm_state import userState
from aiogram.dispatcher import FSMContext
import gspread as gd
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


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

def check_google_sheet(user_id):
    SCOPE = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(KEY, SCOPE)
    gc = gd.authorize(credentials)
    url = f"https://docs.google.com/spreadsheets/d/{MAIN_SHEET_ID}/export?format=csv"
    df = pd.read_csv(url, index_col=[0])
    print(df)
    print(df.columns)


@dp.message_handler(CommandStart(), chat_id = USERS, state='*')
async def bot_start(message: types.Message, state:FSMContext):
    check_google_sheet(message.chat.id)
    if check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID_1, user_id = message.chat.id)) and check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID_2, user_id = message.chat.id)):
        await bot.send_message(chat_id = message.chat.id, text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот J.M.ath! приятного пользования", reply_markup=menu)
        await message.delete()
        await state.reset_state()
    else:
        await message.answer(f"Здравствуйте уважаемый {message.from_user.full_name}, добро пожаловать на бот J.M.ath! для того чтобы пользоваться ботом подпишитесь на канал J.M.ath", reply_markup=follow_inline_button)
        await state.reset_state()

@dp.callback_query_handler(follow_callback.filter(item_name = 'followed'), chat_id = USERS)
async def chech_following(call: CallbackQuery, callback_data: dict):
    if check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID_1, user_id = call.from_user.id)) and check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID_2, user_id = call.from_user.id)):
        await bot.send_message(chat_id = call.from_user.id, text = f"Здравствуйте уважаемый {call.from_user.full_name}, добро пожаловать на бот J.M.ath! приятного пользования", reply_markup=menu)
        await call.message.delete()
    else:
        await bot.send_message(chat_id = call.from_user.id,text = f"Здравствуйте уважаемый {call.from_user.full_name}, добро пожаловать на бот J.M.ath! для того чтобы пользоваться ботом подпишитесь на канал J.M.ath", reply_markup=follow_inline_button)
        await call.message.delete()

@dp.message_handler(text='jmath', chat_id = ADMINS)
async def check_answers(message: Message):
    await bot.send_message(chat_id=message.from_user.id, text = "Введите текст который хотели бы отправить всем пользователям")
    await message.delete()
    await userState.message_state.set()


@dp.message_handler(state=userState.message_state, chat_id = ADMINS)
async def check_answers(message: Message, state:FSMContext):
    text = message.text
    for user in USERS:
        try:
            await bot.send_message(chat_id=int(user), text = text)
        except:
            continue
    await message.delete()
    await state.reset_state()

