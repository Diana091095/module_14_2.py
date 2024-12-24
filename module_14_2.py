import sqlite3

connection = sqlite3.connect("not_telegram.db")
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

cursor.execute("CREATE INDEX IF NOT EXISTS idx_id ON Users(id)")

for i in range(1, 11, 1):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
                   (f"User{i}", f"example{i}@gmail.com", f"{10 * i}", "1000"))

for i in range(1, 11, 2):
    cursor.execute(" UPDATE Users SET balance = ? WHERE username = ?",(500, f"User{i}"))
#
for i in range(1,11,3):
    cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i}",))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
result = cursor.fetchall()
for all in result:
    print(f'Имя: {all[0]} | Почта: {all[1]} | Возраст: {all[2]} | Баланс: {all[3]}')

for i in range(1,11,3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
# cursor.execute("SELECT AVG(balance) from Users")
# avg_balance = cursor.fetchone()[0]

print(all_balances/total_users)

connection.commit()
connection.close()