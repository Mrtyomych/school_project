import asyncio
import sqlite3
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

import json
import random

from db import BotDB
from config import settings

bot_db = BotDB("project.db")
bot = Bot(token=settings['token'])
dp = Dispatcher()

def get_new_exercise() -> tuple:
    """
        Возвращает кортеж, состоящий из списка слов и последовательности цифр, являющейся номерами верно написанных слов
    """
    with open("pr.json", "r", encoding="utf-8") as file:
        data = list(json.load(file).items())
        amount_true_answers = random.randint(1,4)
        true_answers = [random.choice(data)[0] for i in range(amount_true_answers)]  
        false_answers = [random.choice(random.choice(data)[1]) for i in range(5-amount_true_answers)]  
        result = true_answers.copy() + false_answers.copy()
        random.shuffle(result)
        
        answer = ""
        for i in range(len(result)):
            if result[i] in true_answers:
                answer += str(i+1)
        return (result, answer)

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Hello!")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


