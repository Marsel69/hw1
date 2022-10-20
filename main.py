from aiogram.utils import executor
from config import dp
import logging
from handlers import client, callback, extra, fsmAdminMentor

callback.register_handlers_callback(dp)
client.register_handler_client(dp)
fsmAdminMentor.register_handlers_fsm_AdminMentor(dp)

extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

