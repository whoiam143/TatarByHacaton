import asyncio

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import CommandStart, Command
from translator import *


from data.db import *

import app.keyboards as kb


router = Router()


####################### MENU and START #######################

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("""Привет🖐️, я татарин Айдар, и помогу тебе узнать больше о Республике Татарстан и её культуре!
-----------------------------------------
Hi🖐️, I am a Tatarin Aidar, and I will help you know more about the Republic of Tatarstan and its culture!""")
    await message.answer("Выбери язык / Choose language:", reply_markup=kb.start_kb)


@router.callback_query(F.data == "ru")
async def select_russian(callback: CallbackQuery):
    kb.user_lang(callback.from_user.id, "ru")
    await callback.message.answer("Вы выбрали русский язык🇷🇺", reply_markup=kb.menu_keyboard(callback.from_user.id))
    await callback.message.delete()


@router.callback_query(F.data == "en")
async def select_russian(callback: CallbackQuery):
    kb.user_lang(callback.from_user.id, "en")
    await callback.message.answer("You selected english language🇺🇸", reply_markup=kb.menu_keyboard(callback.from_user.id))
    await callback.message.delete()


@router.message(F.text.in_(["Назад ⬅️", "Back ⬅️"]))
async def back1(message: Message):
    await message.answer(get_text(6, kb.get_user_lang(message.from_user.id)),reply_markup=kb.menu_keyboard(message.from_user.id))


@router.message(F.text.in_(["⬅️ Назад", "⬅️ Back"]))
async def back2(message: Message):
    await message.answer(get_text(8, kb.get_user_lang(message.from_user.id)),reply_markup=kb.eat_veiw(message.from_user.id))


@router.message(F.text.in_(["Назад", "Back"]))
async def back2(message: Message):
    await message.answer(get_text(8, kb.get_user_lang(message.from_user.id)),reply_markup=kb.eat_veiw(message.from_user.id))


####################### GAME #######################

@router.message(F.text.in_(["Начать путешествие🧭", "Start the trip🧭"]))
async def start(message: Message):
    photo = FSInputFile("pictures/shit.jpg")
    await message.answer_photo(photo, get_text(21, kb.get_user_lang(message.from_user.id)))
    await asyncio.sleep(10)
    photo2 = FSInputFile("pictures/karta1.jpg")
    await message.answer_photo(photo2, get_text(22, kb.get_user_lang(message.from_user.id)))
    await asyncio.sleep(3)
    photo3 = FSInputFile("pictures/bolgar_mech.jpg")
    await message.answer_photo(photo3, get_text(23, kb.get_user_lang(message.from_user.id)))
    await asyncio.sleep(13)
    await message.answer(get_text(24, kb.get_user_lang(message.from_user.id)), reply_markup=kb.kvest1(message.from_user.id))


@router.message(F.text.in_(["Брутальный треугольник💪", "The Brutal Triangle💪", "Лапша быстрого приготовления🍜", "Instant noodles🍜"]))
async def check1(message: Message):
    await message.reply(get_text(30, kb.get_user_lang(message.from_user.id)), reply_markup=kb.kvest1(message.from_user.id, ))


@router.message(F.text.in_(["Три угла📐", "Three corners📐"]))
async def lvl2_3(message: Message):
    await message.reply(get_text(31, kb.get_user_lang(message.from_user.id)))
    photo = FSInputFile("pictures/treygl1.jpg")
    await message.answer_photo(photo, get_text(32, kb.get_user_lang(message.from_user.id)))
    await asyncio.sleep(3)
    karta2 = FSInputFile("pictures/karta2.jpg")
    await message.answer_photo(karta2, get_text(34, kb.get_user_lang(message.from_user.id)))
    await asyncio.sleep(3)
    vid = FSInputFile("pictures/inno.mp4")
    await message.answer_video(vid, caption=get_text(33, kb.get_user_lang(message.from_user.id)))
    await asyncio.sleep(10)
    photo2 = FSInputFile("pictures/treygl4.jpg")
    await message.answer_photo(photo2, get_text(32, kb.get_user_lang(message.from_user.id)))
    await asyncio.sleep(3)
    karta2 = FSInputFile("pictures/karta3.jpg")
    await message.answer_photo(karta2, get_text(35, kb.get_user_lang(message.from_user.id)))
    await asyncio.sleep(3)
    photo3 = FSInputFile("pictures/sviyajsk.jpg")
    await message.answer_photo(photo3, get_text(36, kb.get_user_lang(message.from_user.id)))
    await asyncio.sleep(10)
    await message.answer(get_text(37, kb.get_user_lang(message.from_user.id)), reply_markup=kb.kvest2(message.from_user.id))


@router.message(F.text.in_(["C овощами🍅", "With vegetables 🍅", "C фруктами🍏", "With fruits🍏"]))
async def check1(message: Message):
    await message.reply(get_text(30, kb.get_user_lang(message.from_user.id)), reply_markup=kb.kvest2(message.from_user.id, ))


@router.message(F.text.in_(["C мясом и картошкой🍖🥔", "With meat and potatoes🍖🥔"]))
async def lvl3_4(message: Message):
    await message.reply(get_text(31, kb.get_user_lang(message.from_user.id)))
    photo = FSInputFile("pictures/treygl3.jpg")
    await message.answer_photo(photo, get_text(32, kb.get_user_lang(message.from_user.id)))
    await asyncio.sleep(3)
    karta4 = FSInputFile("pictures/karta4.jpg")
    await message.answer_photo(karta4, get_text(41, kb.get_user_lang(message.from_user.id)))
    await asyncio.sleep(3)
    photo3 = FSInputFile("pictures/kazan.jpg")
    await message.answer_photo(photo3, get_text(42, kb.get_user_lang(message.from_user.id)))
    await asyncio.sleep(10)
    await message.answer("https://www.youtube.com/watch?v=rEqRoRZ96V4&ab_channel=tatarcha")
    await asyncio.sleep(10)
    await message.answer(get_text(46, kb.get_user_lang(message.from_user.id)), reply_markup=kb.kvest3(message.from_user.id))


