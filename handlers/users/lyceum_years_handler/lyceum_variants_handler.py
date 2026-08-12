from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from keyboards.default.lyceums import lyceum
from keyboards.inline.lyceum_variants import lyceum_variants
from keyboards.inline.follow_button import follow_inline_button
from handlers.users.start import check_google_sheet
from handlers.users.menu_handler import check_sub_channel
from data.config import CHANNEL_ID_1

from loader import dp, bot


@dp.message_handler(text='Лицейские варианты📄', state='*')
async def send_lyceum_variants(message: Message, state: FSMContext):
    if check_google_sheet(message.chat.id):
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_1, user_id=message.chat.id)):
            await message.answer('Выберите вариант:', reply_markup=lyceum_variants)
            await state.reset_state()
        else:
            await bot.send_message(chat_id=message.chat.id, text=f"Здравствуйте уважаемый {message.chat.first_name}, добро пожаловать на бот J.M.ath! для того чтобы пользоваться ботом подпишитесь на канал J.M.ath", reply_markup=follow_inline_button)
            await message.delete()
            await state.reset_state()


@dp.callback_query_handler(text='nazad_lyceum_variants')
async def back_to_lyceums(call: CallbackQuery):
    await call.message.answer('Выберите лицей: ', reply_markup=lyceum)
    await call.message.delete()
