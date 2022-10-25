import asyncio

import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer("Братан не беспокойся я напомню")



async def information():
    await bot.send_message(chat_id=chat_id, text="Забери справку после колледжа!!")

async def sheduler():
    aioschedule.every().thursday.at('13:55').do(information)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)

def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: "напомни в понидельник забрать справку" in word.text)

