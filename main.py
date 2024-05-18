import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from app.handlers import router
import app.keyboards as kb
from aiogram.types import Message
from translator import *

dp = Dispatcher()


async def main():
    with open("data/token.txt", "r") as file:
        token = file.readline()
    bot = Bot(token)
    dp.include_router(router)
    await dp.start_polling(bot)
    
    
@dp.business_message()
async def check_business_message(message: Message):
    if message.from_user.id != message.chat.id:
        await message.answer(translate_to_tat(message.text))
        


@dp.message(Command('translate'))
async def check_message(message: Message):
    if message.chat.id < 0:
        if '/translate@aiogramadil_bot' in message.text:
            await message.answer(translate_to_tat(message.text[26:]))
        else:
            await message.answer(translate_to_tat(message.text[10:]))


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception:
        print("not working")

