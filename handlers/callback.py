from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
from database.bot_db import sql_command_delete

# @dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_1)

    question = 'создатель Minecraft??'
    answers = [
        "Йенс Бергенстен",
        'Джеймс Гослинг',
        'Маркус Перссон',
        'Брин Сергей'
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="В гугле посмотри",
        open_period=10,
        reply_markup=markup
    )
# @dp.callback_query_handler(lambda call: call.data == 'button_call_2')
async def quiz_3(message: types.Message):
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
        correct_option_id=1,
        explanation="В гугле посмотри",
        open_period=10,
    )


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(int(call.data.replace("delete ", "")))
    await call.answer(text="Удален из БД", show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == 'button_call_2')
    dp.register_callback_query_handler(complete_delete, lambda call: call.data and call.data.startswith("delete "))
