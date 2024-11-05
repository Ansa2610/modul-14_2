import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(  
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# Заполните её 10 записями:
# for i in range(10):
# 	n = i + 1
# 	cursor.execute("INSERT INTO Users (username, email, age, balance)"
# 						"VALUES (?, ?, ?, ?)", (f'User{n}',
# 						f'example{n}@gmail.com', f'{n*10}', '1000')
# 				   )

# Обновите balance у каждой 2-ой записи, начиная с 1ой на 500:
# for i in range(10):
#     if i % 2 == 0:
#         n = i + 1
#         cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, f"{n}"))

# Удалите каждую 3ую запись в таблице, начиная с 1ой:
# for i in range(10):
#     if i % 3 == 0:
#         n = i + 1
#         cursor.execute("DELETE FROM Users WHERE id = ?", (f"{n}",))

# Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60:

# cursor.execute("SELECT * FROM Users WHERE age != 60")
# result = cursor.fetchall()
# for user in result:
# 	print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | '
# 		  f'Баланс: {user[4]}')

# Удаление пользователя с id=6
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

# Подсчёт кол-ва всех пользователей
cursor.execute("SELECT COUNT(*) FROM Users ")
all_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

print(all_balances / all_users)

connection.commit()
connection.close()
