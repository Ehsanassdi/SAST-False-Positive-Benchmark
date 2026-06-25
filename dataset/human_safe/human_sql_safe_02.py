import sqlite3

email = input("Enter email: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users WHERE email = ?", (email,))

print(cursor.fetchall())

conn.close()
