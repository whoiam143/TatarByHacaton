from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from TatarByHacaton.data.db import *


start_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="RU🇷🇺", callback_data="ru")],
                                                 [InlineKeyboardButton(text="EN🇺🇸", callback_data="en")]],
                                resize_keyboard=True)


def menu_keyboard(user_id):
    menu_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=str(get_text(1, get_user_lang(user_id))))],
                                            [KeyboardButton(text=str(get_text(2, get_user_lang(user_id))))]],
                                  resize_keyboard=True, input_field_placeholder="Выбери опцию:")
    return menu_kb

def kvest1(user_id):
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="1 отве", callback_data="ru")],
                                                 [InlineKeyboardButton(text="EN🇺🇸", callback_data="en")]],
                                resize_keyboard=True)


def user_lang(user_id, lang):
    with sql.connect('data/dictionary.sqlite3') as db:
        cur = db.cursor()
        res = cur.execute("""SELECT * FROM users WHERE user_id == ? """, (user_id, ))
        if res.fetchone() is None:
            cur.execute("""INSERT INTO users VALUES (?, ?)""", (user_id, lang))
            db.commit()
        else:
            cur.execute("""UPDATE users SET lang == ? WHERE user_id == ?""", (lang, user_id))
            db.commit()
            

def get_user_lang(user_id):
    with sql.connect('data/dictionary.sqlite3') as db:
        cur = db.cursor()
        res = cur.execute("""SELECT lang FROM users WHERE user_id == ? """, (user_id, ))
        return res.fetchone()[0]