from aiogram.dispatcher.filters.state import StatesGroup, State

class StateDtm(StatesGroup):
    language = State()
    year = State()
 
class userState(StatesGroup):
    message_state = State()
    question_state = State()
