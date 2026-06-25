import sqlite3

role = input("Role: ")

db = sqlite3.connect("accounts.db")
cursor = db.cursor()

cursor.execute(
    "SELECT username FROM users WHERE role = ?",
    (role,)
)

print(cursor.fetchall())

db.close()
