from aiogram import Dispatcher, Bot
import os


# Бот главная фигура, но к нему почти никогда не обращаемся
# Мы спрятали токен в виртуальное окружение теперь можно спокойно пушить на гитхаб
bot = Bot(token=os.getenv('TOKEN'))  # Диспетчер работает на бота
dp = Dispatcher(bot)
