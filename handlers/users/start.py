import datetime
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menuStart import language, user_keyboard, name_keyb, back_first, \
    number
from keyboards.default.menuStart_ru import petowner_keyboard as petowner_keyboard_ru, \
    start_keyboard_vetdoctor as start_keyboard_vetdoctor_ru, back_first as back_first_ru \
    , user_keyboard as user_keyboard_ru, number as number_ru
from keyboards.inline.admin_keyb import start_admin
from loader import dp, bot
from filters.private_chat import IsPrivate
from keyboards.inline.deals import typework
from keyboards.inline.deal_ru import typework_
from infos.models import Users, Basked
from states.statesper import UserState
from states.statesper_ru import UserState_


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    return await message.answer("Muloqot tilini tanlang:\n"
                                "Выберите язык:", reply_markup=language)


@dp.message_handler(IsPrivate(), text=("🇺🇿O'zbekcha", '🇺🇿Сменить язык'))
async def lang(message: types.Message, user_obj=None):
    if not user_obj:
        user_obj = message.from_user
    db = Users.objects.filter(chat_id=user_obj.id)
    if not db:
        user = Users.objects.create(chat_id=user_obj.id,
                                    username=user_obj.username, time_created=datetime.datetime.now())
        Basked.objects.create(user=user)
        await UserState.full_name.set()
        await message.answer(
            f"Iltimos, Ismingizni kiriting!",
            reply_markup=types.ReplyKeyboardMarkup(
                keyboard=name_keyb(user_obj.full_name).keyboard + back_first.keyboard,
                resize_keyboard=True))
    else:
        db = db.first()
        if not db.full_name:
            await UserState.full_name.set()
            await message.answer('Siz to\'liq ro\'yhatdan o\'tmagansiz!!')
            return await message.answer(
                f"Iltimos, Ismingizni kiriting!",
                reply_markup=types.ReplyKeyboardMarkup(
                    keyboard=name_keyb(user_obj.full_name).keyboard + back_first.keyboard,
                    resize_keyboard=True))
        if not db.number_phone:
            await UserState.number_phone.set()
            await message.answer('Siz to\'liq ro\'yhatdan o\'tmagansiz!!')
            return await message.answer("Telefon raqamingizni kiriting!:",
                                        reply_markup=number)
        await message.answer("Bosh menu:", reply_markup=user_keyboard)


@dp.message_handler(IsPrivate(), text=("🇷🇺Русский", '🇷🇺Tilni o\'zgartirish'))
async def lang_(message: types.Message, user_obj=None):
    if not user_obj:
        user_obj = message.from_user
    db = Users.objects.filter(chat_id=user_obj.id)
    if not db:
        user = Users.objects.create(chat_id=user_obj.id,
                                    username=user_obj.username, time_created=datetime.datetime.now())
        Basked.objects.create(user=user)
        await UserState_.full_name.set()
        await message.answer(
            f"Пожалуйста, введите ваше имя!:",
            reply_markup=types.ReplyKeyboardMarkup(
                keyboard=name_keyb(user_obj.full_name).keyboard + back_first_ru.keyboard,
                resize_keyboard=True))
    else:
        db = db.first()
        if not db.full_name:
            await UserState_.full_name.set()
            await message.answer('Вы не полностью зарегистрированы!')
            return await message.answer(
                f"Пожалуйста, введите ваше имя!:",
                reply_markup=types.ReplyKeyboardMarkup(
                    keyboard=name_keyb(user_obj.full_name).keyboard + back_first_ru.keyboard,
                    resize_keyboard=True))
        if not db.number_phone:
            await UserState_.number_phone.set()
            await message.answer('Вы не полностью зарегистрированы!')
            return await message.answer("Отправьте свой номер телефона:",
                                        reply_markup=number_ru)
        await message.answer("Главное меню", reply_markup=user_keyboard_ru)


@dp.callback_query_handler(text='headback', state='*')
async def back_call(msg: types.CallbackQuery, state=FSMContext):
    await msg.message.delete()
    await lang(msg.message, user_obj=msg.from_user)
    await state.finish()


@dp.callback_query_handler(text='headbackru', state='*')
async def back_callru(msg: types.CallbackQuery, state=FSMContext):
    await msg.message.delete()
    await lang_(msg.message, user_obj=msg.from_user)
    await state.finish()


@dp.message_handler(IsPrivate(), text=['/start', '⬅Bosh menyuga qaytish', '⬅Вернуться в главное меню'], state="*")
async def bot(msg: types.Message, state=FSMContext):
    await bot_start(msg)
    await state.finish()


@dp.message_handler(IsPrivate(), text='Adminga murojaat qilish')
async def admin_func(msg: types.Message):
    await msg.answer('<b>Admin bilan bog`lanish:</b>\n'
                     f'📞 +998905042141\n'
                     '@alizhanovbekhruz\n', parse_mode='html')


@dp.message_handler(IsPrivate(), text='Связаться с администратором')
async def admin_func1(msg: types.Message):
    await msg.answer('<b>Связаться с администратором:</b>\n'
                     f'📞 +998905042141\n'
                     '@alizhanovbekhruz\n', parse_mode='html')
