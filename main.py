from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import bot, dp
import logging


@dp.message_handler(commands=['start', 'info'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"Приветик {message.from_user.first_name}!")
    # await message.answer("This is answer method")
    # await message.reply("This is reply method")

@dp.message_handler(commands=['mem'])
async def mem_command(message: types.Message):
    photo = open('media/mem.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = 'Кто создаль Facebook ?'
    answers = [
        "Марсель",
        'Ророноа Зоро',
        'Марк Цукерберг',
        'Джеймс Гослинг',

    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="В гугле посмоти",
        open_period=10,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(message: types.Message):
    question = 'создатель Java??'
    answers = [
        "Йенс Бергенстен",
        'Джеймс Гослинг',
        'Маркус Перссон',
        'Брин Сергей'
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="В гугле посмотри",
        open_period=10,
    )


@dp.message_handler()
async def echo(message: types.Message):
    # print(message)

    if message.text.isnumeric():
        await bot.send_message(message.from_user.id, int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
