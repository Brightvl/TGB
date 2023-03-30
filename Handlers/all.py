from loader import dp
from aiogram.types import Message

# all реагирует на все вообще поэтому нет команд в функции(ЖАДНАЯ ПАДЛА)

@dp.message_handler()
async def help_command(message: Message):
    await message.answer(f'{message.from_user.first_name}, я не знаю что это значит, у меня нет для тебя ответа')
    # Прописываем что будет делать хэндлер
    # {message.text}

