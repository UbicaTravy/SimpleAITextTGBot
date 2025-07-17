from aiogram import Router, types
from aiogram.filters import Command
from services.analyzer import DeepSeekAnalyzer

router = Router()

@router.message(Command("analyze"))
async def analyze_command(message: types.Message):
    await message.answer("Отправьте текст для анализа через DeepSeek AI")

@router.message()
async def handle_text(message: types.Message):
    try:
        analysis = DeepSeekAnalyzer.analyze_text(message.text)
        await message.answer(f"🔍 Анализ DeepSeek:\n\n{analysis}")
    except Exception as e:
        await message.answer(f"❌ Ошибка: {str(e)}")
