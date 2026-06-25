import sqlite3

role = input("Role: ")

conn = sqlite3.connect("accounts.db")
cursor = conn.cursor()

query = f"SELECT username FROM users WHERE role = '{role}'"
cursor.execute(query)

print(cursor.fetchall())
conn.close()
