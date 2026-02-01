import asyncio
import os
from pathlib import Path

from aiogram import Bot, Dispatcher

from dotenv import load_dotenv
from loguru import logger

from db.connection import engine, flush_db
from handlers.start import start_router

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv("TOKEN")
if TOKEN is None:
    raise ValueError("Токен не найден! Проверьте файл .env")

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def db_startup(dispatcher: Dispatcher):
    await flush_db(engine=engine)


async def main():
    dp.include_router(start_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logger.info("Telegram bot starting!")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("The bot was just stopped!")
