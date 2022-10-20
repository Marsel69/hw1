from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


from config import bot
from keyboards.client_kb import cancel_markup

class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    nap = State()
    age = State()
    group = State()

async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.id.set()
        await message.answer(f'Приветик {message.from_user.full_name}\n'
                             f'Напиши свой айди', reply_markup=cancel_markup)
async def load_id(message: types.Message, state: FSMContext):
    try:
        Mentor_id = int(message.text)
        if Mentor_id < 0 or Mentor_id > 10000000000:
            await message.answer(f"не правильно написал айди!"
                                 f"напиши заново")
            return
        else:
            async with state.proxy() as data:
                data['ID'] = Mentor_id
        await FSMAdmin.next()
        await message.answer("напиши свое имя?", reply_markup=cancel_markup)
    except:
        await message.answer("айди должен быть только из цифр")

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("какое у тебя направленния?", reply_markup=cancel_markup)
async def load_nap(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['nap'] = message.text
    await FSMAdmin.next()
    await message.answer("сколько тебе лет?", reply_markup=cancel_markup)
async def load_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        if age < 15:
            await message.answer("Ты слишком маленький для ментора")
            return
        elif age > 40:
            await message.answer('Ты слишком стар для ментора')
            return
        else:
            async with state.proxy() as data:
                data['age'] = int(message.text)
            await FSMAdmin.next()
            await message.answer('Введите группу', reply_markup=cancel_markup)
    except:
        await message.answer('Вводи только число')
async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await message.answer(f"ID: {data['ID']}    Имя: {data['name']}\n"
                            f"Направление: {data['nap']}   Возраст: {data['age']}   Группа: {data['group']}")
        await state.finish()
        await message.answer('Регистрация закончена!')

async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Ну и пошел ты нах")
    else:
        await message.answer('Ты не регистрируешься')


def register_handlers_fsm_AdminMentor(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True),
                                state='*')
    dp.register_message_handler(fsm_start, commands=['register'])

    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_nap, state=FSMAdmin.nap)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)


