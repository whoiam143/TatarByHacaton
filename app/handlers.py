from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

import TatarByHacaton.app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет я бот, который поможет узнать тебе больше о Татарском языке и Республике Татарстан  \n "
                         "Hi, I am a bot that will help you learn more about the Tatar language and the Republic of Tatarstan")
    await message.answer("Выбири опцию ->", reply_markup=kb.start_kb)