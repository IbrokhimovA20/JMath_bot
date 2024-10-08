from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.callback_data import lesson_callback
from keyboards.inline.konspekts import *
from keyboards.inline.themes import geometriya_themes_1


from aiogram.types import CallbackQuery

from loader import dp


all_teors_geometriya = {"teor_geot_ugli" : ["BQACAgIAAxkBAAEBGntnBVpl8dJTfOULDDNBjcwdqFLiCQACYF8AAgpMKEgQQxoqwu2IyDYE"],
                        "teor_geot_paralel_pramoy" : ["BQACAgIAAxkBAAEBGn9nBVp5bRjpH0gUoyzjDFbFfCECSQACYl8AAgpMKEjnGxg80RCH1jYE"],
                        "teor_geot_treugolnik" : ["BQACAgIAAxkBAAEBGoFnBVqB4PBjkae-j-UxdSLe4smYbAACZF8AAgpMKEjCw_8naAUjfTYE"],
                        "teor_geot_vidi_treugolnikov" : ["BQACAgIAAxkBAAEBGoNnBVqG1CJZ7NuowT7C_N_0er6vFgACZV8AAgpMKEjzD7h1sUXEazYE"],
                        "teor_geot_sin_kos_tan_cotan" : ["BQACAgIAAxkBAAEBGoVnBVqMunbakSYJkFlN-L-wHxniegACZl8AAgpMKEhpbC_vbBIdBzYE"],
                        "teor_geot_biss_mediana_visota" : ["BQACAgIAAxkBAAEBGodnBVqS_YtYaTfgOT9lno1kqYw8qAACZ18AAgpMKEiHOJhFIfMhUjYE"],
                        "teor_geot_ploshad_treugolnikov" : ["BQACAgIAAxkBAAEBGolnBVqWWSkQsBPXyfPrzQXEvUd3UgACaF8AAgpMKEh2Gsu9SohTiTYE"],
                        "teor_geot_podobiye_treugolnikov" : ["BQACAgIAAxkBAAEBGotnBVqeDUGGWKd9-wJCN2qM3UKxhAACal8AAgpMKEiQI8WTbMidVjYE"],
                        "teor_geot_kvadrat" : ["BQACAgIAAxkBAAEBGo1nBVqiaFvJQSdxqAmKBEOHxUaEtwACbF8AAgpMKEiPVTK2BD5IvzYE"],
                        "teor_geot_parallelogram" : ["BQACAgIAAxkBAAEBGo9nBVqoobFsUMt90DvZHtiA7Q1H5AACbl8AAgpMKEhHIEc7DO8G_DYE"],
                        "teor_geot_trapetsiya" : ["BQACAgIAAxkBAAEBGpFnBVqtU2CVqrqLed20U7yitz43IAACb18AAgpMKEgbvO7e3HUaQjYE"],
                        "teor_geot_mnogougolnik" : ["BQACAgIAAxkBAAEBGpNnBVqxwJVNQaP-IkcWnRK6aNA_FgACcF8AAgpMKEhN78A2fBsSFjYE"],
                        "teor_geot_okrujnost_krug" : ["BQACAgIAAxkBAAEBGpVnBVq2ouHPfQ_LLqtxMankUviHXwACcV8AAgpMKEhnlGvdhME87DYE"],
                        "teor_geot_ploshad" : ["BQACAgIAAxkBAAEBGpdnBVq6ErB6lZBByr1ZDxCs3oSmOwACc18AAgpMKEhLMFf9zassJzYE"],
                        "teor_geot_okrujnost_treugolnik" : ["BQACAgIAAxkBAAEBGplnBVq_6M7v-vXDagyo1sghLfqMlwACdF8AAgpMKEjgt_UReH4DBzYE"],
                        "teor_geot_okrujnost_chugolnik" : ["BQACAgIAAxkBAAEBGptnBVrEBjfbtOXDEgABjBs32tvhRpQAAnVfAAIKTChId5MaakmqTRM2BA"],
                        "teor_geot_sistema_koordinat" : ["BQACAgIAAxkBAAEBGp1nBVrZauxeIer5gqvoP3tO7-ZKVgACdl8AAgpMKEgXPmjcNmJPwDYE"],
                        "teor_geot_prizma" : ["BQACAgIAAxkBAAEBGp9nBVrh2cm1EOJ7Q_owXKUJs1O2iAACd18AAgpMKEhsQ1l_bsvGcjYE"],
                        "teor_geot_piramida" : ["BQACAgIAAxkBAAEBGqFnBVrqyWCYBQj7rTsMWOhW1yICFQACeV8AAgpMKEhaMjvy_SrwtjYE"],
                        "teor_geot_silindr" : ["BQACAgIAAxkBAAEBGqNnBVryvLSXX_usMgzWKJpRPT345QACe18AAgpMKEgyfnsFitkHNzYE"],
                        "teor_geot_konus" : ["BQACAgIAAxkBAAEBGqVnBVr4vldX-24CqqVF8YOYF9q4HwACfF8AAgpMKEjw6DLlfOwc9zYE"],
                        "teor_geot_shar_sfera" : ["BQACAgIAAxkBAAEBGqdnBVsBiDLJtnDVTix4JaBEQ8xWcQACfV8AAgpMKEgAATfzI3b_hAY2BA"],
                        "teor_geot_kombinasiya" : ["BQACAgIAAxkBAAEBGqlnBVsGJ4c9thmUvISnxYFFa7qrrwACfl8AAgpMKEgAAXjmHAABcX8NNgQ"]}


