from cgitb import text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from aiogram.dispatcher.handler import SkipHandler
from keyboards.default.main_keyboard import menu
from keyboards.default.library import library_books
from keyboards.inline.classes import category_type
from keyboards.inline.classes import category_subject
from keyboards.default.univers_1 import univers_1
# from keyboards.inline.themes import themes_5_6
from keyboards.inline.themes import give_class_themes
# from keyboards.inline.themes import themes_7
# from keyboards.inline.themes import themes_8
# from keyboards.inline.themes import themes_9
# from keyboards.inline.themes import themes_10
# from keyboards.inline.themes import themes_11
from keyboards.inline.themes import geometriya_themes_1
from keyboards.inline.themes import geometriya_themes_2
from keyboards.inline.themes import geometriya_themes_3
from keyboards.inline.themes import geometriya_themes_4
from keyboards.inline.callback_data import themes_callback
from keyboards.default.uzbek_books import uzb_books
from keyboards.default.russian_books import rus_books
from keyboards.inline.follow_button import follow_inline_button
from keyboards.default.lyceums import lyceum
from states.dtm_state import userState
from aiogram.dispatcher import FSMContext
from .all_books_programms import CAMBRIDGE,LOGICAL

from aiogram.types import CallbackQuery
from data.config import ADMINS
from data.config import CHANNEL_ID_1
from handlers.users.start import check_google_sheet

from loader import dp, bot

def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else: 
        return False

@dp.message_handler(content_types=['file'], chat_id = ADMINS)
async def see_what(message:Message):
    print(message)

@dp.message_handler(content_types=ContentType.DOCUMENT, chat_id = ADMINS)
async def download(message: Message):
    doc_id = message.document.file_id
    await message.answer(f"ID {doc_id}")

@dp.message_handler(content_types=ContentType.TEXT, chat_id = ADMINS)
async def extract_links(message: Message):
    links = [f"{message.text[e.offset:e.offset + e.length]} -> {e.url}"
             for e in (message.entities or []) if e.type == 'text_link']
    if not links:
        raise SkipHandler()
    await message.answer('\n'.join(links))

