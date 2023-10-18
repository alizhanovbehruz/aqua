from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

language = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿O'zbekcha"),
            KeyboardButton(text="🇷🇺Русский "),
        ],
    ],
    resize_keyboard=True
)

basked_service = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🛎 Сделать заказ'),
        ],
        [
            KeyboardButton(text='⚙ Изменить'),
            KeyboardButton(text='❌ Очистить')
        ],
        [
            KeyboardButton(text="↩️Назад"),
        ],
    ],
    resize_keyboard=True
)


user_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📁 Каталог'),
            KeyboardButton(text='🛍 Корзина'),
        ],
        [
            KeyboardButton(text='📞 Обратная связь'),
            KeyboardButton(text='📍 Наш адрес'),
        ],
        [
            KeyboardButton(text='🇺🇿Сменить язык'),
        ],
    ],
    resize_keyboard=True
)

Loc_send = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍Отправить местоположение", request_location=True),
        ],
        [
            KeyboardButton(text="⬅Назад"),
        ],
        [
            KeyboardButton(text="⬅Вернуться в главное меню"),
        ]
    ],
    resize_keyboard=True
)

start_keyboard_vetdoctor = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Мой аккаунт"),
        ],
        [
            KeyboardButton(text="Связаться с администратором"),
        ],
    ],
    resize_keyboard=True
)

number_first = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отправить номер телефона', request_contact=True)
        ],
        [
            KeyboardButton(text='⬅Вернуться в главное меню')
        ],
    ],
    resize_keyboard=True
)

petowner_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🐶Найти ветеринара'),
        ],
        [
            KeyboardButton(text='🏥Найти клинику или ветаптеку'),
        ],
        [
            KeyboardButton(text='Связаться с администратором'),
        ],
    ],
    resize_keyboard=True
)

number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отправить номер телефона', request_contact=True)
        ],
        [
            KeyboardButton(text='⬅Назад')
        ],
        [
            KeyboardButton(text='⬅Вернуться в главное меню')
        ],
    ],
    resize_keyboard=True
)

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅Назад')
        ],
        [
            KeyboardButton(text='⬅Вернуться в главное меню')
        ],
    ],
    resize_keyboard=True
)

back_first = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅Вернуться в главное меню')
        ],
    ],
    resize_keyboard=True
)
