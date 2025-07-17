from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Отправь мне текст для анализа.")

@router.message(Command("help"))
async def help(message: types.Message):
    await message.answer("Доступные команды:\n/start - начать\n/help - помощь")
