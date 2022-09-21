from cgitb import text
import logging
import re
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from telegram import CallbackQuery, ReplyMarkup
from aiogram.types import CallbackQuery

from loader import dp


wiut_2019 = ['A', 'B', 'C']
wiut_2020 = ['']
wiut_2021 = []
iut_2019 = []
iut_2020 = []
iut_2021 = []
amity_2019 = []
amity_2020 = []
amity_2021 = []
bmu_2019 = []
bmu_2020 = []
bmu_2021 = []
plehanova_2019 = []
plehanova_2020 = []
plehanova_2021 = []
gubkina_2019 = []
gubkina_2020 = []
gubkina_2021 = []
lomonosova_2019 = []
lomonosova_2020 = []
lomonosova_2021 = []
mifi_2019 = []
mifi_2020 = []
mifi_2021 = []
national_2019 = []
national_2020 = []
national_2021 = []

def comparing(answer):
    true_cheked = []
    checked = []
    if answer[0] == 'wiut2019':
        del answer[0]
        for true_answer,cheking_answer in zip(wiut_2019,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'wiut2020':
        del answer[0]
        for true_answer,cheking_answer in zip(wiut_2020,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'wiut2021':
        del answer[0]
        for true_answer,cheking_answer in zip(wiut_2021,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'iut2019':
        del answer[0]
        for true_answer,cheking_answer in zip(iut_2019,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'iut2020':
        del answer[0]
        for true_answer,cheking_answer in zip(iut_2020,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'iut2021':
        del answer[0]
        for true_answer,cheking_answer in zip(iut_2021,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'amity2019':
        del answer[0]
        for true_answer,cheking_answer in zip(amity_2019,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'amity2020':
        del answer[0]
        for true_answer,cheking_answer in zip(amity_2020,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'amity2021':
        del answer[0]
        for true_answer,cheking_answer in zip(amity_2021,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'bmu2019':
        del answer[0]
        for true_answer,cheking_answer in zip(bmu_2019,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'bmu2020':
        del answer[0]
        for true_answer,cheking_answer in zip(bmu_2020,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'bmu2021':
        del answer[0]
        for true_answer,cheking_answer in zip(bmu_2021,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'plehanova2019':
        del answer[0]
        for true_answer,cheking_answer in zip(plehanova_2019,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'plehanova2020':
        del answer[0]
        for true_answer,cheking_answer in zip(plehanova_2020,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'plehanova2021':
        del answer[0]
        for true_answer,cheking_answer in zip(plehanova_2021,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'gubkina2019':
        del answer[0]
        for true_answer,cheking_answer in zip(gubkina_2019,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'gubkina2020':
        del answer[0]
        for true_answer,cheking_answer in zip(gubkina_2020,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'gubkina2021':
        del answer[0]
        for true_answer,cheking_answer in zip(gubkina_2021,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'lomonosova2019':
        del answer[0]
        for true_answer,cheking_answer in zip(lomonosova_2019,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'lomonosova2020':
        del answer[0]
        for true_answer,cheking_answer in zip(lomonosova_2020,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'lomonosova2021':
        del answer[0]
        for true_answer,cheking_answer in zip(lomonosova_2021,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'mifi2019':
        del answer[0]
        for true_answer,cheking_answer in zip(mifi_2019,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'mifi2020':
        del answer[0]
        for true_answer,cheking_answer in zip(mifi_2020,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'mifi2021':
        del answer[0]
        for true_answer,cheking_answer in zip(mifi_2021,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'national2019':
        del answer[0]
        for true_answer,cheking_answer in zip(national_2019,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'national2020':
        del answer[0]
        for true_answer,cheking_answer in zip(national_2020,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == 'national2021':
        del answer[0]
        for true_answer,cheking_answer in zip(national_2021,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    
    return len(true_cheked),checked

@dp.message_handler(text_contains='wiut2019')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='wiut2020')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='wiut2021')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='iut2019')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='iut2020')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='iut2021')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='amity2019')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='amity2020')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='amity2021')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='bmu2019')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='bmu2020')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='bmu2021')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='plehanova2019')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='plehanova2020')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='plehanova2021')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='gubkina2019')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='gubkina2020')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='gubkina2021')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='lomonosova2019')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='lomonosova2020')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='lomonosova2021')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='mifi2019')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='mifi2020')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='mifi2021')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='national2019')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='national2020')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='national2021')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))


