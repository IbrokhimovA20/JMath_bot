from aiogram.types import Message
from states.dtm_state import userState
from aiogram.dispatcher import FSMContext
from data.config import ADMINS_GROUP
import pandas as pd
from aiogram.types import CallbackQuery
from keyboards.inline.follow_button import user_answer
from keyboards.default.main_keyboard import menu
from loader import dp, bot


@dp.message_handler(state=userState.question_state)
async def give_to_group(message: Message, state:FSMContext):
    mes = await bot.forward_message(chat_id=ADMINS_GROUP, message_id=message.message_id, from_chat_id=message.from_user.id)
    df = pd.read_pickle("user_messages.pickle")
    pd.concat([pd.DataFrame({"user_id" : message.from_user.id, "message_id" : mes.message_id}, index=[0]),df]).to_pickle("user_messages.pickle")
    await bot.send_message(chat_id=message.chat.id, text="""Ваш вопрос отправлен в группу дождитесь ответа""")
    state.reset_state()


@dp.message_handler(content_types=['photo'], state=userState.question_state)
async def give_to_group(message: Message, state:FSMContext):
    mes = await bot.forward_message(chat_id=ADMINS_GROUP, message_id=message.message_id, from_chat_id=message.from_user.id)
    # mes = await bot.send_photo(chat_id=ADMINS_GROUP, photo=f"{message.photo[-1].file_id}")
    df = pd.read_pickle("user_messages.pickle")
    pd.concat([pd.DataFrame({"user_id" : message.from_user.id, "message_id" : mes.message_id}, index=[0]),df]).to_pickle("user_messages.pickle")
    await bot.send_message(chat_id=message.chat.id, text="""Ваш вопрос отправлен в группу дождитесь ответа""")
    state.reset_state()


@dp.message_handler(chat_id=ADMINS_GROUP)
async def give_to_group(message: Message, state:FSMContext):
    try:
        df = pd.read_pickle("user_messages.pickle")
        tg_id = df[df["message_id"] == message["reply_to_message"]["message_id"]]["user_id"].iloc[0]
        await bot.send_message(chat_id=tg_id, text=message.text)
        await bot.send_message(chat_id=tg_id, text="Вам понятен ответ ?", reply_markup=user_answer)
        # user_state = dp.current_state(user_id=tg_id, chat_id=42)
        # user_state.set_state(userState.question_state)
        # await userState.question_state.set()
    except:
        pass


@dp.message_handler(content_types=['photo'], chat_id=ADMINS_GROUP)
async def give_to_group(message: Message, state:FSMContext):
    try:
        df = pd.read_pickle("user_messages.pickle")
        tg_id = df[df["message_id"] == message["reply_to_message"]["message_id"]]["user_id"].iloc[0]
        await bot.send_photo(chat_id=tg_id, photo=f"{message.photo[-1].file_id}")
        await bot.send_message(chat_id=tg_id, text="Вам понятен ответ ?", reply_markup=user_answer)
        # await userState.question_state.set()
        # await bot.send_message(chat_id=tg_id, text=message.text)
    except:
        pass


@dp.message_handler(content_types=['video_note'], chat_id=ADMINS_GROUP)
async def give_to_group(message: Message, state:FSMContext):
    try:
        df = pd.read_pickle("user_messages.pickle")
        tg_id = df[df["message_id"] == message["reply_to_message"]["message_id"]]["user_id"].iloc[0]
        await bot.send_video_note(chat_id=tg_id, video_note=f"{message.video_note.file_id}")
        await bot.send_message(chat_id=tg_id, text="Вам понятен ответ ?", reply_markup=user_answer)
        # await userState.question_state.set()
        # await bot.send_message(chat_id=tg_id, text=message.text)
    except:
        pass


@dp.message_handler(content_types=['voice'], chat_id=ADMINS_GROUP)
async def give_to_group(message: Message, state:FSMContext):
    try:
        df = pd.read_pickle("user_messages.pickle")
        tg_id = df[df["message_id"] == message["reply_to_message"]["message_id"]]["user_id"].iloc[0]
        await bot.send_voice(chat_id=tg_id, voice=f"{message.voice.file_id}")
        await bot.send_message(chat_id=tg_id, text="Вам понятен ответ ?", reply_markup=user_answer)
        # await userState.question_state.set()
        # await bot.send_message(chat_id=tg_id, text=message.text)
    except:
        pass


@dp.message_handler(content_types=['voice'], state=userState.question_state)
async def give_to_group(message: Message, state:FSMContext):
    mes = await bot.forward_message(chat_id=ADMINS_GROUP, message_id=message.message_id, from_chat_id=message.from_user.id)
    # mes = await bot.send_voice(chat_id=ADMINS_GROUP, voice=f"{message.voice.file_id}")
    df = pd.read_pickle("user_messages.pickle")
    pd.concat([pd.DataFrame({"user_id" : message.from_user.id, "message_id" : mes.message_id}, index=[0]),df]).to_pickle("user_messages.pickle")
    await bot.send_message(chat_id=message.chat.id, text="""Ваш вопрос отправлен в группу дождитесь ответа""")
    state.reset_state()



@dp.message_handler(content_types=['video_note'], state=userState.question_state)
async def give_to_group(message: Message, state:FSMContext):
    mes = await bot.forward_message(chat_id=ADMINS_GROUP, message_id=message.message_id, from_chat_id=message.from_user.id)
    # mes = await bot.send_video_note(chat_id=ADMINS_GROUP, video_note=f"{message.video_note.file_id}")
    df = pd.read_pickle("user_messages.pickle")
    pd.concat([pd.DataFrame({"user_id" : message.from_user.id, "message_id" : mes.message_id}, index=[0]),df]).to_pickle("user_messages.pickle")
    await bot.send_message(chat_id=message.chat.id, text="""Ваш вопрос отправлен в группу дождитесь ответа""")
    state.reset_state()


@dp.callback_query_handler(text=['not_understood', 'understood'], state=userState.question_state)
async def buy_courses(call: CallbackQuery, state: FSMContext):
    if call.data == "understood":
        await bot.send_message(chat_id=call.from_user.id, text="Cпасибо что воспользовались нашим ботом. Удачи вам в дальнейшем!", reply_markup=menu)
        await state.reset_state()
    elif call.data == "not_understood":
        await bot.send_message(chat_id=ADMINS_GROUP, text=f"Ученик {call.from_user.first_name}, не понял объяснение")
        await bot.send_message(chat_id=message.chat.id, text="""Ваш вопрос отправлен в группу дождитесь ответа""")

    await call.message.delete()