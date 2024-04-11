from .const import BOT_TOKEN
from aiogram import Bot, Dispatcher

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

__all__ = ['bot', 'dp']