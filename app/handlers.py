from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
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
    #add_result(2, "Путеводитель🗺", "Travel Guide 🗺")


####################### GAME #######################

@router.message(F.text == "Начать путешествие🧭" or F.text == "Start the trip🧭")
async def lvl1(message: Message):
    await message.answer("Какое-то вступление, фото")



####################### TRAVEL GUIDE #######################

@router.message(F.text == "Путеводитель🗺" or F.text == "Travel Guide 🗺")
async def eating_place(message: Message):
    await message.answer(get_text())



@router.message(F.text == "1" or F.text == "1")
async def eating_place(message: Message):
    await message.answer(get_text(1))






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