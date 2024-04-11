from aiogram import types

from Config.initialize import dp, bot


@dp.message_handler(commands=["start"])
async def start(Msg: types.Message):
    await Msg.reply(
        "Привет, я миньон бот!"
    )