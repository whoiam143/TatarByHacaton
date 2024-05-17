from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="RU🇷🇺", callback_data="ru")],
                                                 [InlineKeyboardButton(text="EN🇺🇸", callback_data="en")]],
                                resize_keyboard=True, input_field_placeholder="Choose language:")

