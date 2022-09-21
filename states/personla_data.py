from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonlaData(StatesGroup):
    fullname = State()
    e_mail = State()
    phoneNum = State()