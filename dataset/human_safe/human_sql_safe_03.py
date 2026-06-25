import sqlite3

user_id = int(input("Enter user ID: "))

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("SELECT username FROM users WHERE id = ?", (user_id,))

print(cursor.fetchone())

conn.close()
