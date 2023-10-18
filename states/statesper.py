from aiogram.dispatcher.filters.state import StatesGroup, State


class UserState(StatesGroup):
    full_name = State()
    number_phone = State()


class Ordering(StatesGroup):
    location = State()
    confirm = State()