@router.message(F.text.in_(["Богатая купчиха💰", "A rich merchant's wife💰", "Крестьянка👩", "Peasant woman 👩"]))
async def check1(message: Message):
    await message.reply(get_text(30, kb.get_user_lang(message.from_user.id)), reply_markup=kb.kvest3(message.from_user.id, ))


@router.message(F.text.in_(["Правительница Казани👸", "The ruler of Kazan 👸"]))
async def lvl3_4(message: Message):
    await message.reply(get_text(31, kb.get_user_lang(message.from_user.id)))
    photo = FSInputFile("pictures/treygl2.jpg")
    await message.answer_photo(photo, get_text(47 , kb.get_user_lang(message.from_user.id)))
    await asyncio.sleep(3)
    gif = FSInputFile("pictures/ech.gif")
    await message.answer_animation(gif, caption=get_text(48, kb.get_user_lang(message.from_user.id)), reply_markup=kb.menu_keyboard(message.from_user.id))


####################### TRAVEL GUIDE #######################Travel Guide 🗺
@router.message(F.text.in_(["Travel Guide 🗺", "Путеводитель🗺"]))
async def eating_place(message: Message):
    await message.answer(get_text(3, kb.get_user_lang(message.from_user.id)), reply_markup=kb.eat_veiw(message.from_user.id))


@router.message(F.text.in_(["Попробовать местную кухню🍴", "Try the cuisine🍴"]))
async def eating(message: Message):
    await message.answer(get_text(7, kb.get_user_lang(message.from_user.id)), reply_markup=kb.eat(message.from_user.id))


@router.message(F.text.in_(["Развлечься🤟", "Have fun🤟"]))
async def fun(message: Message):
    await message.answer(get_text(12, kb.get_user_lang(message.from_user.id)), reply_markup=kb.fun(message.from_user.id))


@router.message(F.text == "1. Тюбетей")
async def tubetey(message: Message):
    photo = FSInputFile("pictures/tubetey.jpg")
    await message.answer_photo(photo, get_text(9, kb.get_user_lang(message.from_user.id)), reply_markup=kb.eat(message.from_user.id))


@router.message(F.text == "2. Гусь")
async def tubetey(message: Message):
    photo = FSInputFile("pictures/gus.jpg")
    await message.answer_photo(photo, get_text(10, kb.get_user_lang(message.from_user.id)), reply_markup=kb.eat(message.from_user.id))


@router.message(F.text == "3. Азу")
async def tubetey(message: Message):
    photo = FSInputFile("pictures/azy.jpg")
    await message.answer_photo(photo, get_text(11, kb.get_user_lang(message.from_user.id)), reply_markup=kb.eat(message.from_user.id))


@router.message(F.text == "1. Skypark")
async def tubetey(message: Message):
    photo = FSInputFile("pictures/skypark.jpg")
    await message.answer_photo(photo, get_text(14, kb.get_user_lang(message.from_user.id)), reply_markup=kb.fun(message.from_user.id))


@router.message(F.text == "2. Форсаж")
async def tubetey(message: Message):
    photo = FSInputFile("pictures/forsaj.jpg")
    await message.answer_photo(photo, get_text(15, kb.get_user_lang(message.from_user.id)), reply_markup=kb.fun(message.from_user.id))


@router.message(F.text == "3. LazerLand")
async def tubetey(message: Message):
    photo = FSInputFile("pictures/lazerland.jpg")
    await message.answer_photo(photo, get_text(16, kb.get_user_lang(message.from_user.id)), reply_markup=kb.fun(message.from_user.id))


####################### TRANSLATER #######################
@router.business_message()
async def check_business_message(message: Message):
    if message.from_user.id != message.chat.id:
        await message.answer(translate_to_tat(message.text))


@router.message(Command('translate'))
async def check_message(message: Message):
    if message.chat.id < 0:
        if '/translate@TatarinForHacatonBot' in message.text:
            if match(message.text):
                await message.answer(translate_to_tat(message.text[31:]))
            else:
                await message.answer(translate_from_en_to_tat(message.text[31:]))
        else:
            if match(message.text):
                await message.answer(translate_to_tat(message.text[10:]))
            else:
                await message.answer(translate_from_en_to_tat(message.text[10:]))


@router.message(F.text.in_(["Переводчик🌎", "Translator🌎"]))
async def translator(message: Message):
    await message.answer(get_text(50, kb.get_user_lang(message.from_user.id)), reply_markup=kb.kb_translate(message.from_user.id))


@router.message(F.text.in_(["Назад⏪️", "Back⏪️"]))
async def translator(message: Message):
    await message.answer(get_text(51, kb.get_user_lang(message.from_user.id)),reply_markup=kb.menu_keyboard(message.from_user.id))


def match(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    return not alphabet.isdisjoint(text.lower())


@router.message(F.text.in_(["Добавление бота переводчика в чат➕", "Adding a bot for translating in a chat➕"]))
async def translator(message: Message):
    await message.answer(get_text(53, kb.get_user_lang(message.from_user.id)))
    
    
    
@router.message()
async def translate_text(message: Message):
    if match(message.text):
        await message.answer(translate_to_tat(message.text))
    else:
        await message.answer(translate_from_en_to_tat(message.text))
