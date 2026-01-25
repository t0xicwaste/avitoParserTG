from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.main_menu import main_kb

start_router = Router()


@start_router.message(CommandStart())
async def start(msg: Message):
    await msg.answer(
        "👋 Привет!\n"
        "Я помогу отслеживать объявления на Avito.\n"
        "\n"
        "🔔 Получай уведомления сразу после публикации\n"
        "🚲 Подходит для перекупов, магазинов и частных лиц"
    )
    await msg.answer("Выберите действие:", reply_markup=main_kb)
