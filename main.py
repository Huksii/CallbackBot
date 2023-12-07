from aiogram import Bot, Dispatcher, executor
from aiogram.types import *

from os import system
system("clear")
from core.config import TOKEN, ADMIN_ID
from core.inline import menu, other, admin
from core.database import create_table, insert_users, find_user, pull_user, admin_get_users
from core.keyboard import registration, profile

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: Message):
    create_table()
    username = message.from_user.username
    first_name = message.from_user.first_name
    name = "Пользователь"
    if username != None:
        name = username
    elif first_name != None:
        name = first_name
    await message.answer(f"Добро пожаловать, {name}",
            reply_markup=menu)
    if message.from_user.id in ADMIN_ID:
        await message.answer(f"Вы администратор", reply_markup=admin)
    
    if find_user(message.from_user.id) is not None:
        await message.answer("Вы зашли на ваш профиль", reply_markup=profile)

    else:
        await message.answer("Зарегистрируйтесь", reply_markup=registration)

@dp.callback_query_handler()
async def menu_1(call: CallbackQuery):
    if call.data == "menu_1":
        await call.message.edit_text("https://www.youtube.com",
                reply_markup=menu)
    elif call.data == "menu_2":
        await call.message.edit_text("https://instagram.com",
                reply_markup=menu)
    elif call.data == "menu_3":
        await call.message.edit_reply_markup(reply_markup=other)
    elif call.data == "menu_4":
        await call.message.edit_reply_markup(reply_markup=menu)
    elif call.data == "other_1":
        await call.message.edit_text("https://web.telegram.org/a",
                reply_markup=other)
    elif call.data == "other_2":
        await call.message.edit_text("https://whatsapp.com",
                reply_markup=other)
    elif call.data == "del":
        l = ["😀", "😃", "😄", "😁", "😆", "🥹",
             "😅", "😂", "🤣", "🥲", "😊", "🙂", "😇"]
        loading = ""
        for i in l:
            loading += i
            await call.message.edit_text(f"Загрузка {loading}",
                reply_markup=menu)
            
        await call.message.delete_reply_markup()
        await call.message.delete()
    elif call.data == "users":
        if call.message.chat.id in ADMIN_ID:
            text = admin_get_users()
            await call.message.edit_text(text, reply_markup=admin)
        else:
            call.message.answer("У вас больше нет доступа к этой функции")

@dp.message_handler(content_types=ContentTypes.CONTACT)
async def contact(message:Message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    phone = message.contact.phone_number

    insert_users(user_id, username, first_name, last_name, phone)

    await message.answer(f"Вы зарегистрированы", reply_markup = profile)


@dp.message_handler(content_types=ContentTypes.TEXT)
async def contact(message:Message):
    if find_user(message.from_user.id) is not None:

        if message.text.lower() == "профиль":
            user_id = message.from_user.id
        
            t = pull_user(user_id)
            await message.answer(f"Данные о пользователе {t}")
    
    else:
        await message.answer("Ваш профиль не найден")

if __name__== "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except (KeyboardInterrupt, SystemExit):
        pass

