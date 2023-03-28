from loader import dp
from aiogram.types import Message


@dp.message_handler(commands=['help'])
async def help_command(message: Message):
    name = await help_helper(message)
    await message.answer(f'Бог поможет, {name}')
    # Прописываем что будет делать хэндлер


async def help_helper(message: Message):
    user = message.from_user.first_name
    user = 'уважаемый ' + user
    return user
