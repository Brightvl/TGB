from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# импортируем библиотеку поля для кнопок и кнопки

#  Здесь будут примитивные клавиатуры

# для клавиатуры сначала нужно создать доску
kb_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# resize для уменьшения самих кнопок в приложении
# one_time_k для того чтобы после нажатия клавиатура скрылась

# Теперь делаем кнопки

btn_start = KeyboardButton(text='/start')
btn_help = KeyboardButton(text='/help')
btn_mother = KeyboardButton(text='мама')
btn_location = KeyboardButton(text='Локация', request_location=True)
btn_phone = KeyboardButton(text='Телефон', request_contact=True)

kb_main.add(btn_start, btn_help)
kb_main.add(btn_mother)
kb_main.add(btn_location, btn_phone)

# remover = ReplyKeyboardRemove() #Удаляет кнопки полностью