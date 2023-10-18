from loader import dp, bot
from aiogram import types
from keyboards.default.menuStart import basked_service,user_keyboard
from infos.models import Product, Users, Basked, BaskedItem
from handlers.users.start import lang


@dp.callback_query_handler(text='gobaskedcall')
async def basked_func1(msg: types.CallbackQuery):
    await msg.message.delete()
    basked_db = Basked.objects.get(user__chat_id=msg.from_user.id)
    basked_obj = basked_db.basked_set.all()
    s = ""
    summ = 0
    if basked_obj:
        await msg.message.answer('Sizning savatingiz:')
        for i in basked_obj:
            s += f"{i.product.name}, 1dona = {i.product.price}so'm, {i.count_product} dona. - {i.total} so'm\n\n"
            summ += i.total
        await msg.message.answer(s + "-------------------\n\n" + "Jami: " + str(summ) + " so'm",
                                 reply_markup=basked_service)
    else:
        await msg.message.answer('Savat bo\'sh holatda')


@dp.message_handler(text='🛍 Savat')
async def basked_func(msg: types.Message):
    basked_db = Basked.objects.get(user__chat_id=msg.from_user.id)
    basked_obj = basked_db.basked_set.all()
    s = ""
    summ = 0
    if basked_obj:
        await msg.answer('Sizning savatingiz:')
        for i in basked_obj:
            s += f"{i.product.name}, 1dona = {i.product.price}so'm, {i.count_product} dona. - {i.total} so'm\n\n"
            summ += i.total
        await msg.answer(s + "-------------------\n\n" + "Jami: " + str(summ) + " so'm",
                         reply_markup=basked_service)
    else:
        await msg.answer('Savat bo\'sh holatda')


@dp.message_handler(text='🛎 Buyurtma berish')
async def basked_func2(msg: types.Message):
    basked_db = Basked.objects.get(user__chat_id=msg.from_user.id)
    basked_obj = basked_db.basked_set.all()
    if basked_obj:
        pass
    else:
        await msg.answer('Savat bo\'sh holatda')
        await msg.answer("Bosh menu:", reply_markup=user_keyboard)


@dp.message_handler(text='⚙ O\'zgartirish')
async def basked_func2(msg: types.Message):
    basked_db = Basked.objects.get(user__chat_id=msg.from_user.id)
    basked_obj = basked_db.basked_set.all()
    if basked_obj:
        pass
    else:
        await msg.answer('Savat bo\'sh holatda')
        await msg.answer("Bosh menu:", reply_markup=user_keyboard)


@dp.message_handler(text='❌ Tozalash')
async def basked_func2(msg: types.Message):
    basked_db = Basked.objects.get(user__chat_id=msg.from_user.id)
    basked_obj = basked_db.basked_set.all()
    if basked_obj:
        pass
    else:
        await msg.answer('Savat bo\'sh holatda')
        await msg.answer("Bosh menu:", reply_markup=user_keyboard)


@dp.message_handler(text='↩ Orqaga')
async def basked_func2(msg: types.Message):
    basked_db = Basked.objects.get(user__chat_id=msg.from_user.id)
    basked_obj = basked_db.basked_set.all()
    if basked_obj:
        await lang(msg)
    else:
        await msg.answer('Savat bo\'sh holatda')
        await msg.answer("Bosh menu:", reply_markup=user_keyboard)


