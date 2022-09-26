from cgitb import text
import logging
import re
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types import CallbackQuery

from loader import dp

answers_5 = ['A', 'B', 'C', 'D']
answers_6 = ['Y', 'V', 'Q', 'U']
answers_7 = ['I', 'V', 'Q', 'D']
answers_8 = ['A', 'D', 'A', 'W']
answers_9 = ['U', 'B', 'D', 'C']
answers_10 = ['D', 'A', 'S', 'C']
answers_11 = ['W', 'A', 'C', 'D']



def comparing(answer):
    true_cheked = []
    checked = []
    if answer[0] == '5класс':
        del answer[0]
        for true_answer,cheking_answer in zip(answers_5,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == '6класс':
        del answer[0]
        for true_answer,cheking_answer in zip(answers_6,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == '7класс':
        del answer[0]
        for true_answer,cheking_answer in zip(answers_7,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == '8класс':
        del answer[0]
        for true_answer,cheking_answer in zip(answers_8,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == '9класс':
        del answer[0]
        for true_answer,cheking_answer in zip(answers_9,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == '10класс':
        del answer[0]
        for true_answer,cheking_answer in zip(answers_10,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    elif answer[0] == '11класс':
        del answer[0]
        for true_answer,cheking_answer in zip(answers_11,answer):
            if true_answer == cheking_answer.upper():
                checked.append('✅')
                true_cheked.append(True)
            else:
                checked.append('❌')
    return len(true_cheked),checked

@dp.message_handler(text_contains='5класс')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n" .join(new_list))

@dp.message_handler(text_contains='6класс')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='7класс')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='8класс')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='9класс')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='10класс')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))

@dp.message_handler(text_contains='11класс')
async def check_answers(message: Message):
    truly,cheked = comparing(message.text.split(' '))
    new_list = []
    await message.answer('Количество ваших правильных ответов: ' + str(truly))
    for index, item in enumerate(cheked):
        new_list.append(f"{index+1}-{item}")
    await message.answer("\n".join(new_list))