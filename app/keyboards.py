from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from data.db import *



start_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="RU🇷🇺", callback_data="ru")],
                                                 [InlineKeyboardButton(text="EN🇺🇸", callback_data="en")]],
                                resize_keyboard=True)

def menu_keyboard(language):
    menu_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=str(get_text(1, language)))],
                                            [KeyboardButton(text="Путеводитель🗺️")]],
                                  resize_keyboard=True, input_field_placeholder="Выбери опцию:")
    return menu_kb

