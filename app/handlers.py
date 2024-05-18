from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from translator import *

from time import sleep

from data.db import *

import app.keyboards as kb


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
    await callback.message.answer("Вы выбрали русский язык🇷🇺")
    kb.user_lang(callback.from_user.id, 'ru')
    await callback.message.delete()
    #kb.menu_keyboard(global_language)



@router.callback_query(F.data == "en")
async def select_russian(callback: CallbackQuery):
    await callback.message.answer("You selected english language🇺🇸")
    kb.user_lang(callback.from_user.id, 'en')
    await callback.message.delete()
    #kb.menu_keyboard(global_language)


#@router.message(F.text == "Начать путешествие🧭" or F.text == "Start the trip🧭")
#async def test(message: Message):
#    add_result(1, "Начать путешествие🧭", "Start the trip🧭")
    #await message.answer("Привет", reply_markup=kb.menu_keyboard(global_language))
    

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