import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from app.handlers import router
import app.keyboards as kb
from aiogram.types import Message
from translator import *
from data.db import *

dp = Dispatcher()


async def main():
    with open("data/token.txt", "r") as file:
        token = file.readline()
    bot = Bot(token)
    dp.include_router(router)
    create_bd()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())


