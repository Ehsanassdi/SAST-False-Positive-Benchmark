import sqlite3

username = input("Enter username: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users WHERE username = ?", (username,))

for row in cursor.fetchall():
    print(row)

conn.close()
