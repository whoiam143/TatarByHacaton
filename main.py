import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router

import app.keyboards as kb

dp = Dispatcher()


async def main():
    with open("data/token.txt", "r") as file:
        token = file.readline()
    bot = Bot(token)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception:
        print("not working")
