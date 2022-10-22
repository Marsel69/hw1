from aiogram import types, Dispatcher
from config import bot, dp, ADMINS
from database.bot_db import sql_command_all
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer('Ты не АДМИН!')
    else:
        mentors = await sql_command_all()
        for mentor in mentors:
            await bot.send_message(message.chat.id, f'ID: {mentor[0]}\n'
                                                    f'Name: {mentor[1]}\n'
                                                    f'Direction: {mentor[2]}\n'
                                                    f'Age: {mentor[3]}\n'
                                                    f'Group: {mentor[4]}',
                                   reply_markup=InlineKeyboardMarkup().add(
                                       InlineKeyboardButton(f'Delete {mentor[1]}', callback_data=f'delete {mentor[0]}')
                                   ))


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(delete_data, commands=['del'])