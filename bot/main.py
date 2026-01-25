import asyncio
import os
from pathlib import Path

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers.start import start_router
from loguru import logger

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(start_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logger.info("Telegram bot starting!")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("The bot was just stopped!")
