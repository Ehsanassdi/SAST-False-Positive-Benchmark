import sqlite3

username = input("Username: ")

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

sql = "SELECT * FROM users WHERE username = ?"

cursor.execute(sql, (username,))

rows = cursor.fetchall()

print(rows)

connection.close()
