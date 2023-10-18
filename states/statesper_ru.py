from aiogram.dispatcher.filters.state import StatesGroup, State


class UserState_(StatesGroup):
    full_name = State()
    number_phone = State()


class Ordering_(StatesGroup):
    location = State()
    confirm = State()
