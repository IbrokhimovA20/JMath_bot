from atexit import register
from cgitb import text
from re import U
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.main_keyboard import menu
from keyboards.default.univers_1 import univers_1
from keyboards.default.univers_3 import univers_3
from data.config import CHANNEL_ID_1
from keyboards.inline.follow_button import follow_inline_button
from handlers.users.start import check_google_sheet

from loader import dp, bot

def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else: 
        return False
    
@dp.message_handler(text='Университеты 🎓')
async def send_tests(message: Message):
    if check_google_sheet(message.chat.id):
        if check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID_1, user_id = message.chat.id)):
            await message.answer('Выберите ВУЗ', reply_markup=univers_1)
        else:
            await bot.send_message(chat_id = message.chat.id,text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот J.M.ath! для того чтобы пользоваться ботом подпишитесь на канал J.M.ath", reply_markup=follow_inline_button)
            await message.delete()

@dp.message_handler(text='назад')
async def send_lesson(message: Message):
    if check_google_sheet(message.chat.id):
        await message.answer("Choose",reply_markup=menu)

@dp.message_handler(text='⬅️')
async def send_lesson(message: Message):
    if check_google_sheet(message.chat.id):
        await message.answer("Выберите ВУЗ",reply_markup=univers_1)


@dp.message_handler(text='⬅️')
async def send_lesson(message: Message):
    if check_google_sheet(message.chat.id):
        await message.answer("Выберите ВУЗ",reply_markup=univers_1)

@dp.message_handler(text="Российские ВУЗы")
async def send_russian(message: Message):
    if check_google_sheet(message.chat.id):
        await message.answer("Выберите ВУЗ", reply_markup=univers_3)