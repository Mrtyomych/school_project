import asyncio
import sqlite3
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from other import BotDB, Functions
from config import settings

bot_db = BotDB("files/project.db")
bot = Bot(token=settings['token'])
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Hello!")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


