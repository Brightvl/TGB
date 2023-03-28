from loader import dp
from aiogram.types import Message  # Класс Message
from Handlers.help import help_helper
from Keyboards import kb_main


# Хэндлер объявляется с помощью декоратора @

# хэндлер - это грубо говоря рука бота, которая
# будет выполнять определенную функцию в ответ на определенный «раздражитель»
# Нужен декоратор (что это пока непонятно, но скорее всего нижняя строка)

@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    name = await help_helper((message))
    await message.answer(f'Здравствуй {name}\nВыбери что нибудь', reply_markup=kb_main)
    # Прописываем что будет делать хэндлер
# reply_markup = kb_main это мы ключили отображение кнопок которое находится в папке kb_main
