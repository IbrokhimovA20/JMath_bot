from aiogram.types import Message, ContentType
from data.config import ADMINS

from loader import dp


# Админ отправляет боту PDF, бот отвечает его file_id (нужно для материалов тем)
@dp.message_handler(content_types=ContentType.DOCUMENT, chat_id=ADMINS, state='*')
async def send_file_id(message: Message):
    await message.reply(f"{message.document.file_name}\n<code>{message.document.file_id}</code>")
