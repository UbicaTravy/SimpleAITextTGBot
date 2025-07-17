from aiogram import Dispatcher, Bot
from config import BOT_TOKEN
import asyncio

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    from handlers import common, text_analysis
    dp.include_router(common.router)
    dp.include_router(text_analysis.router)
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
