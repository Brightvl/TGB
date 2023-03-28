# Bot и Dispatcher это классы поэтому с большой буквы
from aiogram import Bot, Dispatcher  # Из aiogram импортируем Bot и Dispatcher
from aiogram.utils import executor
from Handlers import dp  # По сути мы импортировали список handlers-ов из файла __init__


# Функция для отображения работоспособности бота.
# Когда запущен будет выдавать это сообщение
# И мы можем приступать к каким то движениям
# Функция используется в executor
# async функция позволяет выполнять функцию не по порядку
# async - объявляем. await - вызываем
async def on_start(_):
    print('Бот запущен!')


# executor - нужен чтобы бот начал выполнять те функции, что на него возложены
# start_polling - Долгое прослушивание постоянно кидает запрос на телеграм сервер и если что-то приходит он это
# возвращает
executor.start_polling(dp, skip_updates=True, on_startup=on_start)
# Executor - исполнитель работает на dp
# skip_updates=True - Для того чтобы пока наш бот лежит в отключке Если приходят какие-то апдейты для нас их не копили
# По сути игнорит все сообщения пока бот в отключке
# ПРи запуске фраза Updates were skipped successfully. Будет сигнализировать о пропуске не нужных обращений
