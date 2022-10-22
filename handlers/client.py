from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
from keyboards.client_kb import start_markup
from database.bot_db import sql_command_random
# async def pin_command(message: types.Message):
#     if message.reply_to_message:
#         await bot.pin_chat_message(message.chat.id, message.reply_to_message.from_user.id)
# @dp.message_handler(commands=['start', 'info'])

async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"Приветик {message.from_user.first_name}!",
                           reply_markup=start_markup)
    # await message.answer("This is answer method")
    # await message.reply("This is reply method")
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"Надо было учиться {message.from_user.first_name}")
# @dp.message_handler(commands=['mem'])
async def mem_command(message: types.Message):
    photo = open('media/mem.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


# @dp.message_handler(commands=['quiz'])
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
async def get_random_user(message: types.Message):
    await sql_command_random(message)



def register_handler_client(dp: Dispatcher):
    # dp.register_message_handler(pin_command, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(start_command, commands=['start', 'info'])
    dp.register_message_handler(quiz_1, commands=['test'])
    dp.register_message_handler(mem_command, commands=['mem'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(get_random_user, commands=['get'])

