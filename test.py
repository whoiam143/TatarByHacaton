import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from app.handlers import router
import app.keyboards as kb
from aiogram.types import Message, CallbackQuery
from translator import *
from data.db import *
from aiogram.types import FSInputFile

dp = Dispatcher()


async def main():
    with open("token.txt", "r") as file:
        token = file.readline()
    bot = Bot(token)
    dp.include_router(router)
    create_bd()
    await dp.start_polling(bot)


@dp.message()
async def lvl1(message: Message):
    photo = FSInputFile("pictures/1.jpg")
    await message.answer_photo(photo, get_text(21, "ru"), reply_markup=kb.lvl11)

@dp.callback_query(F.data == "11")
async def lvl1_callback(message: CallbackQuery):
    await message.message.delete()
    photo = FSInputFile("pictures/1.jpg")
    await message.message.answer_photo(photo, get_text(21, "ru"), reply_markup=kb.lvl12)

@dp.callback_query(F.data == "12")
async def lvl1_callback(message: CallbackQuery):
    await message.message.delete()
    photo = FSInputFile("pictures/1.jpg")
    await message.message.answer_photo(photo, get_text(22, "ru"), reply_markup=kb.lvl12)

@dp.callback_query(F.data == "21")
async def lvl1_callback(message: CallbackQuery):
    await message.message.delete()
    photo = FSInputFile("pictures/2.png")
    await message.message.answer_photo(photo, get_text(31, "ru"), reply_markup=kb.lvl21)

@dp.callback_query(F.data == "22")
async def lvl1_callback(message: CallbackQuery):
    message.message.delete()
    photo = FSInputFile("pictures/2.png")
    await message.message.answer_photo(photo, get_text(32, "ru"), reply_markup=kb.lvl22)

@dp.callback_query(F.data == "q111")
async def lvl1_callback(message: CallbackQuery):
    message.message.delete()
    photo = FSInputFile("pictures/2.png")
    await message.message.answer_photo(photo, get_text(111, "ru"), reply_markup=kb.q111)

@dp.callback_query(F.data == "wrong1")
async def lvl1_callback(message: CallbackQuery):
    await message.message.answer('Неверно')


@dp.callback_query(F.data == "31")
async def lvl1_callback(message: CallbackQuery):
    await message.message.delete()
    await message.message.answer('Верно')
    photo = FSInputFile("pictures/3.png")
    await message.message.answer_photo(photo, get_text(41, "ru"), reply_markup=kb.lvl31)


@dp.callback_query(F.data == "32")
async def lvl1_callback(message: CallbackQuery):
    message.message.delete()
    photo = FSInputFile("pictures/3.png")
    await message.message.answer_photo(photo, get_text(42, "ru"), reply_markup=kb.lvl32)


@dp.callback_query(F.data == "41")
async def lvl1_callback(message: CallbackQuery):
    photo = FSInputFile("pictures/4.png")
    await message.message.answer_photo(photo, get_text(51, "ru"), reply_markup=kb.lvl41)    
    


@dp.callback_query(F.data == "q222")
async def lvl1_callback(message: CallbackQuery):
    message.message.delete()
    photo = FSInputFile("pictures/5.png")
    await message.message.answer_photo(photo, get_text(53, "ru"), reply_markup=kb.q222)   


@dp.callback_query(F.data == "42")
async def lvl1_callback(message: CallbackQuery):
    photo = FSInputFile("pictures/4.png")
    await message.message.answer_photo(photo, get_text(52, "ru"), reply_markup=kb.lvl42) 


@dp.callback_query(F.data == "43")
async def lvl1_callback(message: CallbackQuery):
    photo = FSInputFile("pictures/4.png")
    await message.message.answer_photo(photo, get_text(54, "ru"), reply_markup=kb.lvl43)


@dp.callback_query(F.data == "51")
async def lvl1_callback(message: CallbackQuery):
    photo = FSInputFile("pictures/6.png")
    await message.message.answer_photo(photo, get_text(61, "ru"), reply_markup=kb.lvl51)
    
    
if __name__ == '__main__':
    asyncio.run(main())
