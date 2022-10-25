import asyncio

from aiogram.utils import executor
from config import dp
import logging
from handlers import client, callback, extra, fsmAdminMentor, admin, notifications
from database.bot_db import sql_create

async def on_startup(_):
    asyncio.create_task(notifications.sheduler())
    sql_create()


admin.register_handlers_admin(dp)
callback.register_handlers_callback(dp)
client.register_handler_client(dp)
fsmAdminMentor.register_handlers_fsm_AdminMentor(dp)
notifications.register_handlers_notification(dp)

extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

