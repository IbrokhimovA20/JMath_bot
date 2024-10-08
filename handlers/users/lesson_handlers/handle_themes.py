from keyboards.inline.konspekts import give_documents,give_geot_documents
from loader import dp


from aiogram.types import CallbackQuery


@dp.callback_query_handler(lambda call: 'theme' in call.data)
async def handle_themes(call: CallbackQuery, callback_data: dict):
    await call.message.answer('Выберите что вам нужно', reply_markup= await give_documents())



@dp.callback_query_handler(lambda call: 'theme_geot' in call.data)
async def handle_themes(call: CallbackQuery, callback_data: dict):
    await call.message.answer('Выберите что вам нужно', reply_markup= await give_geot_documents())