@dp.callback_query_handler(lambda call: 'teor_geot' in call.data)
async def buying_corse(call: CallbackQuery):
    for i in all_teors_geometriya[call.data.split(":")[1]]:
        await call.message.reply_document(document = i)
    await call.message.delete()


@dp.callback_query_handler(lambda call: 'shpar_geot' in call.data)
async def buying_corse(call: CallbackQuery):
    for i in all_teors_geometriya[call.data.split(":")[1]]:
        await call.message.reply_document(document = i)
    await call.message.delete()

@dp.callback_query_handler(lambda call: 'prim_geot' in call.data)
async def buying_corse(call: CallbackQuery):
    for i in all_teors_geometriya[call.data.split(":")[1]]:
        await call.message.reply_document(document = i)
    await call.message.delete()


# @dp.callback_query_handler(lesson_callback.filter(item_name = 'ugli'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.reply_document(document = "BQACAgIAAxkBAAEBGntnBVpl8dJTfOULDDNBjcwdqFLiCQACYF8AAgpMKEgQQxoqwu2IyDYE")
#     await call.message.delete()
#     # await call.message.answer('В процессе скоро все дополним ...')
#     await call.message.delete()

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_paralel_pramoy'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('В процессе скоро все дополним ...')
#     await call.message.delete()

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_treugolnik'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('В процессе скоро все дополним ...')
#     await call.message.delete()

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_vidi_treugolnikov'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('В процессе скоро все дополним ...')
#     await call.message.delete()

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_sin_kos_tan_cotan'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('В процессе скоро все дополним ...')
#     await call.message.delete()

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_teorema_sin_cos'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('В процессе скоро все дополним ...')
#     await call.message.delete()

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_biss_mediana_visota'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('В процессе скоро все дополним ...')
#     await call.message.delete()

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_ploshad_treugolnikov'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('В процессе скоро все дополним ...')
#     await call.message.delete()

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'kons_podobiye_treugolnikov'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.answer('В процессе скоро все дополним ...')
#     await call.message.delete()

# @dp.callback_query_handler(text='nazad_geometry_1')
# async def buying_corse(call: CallbackQuery):
#     await call.message.answer('Выберите тему', reply_markup = geometriya_themes_1)
#     await call.message.delete()