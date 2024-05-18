from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import CommandStart, Command
from TatarByHacaton.translator import *

from time import sleep

from TatarByHacaton.data.db import *

import TatarByHacaton.app.keyboards as kb


router = Router()


####################### MENU and START #######################

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("""Привет🖐️, я Татарин, и помогу тебе узнать больше о Республике Татарстан и её культуре!
-----------------------------------------
Hi🖐️, I am a Tatarin, and I will help you know more about the Republic of Tatarstan and its culture!""")
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
async def lvl1(message: Message):
    await message.answer("Какое-то вступление, фото")



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
        if '/translate@aiogramadil_bot' in message.text: #НАДО ПОМЕНЯТЬ!!!
            await message.answer(translate_to_tat(message.text[26:]))
        else:
            await message.answer(translate_to_tat(message.text[10:]))