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
            KeyboardButton(text='🛎 Buyurtma berish'),
        ],
        [
            KeyboardButton(text='⚙ O\'zgartirish'),
            KeyboardButton(text='❌ Tozalash')
        ],
        [
            KeyboardButton(text="↩ Orqaga"),
        ],
    ],
    resize_keyboard=True
)

def name_keyb(name):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=name)
            ]
        ],
        resize_keyboard=True
    )


Loc_send = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍Joylashuvni jo'natish", request_location=True),
        ],
        [
            KeyboardButton(text="⬅Orqaga"),
        ],
        [
            KeyboardButton(text="⬅Bosh menyuga qaytish"),
        ]
    ],
    resize_keyboard=True
)

start_keyboard_vetdoctor = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mening akkauntim"),
        ],
        [
            KeyboardButton(text="Adminga murojaat qilish"),
        ],
    ],
    resize_keyboard=True
)

number_first = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Telefon raqamni jo\'natish', request_contact=True)
        ],
        [
            KeyboardButton(text='⬅Bosh menyuga qaytish')
        ],
    ],
    resize_keyboard=True
)


def product_keyboard(obj):
    keyb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=i)
            ] for i in obj
        ]
    )
    keyb.keyboard.append([KeyboardButton(text='⬅Bosh menyuga qaytish')])
    return keyb


user_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📁 Katalog'),
            KeyboardButton(text='🛍 Savat'),
        ],
        [
            KeyboardButton(text='📞 Qayta aloqa'),
            KeyboardButton(text='📍 Bizning manzil'),
        ],
        [
            KeyboardButton(text='🇷🇺Tilni o\'zgartirish'),
        ],
    ],
    resize_keyboard=True
)

number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Telefon raqamni jo\'natish', request_contact=True)
        ],
        [
            KeyboardButton(text='⬅Orqaga')
        ],
        [
            KeyboardButton(text='⬅Bosh menyuga qaytish')
        ],
    ],
    resize_keyboard=True
)

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅Orqaga')
        ],
        [
            KeyboardButton(text='⬅Bosh menyuga qaytish')
        ],
    ],
    resize_keyboard=True
)

back_first = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅Bosh menyuga qaytish')
        ],
    ],
    resize_keyboard=True
)
