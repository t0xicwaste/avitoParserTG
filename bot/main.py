import asyncio
import os

from loguru import logger
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logger.info("Telegram bot starting!")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("The bot was just stopped!")