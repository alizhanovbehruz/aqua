from loader import dp, bot
from aiogram import types
from infos.models import Product, Users, Basked, BaskedItem
from keyboards.inline.deals import product_keyboard, product_items, go_basked


@dp.message_handler(text='📁 Katalog')
async def catalog_func(msg: types.Message):
    product_obj = Product.objects.all()
    await msg.answer('Ajoyib', reply_markup=types.ReplyKeyboardRemove())
    await msg.answer('Maxsulotni tanlang', reply_markup=product_keyboard(product_obj))


@dp.callback_query_handler(lambda a: 'productfirst_' in a.data)
async def catalog_func1(msg: types.CallbackQuery):
    _, product_id = msg.data.split('_')
    await bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message.message_id - 1)
    await msg.message.delete()
    product_obj = Product.objects.filter(id=int(product_id)).first()
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=open(f'media/{product_obj.photo}', 'rb'),
                         caption=f"<b>{product_obj.name}</b>\n\n"
                                 f"{product_obj.desc}\n\n"
                                 f"<b>Narxi:</b> {product_obj.price}\n\n"
                                 f"Miqdorni tanlang:", reply_markup=product_items(product_id=product_obj.id))


@dp.callback_query_handler(lambda a: 'productitems_' in a.data)
async def catalog_func2(msg: types.CallbackQuery):
    _, count, product_id = msg.data.split('_')
    if count == 'save':
        count = int(msg.message.reply_markup.inline_keyboard[0][2]['text'])
        product = Product.objects.get(id=product_id)
        basked = Basked.objects.get(user__chat_id=msg.from_user.id)
        basked_obj = BaskedItem.objects.filter(basked=basked, product=product)
        if basked_obj:
            basked_obj = basked_obj.first()
            basked_obj.count_product += count
            basked_obj.save()
        else:
            BaskedItem.objects.create(basked=basked, product=product, count_product=count)
        await msg.message.delete()
        await msg.message.answer('Tovar savatga qo\'shildi',reply_markup=go_basked)
    elif count == 'back':
        await msg.message.delete()
        await catalog_func(msg.message)
    elif count == 'self':
        await msg.answer('Bu tovar Miqdori!', show_alert=True)
    else:
        needadd = (int(count))
        count = int(msg.message.reply_markup.inline_keyboard[0][2]['text'])
        if (needadd + count) <= 0:
            await msg.message.edit_reply_markup(reply_markup=product_items(product_id=product_id))
        else:
            await msg.message.edit_reply_markup(
                reply_markup=product_items(count=needadd + count, product_id=product_id))
