# import random
from aiogram import types, Dispatcher
from config import bot, dp
# @dp.message_handler()
async def echo(message: types.Message):
    username = f'@{message.from_user.username}' \
        if message.from_user.username is not None else message.from_user.full_name
    # print(message)
    # if message.text.isnumeric():
    #     await bot.send_message(message.from_user.id, int(message.text) ** 2)
    # else:
    mat = ["чмо", "ублюдок", "падлa"]
    for word in mat:
        if word in message.text.lower():
            await bot.delete_message(message.chat.id, message.message_id)
            await message.answer(
                f'Не матерись {username},   Сам ты {word}   если опять будешь материца забанью '
            )


    # if message.text.startswith('game'):
    #     await bot.send_dice(message.message_id, emoji='⚽')

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)


