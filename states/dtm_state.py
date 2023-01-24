from aiogram.dispatcher.filters.state import StatesGroup, State

class StateDtm(StatesGroup):
    language = State()
    year = State()