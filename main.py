from aiogram import Bot, Dispatcher, executor, types
import sqlite3

from django.db.migrations import executor

from keyboards import markups as kb
from config import config
from data import text_data as te

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

base = sqlite3.connect('table.db')
cur = base.cursor()

@dp.message_handler(commands=['start'])
async def start_cmd(msg: types.Message):
    global user_id
    user_name = msg.from_user.username
    us_id = msg.from_user.id
    id = msg.chat.id
    await bot.send_message(id,te.START1 + str(user_name) + te.START2, reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message_id)
    if us_id not in user_id:
        user_id.append(us_id)
        print(user_id)

@dp.callback_query_handler(text='RU')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.OSN_TEXT,reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='back_to_lang')
async def menu(msg: types.Message):
    id = msg.from_user.id
    user_name = msg.from_user.username
    await bot.send_message(id, te.START1 + str(user_name) + te.START2, reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message_id)

@dp.callback_query_handler(text='UZ')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.OSN_TEXT,reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='back_to_menu')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.OSN_TEXT,reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_1')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.OSN_TEXT,reply_markup=kb.menu_1)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_2')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.OSN_TEXT,reply_markup=kb.menu_2)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_3')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.OSN_TEXT,reply_markup=kb.menu_3)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_4')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.OSN_TEXT,reply_markup=kb.menu_4)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_5')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.OSN_TEXT,reply_markup=kb.menu_5)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_6')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.OSN_TEXT,reply_markup=kb.menu_6)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_7')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.OSN_TEXT,reply_markup=kb.menu_7)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_7')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.OSN_TEXT,reply_markup=kb.menu_7)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_8')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.OSN_TEXT,reply_markup=kb.menu_8)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_9')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.OSN_TEXT,reply_markup=kb.menu_9)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_10')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.OSN_TEXT,reply_markup=kb.menu_10)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_11')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.OSN_TEXT,reply_markup=kb.menu_11)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_1_1')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id,te.img_menu_1_1,caption=te.menu_1_1,reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_1_2')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_1_2, caption=te.menu_1_2, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_1_3')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_1_3, caption=te.menu_1_3, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_1_4')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_1_4, caption=te.menu_1_4, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_1_5')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_1_5, caption=te.menu_1_5, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_1_6')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_1_6, caption=te.menu_1_6, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_2_1')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_2_1, caption=te.menu_2_1, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_3_1')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_3_1, caption=te.menu_3_1, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='menu_3_2')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_3_2, caption=te.menu_3_2, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_3_3')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_3_3, caption=te.menu_3_3, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_3_4')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_3_4, caption=te.menu_3_4, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_3_5')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_3_5, caption=te.menu_3_5, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_3_6')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_3_6, caption=te.menu_3_6, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_3_7')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_3_7, caption=te.menu_3_7, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_4_1')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_4_1, caption=te.menu_4_1, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_4_2')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_4_2, caption=te.menu_4_2, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_4_3')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_4_3, caption=te.menu_4_3, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_5_1')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_5_1, caption=te.menu_5_1, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_5_2')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_5_2, caption=te.menu_5_2, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_6_1')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_6_1, caption=te.menu_6_1, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_6_2')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_6_2, caption=te.menu_6_2, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_7_1')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_7_1, caption=te.menu_7_1, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_7_2')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_7_2, caption=te.menu_7_2, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_7_3')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_7_3, caption=te.menu_7_3, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_7_4')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_7_4, caption=te.menu_7_4, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_7_5')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_7_5, caption=te.menu_7_5, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_7_6')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_7_6, caption=te.menu_7_6, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_8_1')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_8_1, caption=te.menu_8_1, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_8_2')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_8_2, caption=te.menu_8_2, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_8_3')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_8_3, caption=te.menu_8_3, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_8_4')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_8_4, caption=te.menu_8_4, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_9_1')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_9_1, caption=te.menu_9_1, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_9_2')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_9_2, caption=te.menu_9_2, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_9_3')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_9_3, caption=te.menu_9_3, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_10_1')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_10_1, caption=te.menu_10_1, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_11_1')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(id, te.img_menu_11_1, caption=te.menu_11_1, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.message_handler(content_types=types.ContentTypes.ANY)
async def all_other_messages(message: types.Message):
    global state
    global admin_id
    await bot.send_message(message.from_user.id,'Не понял вас')
    g = message.from_user.id
    d = message.message_id


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
