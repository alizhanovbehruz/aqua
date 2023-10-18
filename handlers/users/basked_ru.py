from handlers.users.start import lang_
from loader import dp, bot
from aiogram import types
from infos.models import Product, Users, Basked, BaskedItem
from keyboards.default.menuStart_ru import basked_service, user_keyboard as user_keyboard_ru
from states.statesper_ru import Ordering_
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text='gobaskedcalru')
async def basked_func1(msg: types.CallbackQuery):
    await msg.message.delete()
    basked_db = Basked.objects.get(user__chat_id=msg.from_user.id)
    basked_obj = basked_db.basked_set.all()
    s = ""
    summ = 0
    if basked_obj:
        await msg.message.answer('Ваша корзина:')
        for i in basked_obj:
            s += f"{i.product.name}, 1шт = {i.product.price}сум, {i.count_product} штук. - {i.total} сум\n\n"
            summ += i.total
        await msg.message.answer(s + "-------------------\n\n" + "Общий: " + str(summ) + " сум",
                                 reply_markup=basked_service)
    else:
        await msg.message.answer('Ваша корзина пуста')


@dp.message_handler(text='🛍 Корзина')
async def basked_func(msg: types.Message):
    basked_db = Basked.objects.get(user__chat_id=msg.from_user.id)
    basked_obj = basked_db.basked_set.all()
    s = ""
    summ = 0
    if basked_obj:
        await msg.answer('Ваша корзина:')
        for i in basked_obj:
            s += f"{i.product.name}, 1шт = {i.product.price}сум, {i.count_product} штук. - {i.total} сум\n\n"
            summ += i.total
        await msg.answer(s + "-------------------\n\n" + "Общий: " + str(summ) + " сум", reply_markup=basked_service)
    else:
        await msg.answer('Ваша корзина пуста')


@dp.message_handler(text='🛎 Сделать заказ')
async def basked_func2(msg: types.Message):
    basked_db = Basked.objects.get(user__chat_id=msg.from_user.id)
    basked_obj = basked_db.basked_set.all()
    if basked_obj:
        await Ordering_.location.set()
        await msg.answer("Пожалуйста, отправьте свое местоположение. (Не забудьте включить GPS!)")
    else:
        await msg.answer('Ваша корзина пуста')
        await msg.answer("Главное меню", reply_markup=user_keyboard_ru)


@dp.message_handler(text='⚙ Изменить')
async def basked_func2(msg: types.Message):
    basked_db = Basked.objects.get(user__chat_id=msg.from_user.id)
    basked_obj = basked_db.basked_set.all()
    if basked_obj:
        pass
    else:
        await msg.answer('Ваша корзина пуста')
        await msg.answer("Главное меню", reply_markup=user_keyboard_ru)


@dp.message_handler(text='❌ Очистить')
async def basked_func2(msg: types.Message):
    basked_db = Basked.objects.get(user__chat_id=msg.from_user.id)
    basked_obj = basked_db.basked_set.all()
    if basked_obj:
        pass
    else:
        await msg.answer('Ваша корзина пуста')
        await msg.answer("Главное меню", reply_markup=user_keyboard_ru)


@dp.message_handler(text='↩️Назад')
async def basked_func2(msg: types.Message):
    basked_db = Basked.objects.get(user__chat_id=msg.from_user.id)
    basked_obj = basked_db.basked_set.all()
    if basked_obj:
        await lang_(msg)
    else:
        await msg.answer('Ваша корзина пуста')
        await msg.answer("Главное меню", reply_markup=user_keyboard_ru)


"""Ordering"""


@dp.message_handler(state=Ordering_.location, text='⬅Назад')
async def basked_func3(msg: types.Message, state=FSMContext):
    await basked_func(msg)
    await state.finish()


@dp.message_handler(state=Ordering_.location, content_types=types.ContentType.LOCATION)
async def basked_func4(msg: types.ContentType.LOCATION, state=FSMContext):
    async with state.proxy() as data:
        data['latitude'] = msg.location.latitude
        data['longitude'] = msg.location.longitude
    basked_db = Basked.objects.get(user__chat_id=msg.from_user.id)
    basked_obj = basked_db.basked_set.all()
    s = ""
    summ = 0
    await msg.message.answer('Ваша корзина:')
    for i in basked_obj:
        s += f"{i.product.name}, 1шт = {i.product.price}сум, {i.count_product} штук. - {i.total} сум\n\n"
        summ += i.total
    await msg.answer(f"<b>ЗАКАЗ:</b>\n" + s + "-------------------\n\n" + "Общий: " + str(summ) + " сум")
