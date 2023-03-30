from aiogram.types import Message  # Класс Message

from Handlers.help import get_name
from Keyboards import kb_main
from loader import dp


# Хэндлер объявляется с помощью декоратора @

# хэндлер - это грубо говоря рука бота, которая
# будет выполнять определенную функцию в ответ на определенный «раздражитель»
# Нужен декоратор (что это пока непонятно, но скорее всего нижняя строка)

@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    name = await get_name(message)
    await message.answer(f'Здравствуй {await get_name(message)}'
                         f'\nВыбери что нибудь', reply_markup=kb_main)
    # Прописываем что будет делать хэндлер
# reply_markup = kb_main это мы включили отображение кнопок которое находится в папке kb_main
