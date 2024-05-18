from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from time import sleep

from TatarByHacaton.data.db import *

import TatarByHacaton.app.keyboards as kb

router = Router()

global_language = ""

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("""Привет🖐️, я Татарин, и помогу тебе узнать больше о Республике Татарстан и её культуре!
-----------------------------------------
Hi🖐️, I am a Tatarin, and I will help you know more about the Republic of Tatarstan and its culture!""")
    await message.answer("Выбери язык / Choose language:", reply_markup=kb.start_kb)


@router.callback_query(F.data == "ru")
async def select_russian(callback: CallbackQuery):
    global global_language
    global_language = "ru"
    await callback.message.answer("Вы выбрали русский язык🇷🇺", reply_markup=kb.menu_kb)
    await callback.message.delete()
    #kb.menu_keyboard(global_language)



@router.callback_query(F.data == "en")
async def select_russian(callback: CallbackQuery):
    global global_language
    global_language = "en"
    await callback.message.answer("You selected english language🇺🇸")
    #kb.menu_keyboard(global_language)


@router.message(F.text == "Начать путешествие🧭" or F.text == "Start the trip🧭")
async def test(message: Message):
    #add_result(1, "Начать путешествие🧭", "Start the trip🧭")

    await message.answer("Привет", reply_markup=kb.menu_keyboard(global_language))