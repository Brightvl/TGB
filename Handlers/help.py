from aiogram.types import Message

from loader import dp


@dp.message_handler(commands=['Помощь'])
async def help_annotation(message: Message):
    await message.answer(f'Привет, {await get_username(message)}, ты пока располагайся а мы придумаем правила')


# async def help_command(message: Message):
#     name = await help_helper(message)
#     await message.answer(f'Бог поможет, {name}')
#     # Прописываем что будет делать хэндлер


# Выдает имя
async def get_name(message: Message):
    return message.from_user.first_name


# Выдает никнейм
async def get_username(message: Message):
    return message.from_user.username
