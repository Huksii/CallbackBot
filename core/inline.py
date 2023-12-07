from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Youtube", callback_data="menu_1"),
    InlineKeyboardButton("Instagram", callback_data="menu_2"),
    InlineKeyboardButton("Прочее ...", callback_data="menu_3"),
    InlineKeyboardButton("Delete_menu", callback_data="del"),
)

other = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Telegram", callback_data="other_1"),
    InlineKeyboardButton("Whatsapp", callback_data="other_2"),
    InlineKeyboardButton("Menu", callback_data="menu_4"),
    InlineKeyboardButton("Delete_menu", callback_data="del"),
)

admin = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("users", callback_data="users")
)