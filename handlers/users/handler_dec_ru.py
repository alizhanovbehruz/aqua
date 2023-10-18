import datetime
from app import Loc_file_media
from aiogram import types
import re
from handlers.users.start import lang, lang_
from keyboards.default.menuStart import name_keyb
from keyboards.inline.deal_ru import City_keyb, Region_keyb, type_cl, truefalse_keyb, let_keyb, add_clinic_keyb, \
    type_vet_clinic
from keyboards.default.menuStart_ru import back_first, back, number, Loc_send, user_keyboard
from infos.models import Users
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from states.statesper_ru import UserState_
import os
from aiogram.types import ParseMode

phone_re = """^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"""


@dp.message_handler(state=UserState_.full_name)
async def vetdoktor(msg: types.Message, state=FSMContext):
    if msg.text.isdigit():
        return await msg.answer('Правильно введите ваше имя!:')
    Users.objects.filter(chat_id=msg.from_user.id).update(full_name=msg.text)
    await bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message_id - 1)
    await msg.delete()
    await UserState_.next()
    await msg.answer("Отправьте свой номер телефона:",
                     reply_markup=number)


@dp.message_handler(state=UserState_.number_phone, content_types=types.ContentType.CONTACT)
async def pacien_func3_2(msg: types.ContentType, state=FSMContext):
    txt = msg['contact']['phone_number']
    Users.objects.filter(chat_id=msg.from_user.id).update(number_phone=txt)
    await bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message_id - 1)
    await msg.delete()
    await state.finish()
    await msg.answer("Главное меню", reply_markup=user_keyboard)


@dp.message_handler(state=UserState_.number_phone)
async def number_phone(msg: types.Message, state=FSMContext):
    if msg.text == '⬅Назад':
        await UserState_.previous()
        await msg.answer("Пожалуйста, введите ваше имя!:",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=name_keyb(msg.from_user.full_name).keyboard + back_first.keyboard,
                             resize_keyboard=True))
        return
    if not re.match(phone_re, msg.text):
        await msg.answer("Введите свой номер телефона правильно!:")
        return
    Users.objects.filter(chat_id=msg.from_user.id).update(number_phone=msg.text)
    await bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message_id - 1)
    await msg.delete()
    await state.finish()
    await msg.answer("Главное меню", reply_markup=user_keyboard)
