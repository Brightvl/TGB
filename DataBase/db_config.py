# import sqlite3
#
# PATH = "DataBase/db_TGBot.db"
#
# connect = sqlite3.connect(PATH)
# cursor = connect.cursor()
#
#
# def create_table():
#     cursor.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR,
#     tg_id INTEGER, phone VARCHAR, comment VARCHAR)''')
#     connect.commit()
# # CREATE TABLE IF NOT EXISTS – создай таблицу, если такая не существует
# users – а это название нашей таблицы, в скобках указывается название столбца и тип данных, а через запятую название
# и тип данных следующего столбца.
# PRIMARY KEY – означает, что этот столбец будет использоваться как ключ
# AUTOINCREMENT – автоматическое заполнение столбца с созданием уникального значения для каждой строки
