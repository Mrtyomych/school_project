import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandObject
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message

import sqlite3
from random import shuffle

from BotDB import BotDB
from other_funtions import Functions
from config import settings

bot_db = BotDB("files/project.db")
bot = Bot(token=settings['token'])
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Главное меню",
        callback_data="menu")
    )
    await message.answer("Выберите действие", reply_markup=builder.as_markup())

@dp.callback_query(F.data == "menu")
async def menu(callback: types.CallbackQuery):
    await callback.message.delete()
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Профиль и статистика",
        callback_data="profile")
    )
    builder.add(types.InlineKeyboardButton(
        text="Тренировка",
        callback_data="train")
    )
    await callback.message.answer("Главное меню", reply_markup=builder.as_markup())

@dp.callback_query(F.data == "profile")
async def profile(callback: types.CallbackQuery):
    await callback.message.delete()
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Главное меню",
        callback_data="menu")
    )
    await callback.message.answer("В разработке", reply_markup=builder.as_markup())


@dp.callback_query(F.data == "train")
async def menu(callback: types.CallbackQuery):
    await callback.message.delete()
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Задание 4",
        callback_data="ex_4")
    )
    builder.add(types.InlineKeyboardButton(
        text="Главное меню",
        callback_data="menu")
    )
    await callback.message.answer(
        "Выберите задание, которое хотели бы прорешать",
        reply_markup=builder.as_markup())
    
@dp.callback_query(F.data == "ex_4")
async def send_new_ex_4(callback: types.CallbackQuery):
    await callback.message.delete()
    data = Functions.get_the_fourth_task()
    answers = [data[1]]
    answers.extend(data[2])
    shuffle(answers)

    builder = InlineKeyboardBuilder()
    for i in answers:
        if i == data[1]:
            builder.add(types.InlineKeyboardButton(
                text=f"{i}",
                callback_data="true_answer_ex_4")
            )
        else:
            builder.add(types.InlineKeyboardButton(
                text=f"{i}",
                callback_data="false_answer_ex_4")
            )

    await callback.message.answer(
        f"""Укажите вариант ответа, в котором во всех словах верно выделена буква, обозначающая ударный гласный звук.
        [1] {data[0][0]}
        [2] {data[0][1]}
        [3] {data[0][2]}
        [4] {data[0][3]}
        [5] {data[0][4]}""", 
        reply_markup=builder.as_markup())

@dp.callback_query(F.data == "true_answer_ex_4")
async def true_answer_ex_4(callback: types.CallbackQuery):
    await callback.message.delete()
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
                text=f"Продолжить",
                callback_data="ex_4")
            )
    builder.add(types.InlineKeyboardButton(
        text="Главное меню",
        callback_data="menu")
    )
    await callback.message.answer("Ты ахуеть как прав братишка", reply_markup=builder.as_markup())

@dp.callback_query(F.data == "false_answer_ex_4")
async def false_answer_ex_4(callback: types.CallbackQuery):
    await callback.message.delete()
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
                text=f"Продолжить",
                callback_data="ex_4")
            )
    builder.add(types.InlineKeyboardButton(
        text="Главное меню",
        callback_data="menu")
    )
    await callback.message.answer("Боже чел как мне за тебя стыдно ты больше не репер", reply_markup=builder.as_markup())

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


