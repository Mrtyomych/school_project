import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandObject
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message

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
        text="Задание 5",
        callback_data="ex_5")
    )
    builder.add(types.InlineKeyboardButton(
        text="Задание 9",
        callback_data="ex_9")
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
    await callback.message.answer("Всё верно!", reply_markup=builder.as_markup())

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
    await callback.message.answer("К сожалению, это не верный ответ", reply_markup=builder.as_markup())

@dp.callback_query(F.data == "ex_5")
async def send_new_ex_5(callback: types.CallbackQuery):
    await callback.message.delete()
    builder = InlineKeyboardBuilder()
    data = Functions.get_the_fifth_task()
    for i in data[0]:
        if data[0].index(i)+1 == data[2]:
            builder.add(types.InlineKeyboardButton(
                text=f"{i}",
                callback_data="true_answer_ex_5")
            )
        else:
            builder.add(types.InlineKeyboardButton(
                text=f"{i}",
                callback_data="false_answer_ex_5")
            )
    await callback.message.answer(
        f"""Выберите слово, значение которого представлено ниже: \n\n{data[1]}""", 
        reply_markup=builder.as_markup())


@dp.callback_query(F.data == "true_answer_ex_5")
async def true_answer_ex_5(callback: types.CallbackQuery):
    await callback.message.delete()
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
                text=f"Продолжить",
                callback_data="ex_5")
            )
    builder.add(types.InlineKeyboardButton(
        text="Главное меню",
        callback_data="menu")
    )
    await callback.message.answer("Всё верно!", reply_markup=builder.as_markup())

@dp.callback_query(F.data == "false_answer_ex_5")
async def false_answer_ex_5(callback: types.CallbackQuery):
    await callback.message.delete()
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
                text=f"Продолжить",
                callback_data="ex_5")
            )
    builder.add(types.InlineKeyboardButton(
        text="Главное меню",
        callback_data="menu")
    )
    await callback.message.answer("К сожалению, это не верный ответ", reply_markup=builder.as_markup())


@dp.callback_query(F.data == "ex_9")
async def send_new_ex_9(callback: types.CallbackQuery):
    await callback.message.delete()
    builder = InlineKeyboardBuilder()
    data = Functions.get_the_ninth_task()
    for i in data[1]:
        if i == data[0]:
            builder.add(types.InlineKeyboardButton(
                text=f"{i}",
                callback_data="true_answer_ex_9")
            )
        else:
            builder.add(types.InlineKeyboardButton(
                text=f"{i}",
                callback_data="false_answer_ex_9")
            )
    await callback.message.answer("Выберите верно написанное слово:", reply_markup=builder.as_markup())

@dp.callback_query(F.data == "true_answer_ex_9")
async def true_answer_ex_9(callback: types.CallbackQuery):
    await callback.message.delete()
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
                text=f"Продолжить",
                callback_data="ex_9")
            )
    builder.add(types.InlineKeyboardButton(
        text="Главное меню",
        callback_data="menu")
    )
    await callback.message.answer("Всё верно!", reply_markup=builder.as_markup())

@dp.callback_query(F.data == "false_answer_ex_9")
async def false_answer_ex_9(callback: types.CallbackQuery):
    await callback.message.delete()
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
                text=f"Продолжить",
                callback_data="ex_9")
            )
    builder.add(types.InlineKeyboardButton(
        text="Главное меню",
        callback_data="menu")
    )
    await callback.message.answer("К сожалению, это не верный ответ", reply_markup=builder.as_markup())

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


