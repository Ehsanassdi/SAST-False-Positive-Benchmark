import sqlite3

email = input("Email: ")

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute(
    "SELECT * FROM users WHERE email = ?",
    (email,)
)

print(cursor.fetchall())

connection.close()
