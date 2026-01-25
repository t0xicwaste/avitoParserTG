from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="➕ Добавить подписку", callback_data="addSub")],
        [InlineKeyboardButton(text="📂 Мои подписки", callback_data="mySub")],
        [InlineKeyboardButton(text="⚙️ Настройки", callback_data="settings")],
        [InlineKeyboardButton(text="💳 Тарифы", callback_data="tariffs")],
        [InlineKeyboardButton(text="🆘 Поддержка", callback_data="support")],
    ]
)