@dp.message_handler(text='Логические задания🧠', state='*')
async def send_logical(message: Message, state:FSMContext):
    if check_google_sheet(message.chat.id):
        if check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID_1, user_id = message.chat.id)):
            for book in LOGICAL:
                await message.reply_document(document = book)
            await state.reset_state()
        else:
            await bot.send_message(chat_id = message.chat.id,text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот J.M.ath! для того чтобы пользоваться ботом подпишитесь на канал J.M.ath", reply_markup=follow_inline_button)
            await message.delete()
            await state.reset_state()

@dp.message_handler(text='Задать Вопрос❓', state="*")
async def send__question_to_group(message: Message):
    if check_google_sheet(message.chat.id):
        await bot.send_message(chat_id=message.chat.id, text="""Вы можете отправить свой вопрос ввиде текста,фото или видеосообщения если не хотите то нажмите 
/cancel""")
        # if check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID_1, user_id = message.chat.id)):
        # else:
        #     await bot.send_message(chat_id = message.chat.id,text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот J.M.ath! для того чтобы пользоваться ботом подпишитесь на канал J.M.ath", reply_markup=follow_inline_button)
        #     await message.delete()
        await userState.question_state.set()

@dp.message_handler(commands=['cancel'], state="*")
async def cancel_number(message: types.Message, state:FSMContext):
    await state.reset_state()



@dp.message_handler(text='Библиотека📚', state='*')
async def send_libray(message: Message, state:FSMContext):
    if check_google_sheet(message.chat.id):
        if check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID_1, user_id = message.chat.id)):
            await message.answer("Choose", reply_markup=library_books)
            await state.reset_state()
        else:
            await bot.send_message(chat_id = message.chat.id,text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот J.M.ath! для того чтобы пользоваться ботом подпишитесь на канал J.M.ath", reply_markup=follow_inline_button)
            await message.delete()
            await state.reset_state()

@dp.message_handler(text='📓 Cambridge Assessment', state='*')
async def send_libray(message: Message, state:FSMContext):
    if check_google_sheet(message.chat.id):
        for book in CAMBRIDGE:
            await message.reply_document(document = book)
        await state.reset_state()

@dp.message_handler(text='🇺🇿 Узбекские книги', state='*')
async def send_logical(message: Message, state:FSMContext):
    if check_google_sheet(message.chat.id):
        await message.answer("Choose", reply_markup = uzb_books)
        await state.reset_state()

@dp.message_handler(text='🇷🇺 Российские книги', state='*')
async def send_logical(message: Message, state:FSMContext):
    if check_google_sheet(message.chat.id):
        await message.answer("Choose", reply_markup = rus_books)
        await state.reset_state()

@dp.message_handler(text='назад', state='*')
async def send_lesson(message: Message, state:FSMContext):
    if check_google_sheet(message.chat.id):
        await message.answer("Choose",reply_markup=menu)
        await state.reset_state()
    

@dp.message_handler(text='Назад⬆️', state='*')
async def send_lesson(message: Message, state:FSMContext):
    if check_google_sheet(message.chat.id):
        await message.answer("Choose",reply_markup=menu)
        await state.reset_state()

@dp.message_handler(text='Назад ⬆️')
async def send_lesson(message: Message, state:FSMContext):
    if check_google_sheet(message.chat.id):
        await message.answer("Choose",reply_markup=library_books)
        await state.reset_state()

@dp.message_handler(text='Темы📝', state='*')
async def select_class(message: Message, state:FSMContext):
    if check_google_sheet(message.chat.id):
        if check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID_1, user_id = message.chat.id)):
            await message.answer('Выберите предмет: ', reply_markup = category_subject)
            await state.reset_state()
        else:
            await bot.send_message(chat_id = message.chat.id,text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот J.M.ath! для того чтобы пользоваться ботом подпишитесь на канал J.M.ath", reply_markup=follow_inline_button)
            await message.delete()
            await state.reset_state()

@dp.message_handler(text='Лайфхаки 💯', state='*')
async def select_class(message: Message, state:FSMContext):
    if check_google_sheet(message.chat.id):
        if check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID_1, user_id = message.chat.id)):
            await message.answer('А лайфхаки вы можете увидеть в нашем youtube канале  \n\n\n\n https://www.youtube.com/@jmath4124')
            await state.reset_state()
        else:
            await bot.send_message(chat_id = message.chat.id,text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот J.M.ath! для того чтобы пользоваться ботом подпишитесь на канал J.M.ath", reply_markup=follow_inline_button)
            await message.delete()
            await state.reset_state()

@dp.message_handler(text='Лицеи 🎒', state='*')
async def select_class(message: Message, state:FSMContext):
    if check_google_sheet(message.chat.id):
        if check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID_1, user_id = message.chat.id)):
            await message.answer('Выберите лицей: ', reply_markup = lyceum)
            await state.reset_state()
        else:
            await bot.send_message(chat_id = message.chat.id,text = f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот J.M.ath! для того чтобы пользоваться ботом подпишитесь на канал J.M.ath", reply_markup=follow_inline_button)
            await message.delete()
            await state.reset_state()

@dp.callback_query_handler(text='algebra', state='*')
async def buy_courses(call: CallbackQuery, state:FSMContext):
    if check_google_sheet(call.from_user.id):
        await call.message.answer('Выберите класс', reply_markup = category_type)
        await call.message.delete()
        await call.answer(cache_time=10)
        await state.reset_state()

@dp.callback_query_handler(text='geometry', state='*')
async def buy_courses(call: CallbackQuery, state:FSMContext):
    if check_google_sheet(call.from_user.id):
        await call.message.answer('Выберите тему', reply_markup = geometriya_themes_1)
        await call.message.delete()
        await state.reset_state()

@dp.callback_query_handler(themes_callback.filter(item_name='next_1'))
async def buy_courses(call: CallbackQuery, callback_data : dict):
    if check_google_sheet(call.from_user.id):
        await call.message.edit_reply_markup(reply_markup=geometriya_themes_2)

@dp.callback_query_handler(themes_callback.filter(item_name='next_2'))
async def buy_courses(call: CallbackQuery, callback_data: dict):
    if check_google_sheet(call.from_user.id):
        await call.message.edit_reply_markup(reply_markup=geometriya_themes_3)

@dp.callback_query_handler(themes_callback.filter(item_name='next_3'))
async def buy_courses(call: CallbackQuery, callback_data: dict):
    if check_google_sheet(call.from_user.id):
        await call.message.edit_reply_markup(reply_markup=geometriya_themes_4)

@dp.callback_query_handler(themes_callback.filter(item_name='prev_1'))
async def buy_courses(call: CallbackQuery, callback_data: dict):
    if check_google_sheet(call.from_user.id):
        await call.message.edit_reply_markup(reply_markup=geometriya_themes_1)
    

@dp.callback_query_handler(themes_callback.filter(item_name='prev_2'))
async def buy_courses(call: CallbackQuery, callback_data: dict):
    if check_google_sheet(call.from_user.id):
        await call.message.edit_reply_markup(reply_markup=geometriya_themes_2)

@dp.callback_query_handler(themes_callback.filter(item_name='prev_3'))
async def buy_courses(call: CallbackQuery, callback_data: dict):
    if check_google_sheet(call.from_user.id):

        await call.message.edit_reply_markup(reply_markup=geometriya_themes_3)

# @dp.callback_query_handler(text='5_6_class')
# async def buy_courses(call: CallbackQuery):
#     if check_google_sheet(call.from_user.id):
#         await call.message.answer('Выберите тему', reply_markup = themes_5_6)
#         await call.message.delete()


@dp.callback_query_handler(lambda call: 'class' in call.data)
async def give_algebra_classes(call : CallbackQuery):
    if check_google_sheet(call.from_user.id):
        await call.message.answer('Выберите тему', reply_markup = await give_class_themes(call.data))
        await call.message.delete()


# @dp.callback_query_handler(text='6_class')
# async def buy_courses(call: CallbackQuery):
#     if check_google_sheet(call.from_user.id):
#         await call.message.answer('Выберите тему', reply_markup = themes_6)
#         await call.message.delete()

# @dp.callback_query_handler(text='7_class')
# async def buy_courses(call: CallbackQuery):
#     if check_google_sheet(call.from_user.id):
#         await call.message.answer('Выберите тему', reply_markup = themes_7)
#         await call.message.delete()

# @dp.callback_query_handler(text='8_class')
# async def buy_courses(call: CallbackQuery):
#     if check_google_sheet(call.from_user.id):
#         await call.message.answer('Выберите тему', reply_markup = themes_8)
#         await call.message.delete()

# @dp.callback_query_handler(text='9_class')
# async def buy_courses(call: CallbackQuery):
#     if check_google_sheet(call.from_user.id):
#         await call.message.answer('Выберите тему', reply_markup = themes_9)
#         await call.message.delete()

# @dp.callback_query_handler(text='10_class')
# async def buy_courses(call: CallbackQuery):
#     if check_google_sheet(call.from_user.id):
#         await call.message.answer('Выберите тему', reply_markup = themes_10)
#         await call.message.delete()

# @dp.callback_query_handler(text='11_class')
# async def buy_courses(call: CallbackQuery):
#     if check_google_sheet(call.from_user.id):
#         await call.message.answer('Выберите тему', reply_markup = themes_11)
#         await call.message.delete()

@dp.callback_query_handler(text='nazad_v_klass')
async def buy_courses(call: CallbackQuery):
    if check_google_sheet(call.from_user.id):
        await call.message.answer('Выберите тему', reply_markup = category_type)
        await call.message.delete()

@dp.callback_query_handler(text='nazad_years')
async def buy_courses(call: CallbackQuery):
    if check_google_sheet(call.from_user.id):
        await call.message.answer('Выберите ВУЗ', reply_markup = univers_1)
        await call.message.delete()