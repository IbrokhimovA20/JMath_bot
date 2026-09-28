from aiogram.types import CallbackQuery
from keyboards.inline.konspekts import materials, material_sections

from loader import dp


# Кнопки Конспект / Задания / Шпаргалка: callback_data вида "lessons:mat_<раздел>_<тема>"
# Подключается раньше остальных хендлеров, потому что их фильтры ('teor' in call.data и т.п.)
# могут совпасть с названием темы
@dp.callback_query_handler(lambda call: call.data.startswith('lessons:mat_'), state='*')
async def send_materials(call: CallbackQuery):
    code, theme = call.data.split(':')[1][4:].split('_', 1)
    section = {value: key for key, value in material_sections.items()}[code]
    await call.answer()
    await call.message.delete()
    for file_id in materials[theme][section]:
        await call.message.answer_document(document=file_id)
