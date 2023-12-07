from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

registration = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text="Зарегистрироваться", request_contact=True),
)

profile = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text="Профиль"),
)