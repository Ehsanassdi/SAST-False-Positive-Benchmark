import sqlite3

role = input("Enter role: ")

conn = sqlite3.connect("accounts.db")
cursor = conn.cursor()

cursor.execute("SELECT username FROM users WHERE role = ?", (role,))

print(cursor.fetchall())

conn.close()
