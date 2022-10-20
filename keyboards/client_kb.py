from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
)

start_button = KeyboardButton("/start")
help_button = KeyboardButton("/help")
test_button = KeyboardButton("/test")
mem_button = KeyboardButton("/mem")
register_button = KeyboardButton("/register")
start_markup.add(start_button, help_button, test_button, mem_button, register_button)

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('CANCEL'))


