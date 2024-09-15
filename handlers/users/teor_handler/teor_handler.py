from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.callback_data import lesson_callback
from keyboards.inline.konspekts import *
from keyboards.inline.themes import theme_5_6


from aiogram.types import CallbackQuery

from loader import dp,bot
all_teors = {"teor_obiknovenniye_drobi" : ["BQACAgIAAxkBAAKfdGWOxpvhvnTf9HuQSdQxgrFJOEibAAKTOAACbbVpSBF-e-foZX0yNAQ"],
            }

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'teor_obiknovenniye_drobi'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.reply_document(document = "BQACAgIAAxkBAAKfdGWOxpvhvnTf9HuQSdQxgrFJOEibAAKTOAACbbVpSBF-e-foZX0yNAQ")
#     await call.message.delete()

@dp.callback_query_handler(lambda call: 'teor' in call.data)
async def buying_corse(call: CallbackQuery):
    print(call.data.split(":"))
    for i in all_teors[call.data.split(":")[1]]:
        await call.message.reply_document(document = i)
    await call.message.delete()


@dp.callback_query_handler(text='nazad_5_6')
async def buying_corse(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup = theme_5_6)
    await call.message.delete()

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'shpar_obiknovenniye_drobi'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.reply_document(document = "BQACAgIAAxkBAAKfiGWOyeyUUAYW39whOI92HCVk76jEAAKUOAACbbVpSBuXt7y0M1d9NAQ")
#     await call.message.delete()

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'teor_desyatichniye_drobi'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.reply_document(document = "BQACAgIAAxkBAAKfdmWOxyiocBZUc56H5Iudwk4p8SGEAAKWOAACbbVpSPnsJ9lNYQvHNAQ")
#     await call.message.delete()

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'teor_per_drobi'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.reply_document(document = "BQACAgIAAxkBAAKfeGWOx2N0tVbjEeNakM6j13MtuNYFAAKXOAACbbVpSPtrWbv0I6IWNAQ")
#     await call.message.delete()

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'teor_ratsion_chisla'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.reply_document(document = "BQACAgIAAxkBAAKfemWOx687mk6KlAz63pc2NVewIQG_AAKdOAACbbVpSL3QiJOThY5yNAQ")
#     await call.message.delete()

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'teor_stepen_rat_chisla'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.reply_document(document = "BQACAgIAAxkBAAKffGWOx8elJzPEYAgImX8wF4oZdPmMAAKeOAACbbVpSITFkcln8suNNAQ")
#     await call.message.delete()

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'teor_stepen_rat_chisla'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.reply_document(document = "BQACAgIAAxkBAAKfimWOygJKz45-FZOd0V2BktW7kCYaAAKgOAACbbVpSIzppBMGo7c3NAQ")
#     await call.message.delete()


# @dp.callback_query_handler(lesson_callback.filter(item_name = 'shpar_stepen_rat_chisla'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.reply_document(document = "BQACAgIAAxkBAAKhsGWU8ZBch2aTt497bBPFOg92lxDwAAImRwACSEyoSCYrFX29LNWYNAQ")
#     await call.message.delete()